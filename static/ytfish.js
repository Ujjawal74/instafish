$(function () {
  let s_num = parseInt($(".captchaBlock").html());
  let path = window.location.pathname;
  $(".results").css("display", "none");
  let is_result = false;
  let is_error;
  let raw_html = ``;
  const pattern = /(youtube\.com)|(youtu\.be)/i;

  $("#url").on("input", function (e) {
    let url = e.target.value;
    let verify = url.match(pattern);

    if (!verify) {
      return;
    }

    fetch(`${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: url }),
    })
      .then((res) => res.json())
      .then((data) => {
        let { preview, resolutions, error } = data;
        try {
          if (!error) {
            is_result = true;
          }
        } catch {
          console.log("No Media Found!");
        }

        try {
          if (error) {
            is_error = error;
            return;
          }
        } catch {
          console.log("No Errors!");
        }

        preview.forEach((val, index) => {
          let source = val;
          let resolution = `Quality - ${resolutions[index]}`;
          let button = `<a href='javascript:void(0)' class='dl-media' data-ql='${val}' >Download</a>`;
          if (val === "No Media Found!") {
            resolution = `${resolutions[index]} Not Available!`;
            source = "https://img.youtube.com/notfound.jpg";
            button = ``;
          }
          raw_html += `<div class='media'><h3>${resolution}</h3><img src='${source}' alt='media' />${button}</div>`;
        });
      });
  });

  let ticker;

  function runTicker() {
    ticker = setInterval(checker, 1000);
  }

  function checker() {
    console.log("Waiting...");
    let check = $(".results").html();

    if (check !== "") {
      clearInterval(ticker);
      console.log("Waiting Over!");
    }

    if (raw_html) {
      $(".wait").css("display", "none");
      $(".results").css("display", "flex");
      $(".results").html(raw_html);
      raw_html = ``;
    }
  }

  $("#get_data").on("click", () => {
    let url = $("#url").val();

    let correct = url.match(pattern);
    let c_num = parseInt($("#verify").val());
    if (!url) {
      return alert("Please Fill The Url");
    }

    if (!correct) {
      return alert("Please Enter a Valid URL");
    }

    if (!c_num) {
      alert("Please Fill The Captcha!");
      return;
    }

    if (c_num === s_num) {
      $(".wait").css("display", "block");
      $(".wait").append("<img src='image.gif' alt='wait' />");
      try {
        if (is_error) {
          console.log("tick");
          $(".wait").css("display", "none");
          $(".results").css("display", "flex");
          $(".results").html(
            `<h2 style="color:red;padding:5px;border-bottom:2px solid blue;font-style:italic;">${is_error}</h2>`
          );
        }
      } catch {
        console.log("No errors");
      }

      runTicker();
      $("#url").val("");

      if (is_result) {
        $(".wait").css("display", "none");
        $(".results").css("display", "flex");
        $("results").html(raw_html);
      }
    } else {
      alert("Please Fill The Correct Captcha!");
    }
  });
});
