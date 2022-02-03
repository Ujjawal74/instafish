from datetime import  datetime
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Mobile Safari/537.36",
    "Content-Type": "application/json; charset=utf-8",
    "Cookie": "ig_did=C0CB90DA-0D57-468D-8576-EA8E3AD6B8F4; mid=YDdfOgAEAAFOWcvoQ8tYZwzA7dt3; ig_nrcb=1; sessionid=4207735234%3A9IWlwhYdBMVB9u%3A25; shbid=12866; shbts=1614415803.8560727; csrftoken=z70fSa0ofO84aDh2ZK449sChUJQmsNil; rur=RVA; ds_user_id=4207735234",
    "x-asbd-id": "198387",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "hmac.AR1Y4zoDpEVl6cYBqP5O18md_sXGiiXDD9cc3LvPmR3Uv0iu"
}


def yt_headers(video_id):
    yt_headers = {
        'authorization': 'SAPISIDHASH 1641537738_947cb095d25eeffedc23d342d08a656941c0f4dc',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20220106.01.00',
        'x-goog-authuser': '0',
        'x-goog-visitor-id': 'Cgs3MmhGUkFhTWdfZyiKwd-OBg%3D%3D',
        'sec-ch-ua-platform': '"Linux"',
        'accept': '*/*',
        'origin': 'https://www.youtube.com',
        'x-client-data': 'CIq2yQEIo7bJAQipncoBCKDZygEI6vLLAQie+csBCNb8ywEI54TMAQi1hcwBCK2OzAEI/Y7MAQiZj8wBCNKPzAEI2ZDMARiMnssB',
        'referer': f'https://www.youtube.com/watch?v={video_id}',
        'cookie': f'SID=FAj8l_EqbzNGtpnFDO3My57wwB2rO68u_QxONMXWXc0vyiWzOTe5tQTNf0LzMzHDNR1lLg.; __Secure-1PSID=FAj8l_EqbzNGtpnFDO3My57wwB2rO68u_QxONMXWXc0vyiWzez4u4M-4BAipdZAeVPYJmQ.; __Secure-3PSID=FAj8l_EqbzNGtpnFDO3My57wwB2rO68u_QxONMXWXc0vyiWzDVHcUy2J6EBl-7CWFylRFA.; HSID=ABBx4Ac7dBADhCnXN; SSID=AraXYlKOAALQGkKpZ; APISID=l4t4Xieot_A8fWAW/APSq9tkupdJfB9vy6; SAPISID=N9zGX5-P6CvcO5iE/Awg7qr_KNctvfZmYo; __Secure-1PAPISID=N9zGX5-P6CvcO5iE/Awg7qr_KNctvfZmYo; __Secure-3PAPISID=N9zGX5-P6CvcO5iE/Awg7qr_KNctvfZmYo; VISITOR_INFO1_LIVE=72hFRAaMg_g; LOGIN_INFO=AFmmF2swRQIhANbfUKemVMNJuzKZEr57mNQtBeW6FbDzn94NPF8MUeLuAiAq9zaF9ryqsXJLNW74jXK4pApx3YfTszsKpVD1ryCW0g:QUQ3MjNmd1hNOTNxX3BGYjNabEZIc0YyUjg0OUl2dU1RWXZmdzBnX1RhdVBKTDFrSENNcmEzcXF6THp6RW11ZWRpMnhPZ0JLUktDajJtdUQ5cXA4ZXBMQ0Q5MUZPNUhxN3BHbG9oaXF3U0hVTEZ6aFlzUEtxcTZpc2hFSk1BWms1TndDWW5VbjRqSWlzeGRwMktQMml4RUdwbXpLZ2R6U1JR; PREF=f4=4000000&tz=Asia.Calcutta; YSC=praq-Ub1DCI; SIDCC=AJi4QfE_tX3d6NEZyAuGbpvqQG0bNXZsHYj1UJryh3PbFiQB_qY37U_I9kLNN9Ro7cYVraYkbIM; __Secure-3PSIDCC=AJi4QfHxbk48EeepqPMbQLhMfy-gspeQjdMzrr8Q5MEjqWhweusgwPi4ctTeO1L6ndcZAYV7nQ; ST-v976y7=itct=CMICENwwIhMIt-DvvYSf9QIVhIvYBR2y6ARrMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D&csn=MC4zNjU3MTM2ODA3ODgzODUy&endpoint=%7B%22clickTrackingParams%22%3A%22CMICENwwIhMIt-DvvYSf9QIVhIvYBR2y6ARrMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3D{video_id}%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22{video_id}%22%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Frr2---sn-ci5gup-qxar.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26orc%3D1%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26msp%3D1%26odeak%3D1%26odepv%3D1%26osfc%3D1%26id%3D88554e2e68f4ebce%26ip%3D2401%253A4900%253Ac05%253A64a7%253Ad438%253A8050%253Adab0%253Ae4dd%26initcwndbps%3D233750%26mt%3D1641537654%26oweuc%3D%26pxtags%3DCg4KAnR4EggyNDAyNzcwMA%26rxtags%3DCg4KAnR4EggyNDAyNzY5OQ%252CCg4KAnR4EggyNDAyNzcwMA%252CCg4KAnR4EggyNDAyNzcwMQ%252CCg4KAnR4EggyNDAyNzcwMg%252CCg4KAnR4EggyNDA2Nzg1NA%22%7D%7D%7D%7D%7D',
    }
    return yt_headers


def yt_payload(video_id):
    data = f'{{"context":{{"client":{{"hl":"en-GB","gl":"IN","remoteHost":"2401:4900:c05:64a7:d438:8050:dab0:e4dd","deviceMake":"","deviceModel":"","visitorData":"Cgs3MmhGUkFhTWdfZyiKwd-OBg%3D%3D","userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20220106.01.00","osName":"X11","osVersion":"","originalUrl":"https://www.youtube.com/watch?v={video_id}","screenPixelDensity":2,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{{"appInstallData":"CIrB344GEJHXrQUQstStBRCA6q0FEJjqrQUQt8utBRC7x_0SEJH4_BIQ2L6tBQ%3D%3D"}},"screenDensityFloat":1.5,"timeZone":"Asia/Calcutta","browserName":"Chrome","browserVersion":"97.0.4692.71","screenWidthPoints":614,"screenHeightPoints":587,"utcOffsetMinutes":330,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"4000000","clientScreen":"WATCH","mainAppWebInfo":{{"graftUrl":"/watch?v={video_id}","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":false}}}},"user":{{"lockedSafetyMode":false}},"request":{{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]}},"clickTracking":{{"clickTrackingParams":"CMICENwwIhMIt-DvvYSf9QIVhIvYBR2y6ARrMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngE="}},"adSignalsInfo":{{"params":[{{"key":"dt","value":"1641537675283"}},{{"key":"flash","value":"0"}},{{"key":"frm","value":"0"}},{{"key":"u_tz","value":"330"}},{{"key":"u_his","value":"5"}},{{"key":"u_h","value":"1080"}},{{"key":"u_w","value":"1920"}},{{"key":"u_ah","value":"985"}},{{"key":"u_aw","value":"1920"}},{{"key":"u_cd","value":"24"}},{{"key":"bc","value":"31"}},{{"key":"bih","value":"587"}},{{"key":"biw","value":"598"}},{{"key":"brdim","value":"0,27,0,27,1920,27,1920,985,614,587"}},{{"key":"vis","value":"1"}},{{"key":"wgl","value":"true"}},{{"key":"ca_type","value":"image"}}],"bid":"ANyPxKry3-SEKjBX5tLcH1WCp3dM-rprBjmI4n_1kkOlybP6kMmSVauc_wUIrmIRaRzX2j7i06ZRrLKXvQhqdamq5LNmePFyDg"}}}},"videoId":"{video_id}","playbackContext":{{"contentPlaybackContext":{{"currentUrl":"/watch?v={video_id}","vis":0,"splay":false,"autoCaptionsDefaultOn":false,"autonavState":"STATE_NONE","html5Preference":"HTML5_PREF_WANTS","signatureTimestamp":18997,"referer":"https://www.youtube.com/","lactMilliseconds":"-1"}}}},"racyCheckOk":false,"contentCheckOk":false}}'
    return data


tw_headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'guest_id_marketing=v1%3A164042085083830841; guest_id_ads=v1%3A164042085083830841; _sl=1; gt=1474658059720925185; _ga=GA1.2.1324835922.1640420854; _gid=GA1.2.1515655837.1640420854; g_state={"i_l":0}; kdt=7vWcCS6wi0SbAtxsmJNEx6okJQscS451EnRJLLXt; dnt=1; auth_token=b5561f06aca2ecb652fbb53846b5497fe03ee95b; personalization_id="v1_ELYCy7sXstA35CKETMKbgA=="; guest_id=v1%3A164042093426108509; ct0=6bd03c9b424efea8a7c51d638420f1b11f50f9600b4c15d0b9c22bfa91c743699175cb90433b57d421c60f82b4b611f7bee543905c4d3c1c68f24cf66d40607ae9bb91fd5ef18c711c744d418f4dc586; twid=u%3D2819810449; att=1-bFJ9Befo4T562J0KaWVkcobDsXOmHeFliIrhHBWG; lang=en; external_referer=8e8t2xd8A2w%3D|0|4abf247TNXg4Rylyqt4v49u2LWyy1%2FaFyfd602NkflM%3D',
    'x-csrf-token': '6bd03c9b424efea8a7c51d638420f1b11f50f9600b4c15d0b9c22bfa91c743699175cb90433b57d421c60f82b4b611f7bee543905c4d3c1c68f24cf66d40607ae9bb91fd5ef18c711c744d418f4dc586'
}


def error_log(error: str):
    with open('static/errors6291663217.logs', mode='a') as file:
        file.write(f'\n{error},{datetime.today()}')
    return 'Logged Error!'

# story_link = f'https://www.instagram.com/graphql/query/?query_hash=de8017ee0a7c9c45ec4260733d81ea31&variables=%7B%22reel_ids%22%3A%5B%22{user_id}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%7D'
