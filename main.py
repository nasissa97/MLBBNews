from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

soup = ''
today = date.today()
prev_day = today - timedelta(days=1)
prev_day = str(prev_day)
print(today)
print(prev_day)
url = "https://www.mlb.com/scores/" + prev_day
print(url)

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Error")
results = soup.find_all("div", {"class": "sc-fznBtT djSojJ"})
unique_games = set()
for game in results:
    teams = game.find_all("div",
                          {"class":
                           "TeamWrappersstyle" +
                           "__DesktopTeamWrapper-uqs6qh-0 hkpegb"})
    for team in teams:
        unique_games.add(team.text)

count_games = 0

for x in unique_games:
    if count_games >= 2:
        print()
        count_games = 0
    print(f'{x:20}', end='')
    count_games += 1
