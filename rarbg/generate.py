import requests,os

def get_latest(rss_url):
    response = requests.get(rss_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"})
    print(response.text)
    return response.text

filename = f'./rarbg/episode.xml'
if os.path.exists(filename):
    os.remove(filename)

rss_url="https://proxyrarbg.org/rssdd.php?categories=44;50;51;52;42;46;54"

try:
    with open(filename, 'w') as f:
        f.write(get_latest(rss_url))
except:
    print('rarbg rss download failed.')
