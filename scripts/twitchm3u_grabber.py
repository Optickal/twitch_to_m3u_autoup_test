from daytime import daytime
import requests
import is
import sys

@app.route(f'/playlist.m3u')
def playlistgenerator():
    playlist = '#EXTM3U\n'
    with open('streams.txt', 'r') as streams:
        for stream in streams:
            stream = stream.strip()
            if not stream:
                continue
            playlist += f'#EXTINF:-1 group-title="twitch", {stream}\n'
            playlist += f'http:///twitch.tv/?streamer={stream}\n'

    return playlist


@app.route(f'/twitch')
def getm3u():
    streamer = request.args.get('streamer')
    url = 'https://pwn.sh/tools/streamapi.py?url=twitch.tv/'
    try:
        response = requests.get(f'{url}{streamer}').json()
        links = response['urls']
        qualities = {int(key.replace('p','')) : key for key in links.keys() if key != 'audio_only'}

        m3u = ''
        for quality in sorted(qualities.keys(), reverse=True):
            m3u = m3u + links[qualities[quality]] + '\n'
                
    except:
        m3u = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
    
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('"720p60": "https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://telerising.de/epg/easyepg-basic.gz"')
print(banner)
#s = requests.Session()
with open('../streams.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
