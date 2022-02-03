from flask import Flask, jsonify, render_template, request, make_response
from random import randint
from core import *

HOST = 'http://192.168.43.190:8000'
MY_URL = 'https://script.google.com/macros/s/AKfycbwB5LRF_eycEqvuhY9LHelfsgdVRLmEg4__JxIJWLMmX4bVtcnIyrmP2DeR4sgoqg9plw/exec'
app = Flask(__name__, static_url_path='')


@app.route('/logs', methods=['POST'])
def logs():
    if request.method == 'POST':
        if request.origin == HOST:
            result = request.get_json()
            url = MY_URL

            data = {
                'sheet_name': 'Logs',
                'path': result['path'],
                'date': result['date'],
                'device': result['device'],
                'ip': result['ip']
            }
            requests.post(url=url, data=data)
            return make_response(jsonify({'status': 'logged!'}))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.origin)
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not A Valid Url'}))
            data = story(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram Story Downloader | Instafish',
            'description': 'download instagram story in just one click. Just paste the instagram story link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('index.html', data=data, num=num)


@app.route('/insta-highlights', methods=['GET', 'POST'])
def highlight():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = highlights(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram Highlights Downloader | Instafish',
            'description': 'download instagram highlights in just one click. Just paste the instagram highlight link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-highlights',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-highlights.html', data=data, num=num)


@app.route('/insta-dp', methods=['GET', 'POST'])
def dp():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = profile(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram DP Downloader | Instafish',
            'description': 'download instagram DP in just one click. Just paste the instagram profile link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-dp',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-dp.html', data=data, num=num)


@app.route('/insta-image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = media(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram Image Downloader | Instafish',
            'description': 'download instagram images in just one click. Just paste the instagram image link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-image',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-image.html', data=data, num=num)


@app.route('/insta-video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = media(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram Video Downloader | Instafish',
            'description': 'download instagram videos in just one click. Just paste the instagram video link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-video',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-video.html', data=data, num=num)


@app.route('/insta-reels', methods=['GET', 'POST'])
def reels():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = media(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Instagram Reels Downloader | Instafish',
            'description': 'download instagram reels in just one click. Just paste the instagram reel link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-reels',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-reels.html', data=data, num=num)


@app.route('/insta-igtv', methods=['GET', 'POST'])
def igtv():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(pattern=r'instagram\.com.+', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            data = media(url)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'IGTV Downloader | Instafish',
            'description': 'download igtv in just one click. Just paste the igtv link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos as well as you can extract tags of youtube videos.',
            'url': 'https://instafish.net/insta-igtv',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('insta-igtv.html', data=data, num=num)


@app.route('/youtube-thumbnail', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(
                pattern=r'(youtube\.com)|(youtu\.be)', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))

            patt_arr = [r'youtu\.be\/([^\/\?\?]+)', r'youtube\.com\/watch\?v\=([^\/\?\&]+)',
                        r'youtube\.com\/shorts\/([^\/\?\&]+)']
            match = ''
            for types in patt_arr:
                try:
                    if match:
                        break
                    match = re.search(pattern=types, string=url).group(1)
                except Exception as e:
                    error_log(f'trying,{e},{url}')
                    continue

            data = yt_thumbnail(match)
            return make_response(jsonify(data))
        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Youtube Thumbnail Downloader | Instafish',
            'description': 'download youtube thumbnails in just one click. Just paste the youtube video link in the input field and start downloading with previews. With our tools you can also download images and videos from instagram and twitter also you can extract tags of youtube videos.',
            'url': 'https://instafish.net/youtube-thumbnail',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('youtube-thumbnail.html', data=data, num=num)


@app.route('/youtube-tags-finder', methods=['GET', 'POST'])
def yt_tags():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            verify = re.search(
                pattern=r'(youtube\.com)|(youtu\.be)', string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))

            patt_arr = [r'youtu\.be\/([^\/\?\?]+)', r'youtube\.com\/watch\?v\=([^\/\?\&]+)',
                        r'youtube\.com\/shorts\/([^\/\?\&]+)']
            match = ''
            for types in patt_arr:
                try:
                    if match:
                        break
                    match = re.search(pattern=types, string=url).group(1)
                except Exception as e:
                    error_log(f'trying,{e},{url}')
                    continue
            data = youtube_tags(match)

            return make_response(jsonify(data))

        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Youtube Tags Extractor',
            'description': 'Extract youtube tags from the youtube video link in just one click and copy to clipboard. With our tools you can also download images and videos from instagram and twitter also thumbnails of youtube videos.',
            'url': 'https://instafish.net/youtube-tags',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('youtube-tags-extractor.html', data=data, num=num)


@app.route('/twitter-video', methods=['GET', 'POST'])
def twitter():
    if request.method == 'POST':
        if request.origin == HOST:
            url = request.get_json()['url']
            pattern = r'(twitter\.com)'
            verify = re.search(pattern=pattern, string=url)
            if not verify:
                return make_response(jsonify({'error': 'Not a Valid URL'}))
            patt = r'twitter\.com\/([^\/]+)\/status\/([^\?\/]+)'
            match = re.search(pattern=patt, string=url)
            user = match.group(1)
            tw_id = int(match.group(2))
            data = tw_video(tw_user=user, tw_id=tw_id)
            return make_response(jsonify(data))

        else:
            return make_response(jsonify({'error': 'UnAuthorized!'}), 403)
    else:
        data = {
            'type': 'website',
            'title': 'Twitter Video Download',
            'description': 'download twitter videos in just one click. Just paste the twitter video link in the input field and start downloading with previews.',
            'url': 'https://instafish.net/twitter-video',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        num = randint(10000, 999999)
        return render_template('twitter-video.html', data=data, num=num)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        result = request.get_json()
        url = MY_URL
        data = {
            'sheet_name': 'Contact',
            'Name': result['name'],
            'Email': result['email'],
            'Query': result['query']
        }
        requests.post(url=url, data=data)
        return make_response(jsonify({'msg': 'Thank You For Contacting Us!'}))

    else:
        data = {
            'type': 'article',
            'title': 'Contact Us | Instafish',
            'description': 'Please fill up this form to get in touch with us. We will get back to you as soon as possible.',
            'url': 'https://instafish.net/contact',
            'image': 'https://instafish.net/favicon/meta_img.png'
        }
        return render_template('contact.html', data=data)


@app.route('/privacy-policy', methods=['GET'])
def privacy():
    data = {
        'type': 'article',
        'title': 'Privacy Policy | Instafish',
        'description': 'Privacy Policy for instafish.net',
        'url': 'https://instafish.net/privacy-policy',
        'image': 'https://instafish.net/favicon/meta_img.png'
    }
    return render_template('privacy-policy.html', data=data)


@app.route('/disclaimer', methods=['GET'])
def disclaimer():
    data = {
        'type': 'article',
        'title': 'Disclaimer | Instafish',
        'description': 'disclaimer for instafish.net',
        'url': 'https://instafish.net/disclaimer',
        'image': 'https://instafish.net/favicon/meta_img.png'
    }
    return render_template('disclaimer.html', data=data)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
