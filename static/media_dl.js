$(document).on("click", ".dl-media", function (e) {
    let url = $(this).attr("data-ql");
    let media_name;
    let verify = url.match(/\.mp4/i);
    if (verify) {
        media_name = `${Date.now()}.mp4`;
    } else {
        media_name = `${Date.now()}.jpg`;
    }
    fetch(url)
        .then((res) => res.blob())
        .then((blob) => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.style.display = "none";
            a.href = url;
            a.download = media_name;
            document.body.appendChild(a);
            a.click();
        });
});
