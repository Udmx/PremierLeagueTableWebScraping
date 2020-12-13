import requests
from bs4 import BeautifulSoup
from google_trans_new import google_translator

'''The Premier League table is crawled from the link below'''
URL = 'https://footba11.co/tournament/27/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86'

'''
    If you like, you can translate the names of the teams from this library into English
'''
# translator = google_translator()
# translate_text = translator.translate("نفت ابادان")
LIST_TEAMS = list()
LIST_PLAYING = list()
LIST_WIN = list()
LIST_DRAW = list()
LIST_LOSE = list()

result = requests.get(URL)
content = BeautifulSoup(result.text, 'html.parser')
# ------
content_list_team = content.find('div', class_='standings')
content_list_team = content_list_team.findAll('a')[3:]
for i in range(0, 16):
    LIST_TEAMS.append(content_list_team[i].text)
# ----------------------------------------------------
content_list_PLAYING = content.findAll('div', class_='flex-item standings-value played')
for i in range(1, 17):
    LIST_PLAYING.append(content_list_PLAYING[i].text)
# ------------------------------------------------------
content_list_WIN = content.findAll('div', class_='flex-item standings-value wins')
for i in range(1, 17):
    LIST_WIN.append(content_list_WIN[i].text)
# ---------------------------------------------
content_list_DRAW = content.findAll('div', class_='flex-item standings-value draws')
for i in range(1, 17):
    LIST_DRAW.append(content_list_DRAW[i].text)
# -----------------------------------------------
content_list_LOSE = content.findAll('div', class_='flex-item standings-value losses')
for i in range(1, 17):
    LIST_LOSE.append(content_list_LOSE[i].text)
# -----------------------------------------------
'''
    The following loop connects the values together
'''
for i in range(0, 16):
    result = ' {team_play}        Number of games:{number}  |  Number of' \
             ' wins:{win}  |  Draw number:{draw}  |  Number of losses:{lose}'.format(
        team_play=LIST_TEAMS[i], number=LIST_PLAYING[i], win=LIST_WIN[i], draw=LIST_DRAW[i], lose=LIST_LOSE[i])
    print(result)
