import requests
import re
from config import *


def media(url: str) -> dict:
    try:
        match = re.search(
            pattern=r'https\:\/\/www\.instagram\.com\/.*?\/([^\/]+)', string=url)
        fetch_link = match.group(0)
        media_url = f'{fetch_link}/?__a=1'
        shortcode = match.group(1)
        media_url2 = f'https://www.instagram.com/graphql/query/?query_hash=7d4d42b121a214d23bd43206e5142c8c&variables=%7B%22shortcode%22%3A%22{shortcode}%22%2C%22child_comment_count%22%3A3%2C%22fetch_comment_count%22%3A40%2C%22parent_comment_count%22%3A24%2C%22has_threaded_comments%22%3Atrue%7D'
        try:
            fetch = requests.get(url=media_url, headers=headers).json()
            result = fetch['items'][0]
        except Exception as e:
            try:
                error_log(f'trying,{e},{url}')
                fetch = requests.get(url=media_url2, headers=headers).json()
                result = fetch['data']['shortcode_media']
            except Exception as e:
                error_log(f'trying,{e},{url}')

            else:
                links = []

                if 'edge_sidecar_to_children' in result:
                    for item in result['edge_sidecar_to_children']['edges']:
                        if 'video_url' in item['node']:
                            links.append(item['node']['video_url'])
                        else:
                            links.append(item['node']['display_url'])

                else:
                    if 'video_url' in result:
                        links.append(result['video_url'])

                    else:
                        links.append(result['display_url'])

                preview = []
                for link in links:
                    try:
                        url = requests.get(
                            url=f'https://getcdnlink.xyz/api/getcdn?url={link}')
                        pre_link = url.json()['pre_url']
                    except Exception as e:
                        error_log(f'cdn_failed,{e},{url}')
                        preview.append('No Preview Found')
                    else:
                        preview.append(pre_link)
                return ({
                    'links': links,
                    'preview': preview
                })
        else:
            links = []

            if 'carousel_media' in result:
                for item in result['carousel_media']:
                    if 'video_versions' in item:
                        links.append(item['video_versions'][0]['url'])
                    else:
                        links.append(item['image_versions2']
                                     ['candidates'][0]['url'])

            else:
                if 'video_versions' in result:
                    links.append(result['video_versions'][0]['url'])

                else:
                    links.append(result['image_versions2']
                                 ['candidates'][0]['url'])

            preview = []
            for link in links:
                try:
                    url = requests.get(
                        url=f'https://getcdnlink.xyz/api/getcdn?url={link}')
                    pre_link = url.json()['pre_url']
                except Exception as e:
                    error_log(f'cdn_failed,{e},{url}')
                    preview.append('No Preview Found')
                else:
                    preview.append(pre_link)
            return ({
                'links': links,
                'preview': preview
            })

    except Exception as e:
        error_log(f'fully_failed,{e},{url}')
        return ({
            'error': 'No Media Found!'
        })


def story(url: str) -> dict:
    try:
        match = re.search(r'stories\/([^\/]+)', url)
        username = match.group(1)
        id_url = f'https://www.instagram.com/{username}/?__a=1'
        data = requests.get(url=id_url, headers=headers)
        fetch = data.json()
        user_id = fetch['graphql']['user']['id']
    except Exception as e:
        error_log(f'fully_failed,{e},{url}')
        return ({
            'error': 'No Media Found!'
        })
    else:
        try:
            user_id = int(user_id)
            story_link = f'https://i.instagram.com/api/v1/feed/user/{user_id}/story/'
            stories = requests.get(url=story_link, headers=headers)
            links = stories.json()['reel']['items']
        except Exception as e:
            error_log(f'trying,{e},{url}')
            return ({
                'error': 'No Stories Found!'
            })
        else:
            tray = []

            for link in links:
                if 'video_versions' in link:
                    tray.append(link['video_versions'][0]['url'])
                else:
                    tray.append(link['image_versions2']
                                ['candidates'][0]['url'])

            preview = []

            for link in tray:
                try:
                    url = requests.get(
                        url=f'https://getcdnlink.xyz/api/getcdn?url={link}')
                    pre_link = url.json()['pre_url']
                except Exception as e:
                    error_log(f'cdn_failed,{e},{url}')
                    preview.append('No Preview Found!')
                else:
                    preview.append(pre_link)

            return ({
                'links': tray,
                'preview': preview
            })


def highlights(url: str) -> dict:
    try:
        try:
            match = re.search(
                pattern=r'stories\/highlights\/([^\/]+)', string=url)
            hg_id = int(match.group(1))
        except Exception as e:
            error_log(f'trying,{e},{url}')
            original_url = requests.get(url=url, headers=headers).url
            match = re.search(
                pattern=r'stories\/highlights\/([^\/]+)', string=original_url)
            hg_id = int(match.group(1))
        finally:
            hglink = f'https://i.instagram.com/api/v1/feed/reels_media/?reel_ids=highlight%3A{hg_id}'
            data = requests.get(url=hglink, headers=headers)
            hg_key = f'highlight:{hg_id}'
            result = data.json()['reels'][hg_key]['items']
    except Exception as e:
        error_log(f'fully_failed,{e},{url}')
        return ({
            'error': 'No Media Found!'
        })
    else:
        tray = []

        for item in result:
            if 'video_versions' in item:
                tray.append(item['video_versions'][0]['url'])
            else:
                tray.append(item['image_versions2']['candidates'][0]['url'])

        preview = []
        for link in tray:
            try:
                url = requests.get(
                    url=f'https://getcdnlink.xyz/api/getcdn?url={link}')
                pre_link = url.json()['pre_url']
            except Exception as e:
                error_log(f'cdn_failed,{e},{url}')
                preview.append('No Preview Found')
            else:
                preview.append(pre_link)
        return ({
            'links': tray,
            'preview': preview
        })


def profile(url: str) -> dict:
    try:
        patt = r'https\:\/\/.*instagram\.com\/([^\/\?]+)'
        match = re.search(pattern=patt, string=url)
        find = match.group(0)
        profile_link = f'{find}/?__a=1'
        data = requests.get(url=profile_link, headers=headers)
        result = data.json()['graphql']['user']
    except Exception as e:
        error_log(f'fully_failed,{e},{url}')
        return ({
            'error': 'No Media Found!'
        })
    else:

        tray = {
            'full_name': result['full_name'],
            'biography': result['biography'],
            'profile_url': result['profile_pic_url_hd']
        }

        link = tray['profile_url']
        try:
            preview_url = requests.get(
                url=f'https://getcdnlink.xyz/api/getcdn?url={link}').json()['pre_url']
        except Exception as e:
            error_log(f'trying,{e},{url}')
            preview_url = 'No Media Found'

        return ({
            'links': tray,
            'preview': preview_url
        })


def yt_thumbnail(yt_id: str) -> dict:
    try:
        preview = []
        resolutions = ['maxresdefault', 'sddefault',
                       'hqdefault', 'mqdefault', 'default']
        actual_resolutions = ['Full HD', 'HD', 'Medium', 'SD', 'Low']

        for item in resolutions:
            try:
                pre_url = f'https://i.ytimg.com/vi/{yt_id}/{item}.jpg'
                cdn_url = requests.get(
                    url=f'https://getcdnlink.xyz/api/getcdn?url={pre_url}').json()['pre_url']

                preview.append(cdn_url)
            except Exception as e:
                error_log(f'cdn_failed,{e},{yt_id}')
                cdn_url = 'No Media Found!'
                preview.append(cdn_url)

        return ({
            'preview': preview,
            'resolutions': actual_resolutions
        })

    except Exception as e:
        error_log(f'fully_failed,{e},{yt_id}')
        return ({
            'error': 'No Media Found!'
        })


def youtube_tags(yt_id: str) -> dict:
    try:
        url = 'https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
        data = requests.post(url=url, headers=yt_headers(
            id), data=yt_payload(yt_id)).json()
        results = data['videoDetails']['keywords']
        return ({
            'tags': results
        })

    except Exception as e:
        error_log(f'fully_failed,{e},{yt_id}')
        return ({
            'error': 'No Media Found!'
        })


def tw_video(tw_user: str, tw_id: int) -> dict:
    try:
        tray = []
        url = f'https://twitter.com/i/api/graphql/MwoNOssr8CR7CxUWbBQO9w/TweetDetail?variables=%7B%22focalTweetId%22%3A%22{tw_id}%22%2C%22with_rux_injections%22%3Atrue%2C%22includePromotedContent%22%3Atrue%2C%22withCommunity%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withTweetQuoteCount%22%3Atrue%2C%22withBirdwatchNotes%22%3Afalse%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withBirdwatchPivots%22%3Afalse%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Afalse%7D'
        tw_media = requests.get(url=url, headers=tw_headers).json()
        results = tw_media['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][
            0]['content']['itemContent']['tweet_results']['result']
        user = ''
        to_load = {}

        try:
            to_load = tw_media['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][
                1]['content']['itemContent']['tweet_results']['result']
            user = to_load['legacy']['in_reply_to_screen_name']
            try:
                to_reply = to_load['core']['user_results']['result']['legacy']['screen_name']
                if tw_user != to_reply:
                    to_load = tw_media['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][
                        2]['content']['itemContent']['tweet_results']['result']
                else:
                    pass
            except Exception as e:
                error_log(f'trying,{e},{tw_id}')
                pass

        except Exception as e:
            error_log(f'trying,{e},{tw_id}')
            to_load = tw_media['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][1][
                'content']['items'][0]['item']['itemContent']['tweet_results']['result']
            user = to_load['legacy']['in_reply_to_screen_name']

        if user == tw_user:
            try:
                total = results['legacy']['extended_entities']['media']
            except Exception as e:
                error_log(f'trying,{e},{tw_id}')
                try:
                    total = results['quoted_status_result']['result']['legacy']['extended_entities']['media']
                except Exception as e:
                    error_log(f'trying,{e},{tw_id}')
                    total = results['card']['legacy']['binding_values']
                    for item in total:
                        if item['key'] == 'thumbnail_image_original':
                            tray.append(item['value']['image_value']['url'])
                            break
                    return ({
                        'links': tray
                    })

        else:
            try:
                total = to_load['legacy']['extended_entities']['media']
            except Exception as e:
                error_log(f'trying,{e},{tw_id}')
                total = to_load['quoted_status_result']['result']['legacy']['extended_entities']['media']

        for item in total:
            if 'video_info' in item:
                l = item['video_info']['variants']
                b = [x['bitrate'] for x in l if 'bitrate' in x]
                q = [x['url'] for x in l if 'bitrate' in x]
                key = b.index(max(b))
                video_url = q[key]
                tray.append(video_url)
            else:
                image_url = item['media_url_https']
                tray.append(image_url)

        return ({
            'links': tray
        })
    except Exception as e:
        error_log(f'fully_failed,{e},{tw_id}')
        return ({
            'error': 'No Media Found!'
        })
