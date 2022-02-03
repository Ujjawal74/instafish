$(function () {
    let s_num = parseInt($(".captchaBlock").html());
    let path = window.location.pathname;
    $(".results").css("display", "none");
    let is_result = false
    let is_error;
    let raw_html = ``;
    const pattern = /(instagram\.com)/i;

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
            body: JSON.stringify({url: url}),
        })
            .then((res) => res.json())
            .then((data) => {
                if(data){
                    is_result = true
                }
                const {links, preview, error} = data
                try {
                    if (error) {
                        is_error = error
                        return;
                    }
                } catch {
                    console.log('No Errors!')
                }

                preview.forEach((val, index) => {
                    let video = val.match(/\.mp4/i);
                    if (video) {
                        raw_html += `<div class='media'><video src='${val}' controls></video><a href='javascript:void(0)' class="dl-media" data-ql="${val}">Download</a></div>`;
                    } else {
                        raw_html += `<div class='media'><img src='${val}' alt='media' /><a href='javascript:void(0)' class="dl-media" data-ql="${val}">Download</a></div>`;
                    }
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

    $("#get_data").on('click', () => {
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
            try {
                if (is_error) {
                    console.log('tick')
                    $(".wait").css("display", "none");
                    $(".results").css("display", "flex");
                    $(".results").html(
                        `<h2 style="color:red;padding:5px;border-bottom:2px solid blue;font-style:italic;">${is_error}</h2>`
                    );
                }
            } catch {
                console.log('No errors')
            }

            runTicker();
            $(".results").css("display", "none");
            $("#url").val("");

            if (is_result) {
                $(".results").css("display", "flex");
                $(".results").html(raw_html);
            } else {
                $(".wait").css("display", "block");
                $(".wait").append("<img src='image.gif' alt='wait' />");
            }
        } else {
            alert("Please Fill The Correct Captcha!");
        }
    });
});
