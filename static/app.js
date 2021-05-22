$(".active").on("submit", handleSubmit);

score = 0;

time = 60;

endGame(15000);
// clock();

async function handleSubmit(e) {
  e.preventDefault();
  $word = $("#guess");
  $message = $("#message");
  $score = $("#score");

  try {
    response = await axios.post(`/submit/${$word.val()}`, {
      params: { word: $word },
    });

    if (response.data.result === "ok") {
      $message.text(response.data.result);
      word = response.data.word;
      score += word.length;
      $score.text(score);
    } else if (response.data.result === "not-on-board") {
      $message.text(response.data.result);
    }
    $word.val("");
  } catch {
    $message.text("not a word");
    $word.val("");
  }
}

const clock = setInterval(() => {
  if (time >= 0) $("#clock").text(time);
  time--;
}, 1000);

function endGame(time = 60000) {
  setTimeout(gameOver, time);
}

function gameOver() {
  $body = $("body");
  $body.css("opacity", 0.5);

  $("#message").text("Game Over");

  clearInterval(clock);

  $("#clock").text(0);

  $("form").hover(diableForm);

  publishScore();
}

function diableForm() {
  $("form").hide();
  $message = $("#message");
  $message.text("Would you like to start a new game?");
}

async function publishScore() {
  response = await axios.post(`/score`, { score: score });

  return response;
}
