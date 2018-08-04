from bs4 import BeautifulSoup as bs
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0'}

song_name = input("ENTER NAME OF SONG:")
website_list = {0:'musixmatch',1:'a-z'}

print("---CHOOSE WEBSITE FOR FETCHING LYRICS---")
for keys in website_list:
	print(keys,":", website_list[keys])

website_choice = input('Choice:') or '0'
website_choice = int(website_choice)

try:
	print('FETCHING FROM ',website_list[website_choice])
except:
	print('INVALID CHOICE')

### MUSIXMATCH

def musixmatch(song_name='not afraid'):
	home = 'https://www.musixmatch.com'
	search = home +'/search/'+song_name.replace(" ", "%20")
	# print(search)
	home_page = requests.get(search,headers=headers)
	home_content = home_page.content
	soup = bs(home_content, 'html.parser')
	
	# print(soup.title)
	# best_result = soup.find('div class ="box-content"')
	best_result = soup.select_one('a.title')
	# print('best result', best_result)
	# print(best_result.text)
	lyrics_search = home + best_result.get('href')
	print("Lyrics For: "best_result.text)
	lyrics_page = requests.get(lyrics_search,headers=headers)
	lyrics_content = lyrics_page.content
	lsoup = bs(lyrics_content,'html.parser')
	paragraph_list = lsoup.select('p.mxm-lyrics__content')
	print('---- START -------')
	for i in paragraph_list:
		# print('^^^^^')
		print(i.text)
		# print('|||||||')
	print('xxxxxx END xxxxx')

	# print(lsoup.title)
	# time.sleep(2)
	# # lyrics_div_list = lsoup.select_one('div.mxm-track-lyrics-container')
	# # print(lyrics_div_list)
	# # lyrics_div = lyrics_div_list[1]

	# # print(lyrics_div)
	# # print('---')
	# try:
	# 	print('****************')
	# 	print(lyrics_div_list.text)
	# 	print('************')
	# except:
	# 	print('FAIL! .text not working')

	# print('$$$$$$$')
	# main_lyrics_div = lsoup.select_one('div.mxm-track-lyrics-container > div > div')
	# print(main_lyrics_div)
	# print('$$$$$$')

	# print('+++++++')

	# print(main_lyrics_div.text)

	# print('++++++')


musixmatch(song_name)
# musixmatch()




