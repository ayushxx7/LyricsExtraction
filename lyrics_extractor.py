import requests
from bs4 import BeautifulSoup as bs

def fetch_lyrics(song_name='not afraid'):
    """Fetch lyrics from MusixMatch

    Parameters
    ----------
    song_name: str
        The song to searched on MusixMatch
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    home = 'https://www.musixmatch.com'
    search = home+'/search/'+song_name.replace(" ", "%20")

    home_page = requests.get(search, headers=headers)
    home_content = home_page.content
    soup = bs(home_content, 'html.parser')

    best_result = soup.select_one('a.title')
    print(f"Lyrics For: {best_result.text}")

    lyrics_search = home + best_result.get('href')
    lyrics_page = requests.get(lyrics_search, headers=headers)
    lyrics_content = lyrics_page.content
    lsoup = bs(lyrics_content,'html.parser')
    paragraph_list = lsoup.select('p.mxm-lyrics__content')

    print('---- START -------')
    for para in paragraph_list:
        print(para.text)
    print('xxxxxx END xxxxx')

if __name__ == "__main__":
    song_name = input("ENTER NAME OF SONG:")
    print('FETCHING FROM MusixMatch')
    fetch_lyrics(song_name)
