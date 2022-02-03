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
                if (data) {
                    is_result = true
                }
                const {links, preview, error} = data
                let {profile_url, full_name, biography} = links
                try {
                    if (error) {
                        is_error = error
                        return;
                    }
                } catch {
                    console.log('No Errors!')
                }

                full_name = `${full_name}`;
                biography = biography.replace(/\n/g, "<br>");
                raw_html += `<div class='media'><img style='border-radius:50%;' src='${preview}' alt='media' /></div>`;
                raw_html += `<h2>${full_name}</h2>`;
                raw_html += `<p>${biography}</p>`;
                raw_html += `<br><a href='javascript:void(0)' class="dl-media" data-ql="${preview}" style='border-radius:5px;'>Download DP</a>`;
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
                    $(".wait").css("display", "none");
                    $(".results").css("display", "flex");
                    $(".results").html(
                        `<h2 style="color:red;padding:5px;border-bottom:2px solid blue;font-style:italic;">${is_error}</h2>`
                    );
                }
            } catch {
                console.log('No Errors!')
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
    })
});
