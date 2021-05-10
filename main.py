from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

games_of_the_day = []


def getURL() -> str:
    """ sets up the html request and """
    today = date.today()
    prev_day = today - timedelta(days=1)
    prev_day = str(prev_day)
    url = "https://www.mlb.com/scores/" + prev_day
    return url


def getPayLoad(url: str) -> object:
    soup = ''
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print("Error")
    results = soup.find_all("div", {"class": "sc-fznBtT djSojJ"})
    return results


def getGames(payload: object):
    print(type(payload))
    """ getGame() passes in all the single game divs, to then extract
    the team names,the scores, and stores them in a temporary list
    which will append to the module level list 'games_of_the_day' """
    global games_of_the_day
    for game in payload:
        teams = game.find_all("div",
                              {"class":
                               "TeamWrappersstyle" +
                               "__DesktopTeamWrapper-uqs6qh-0 hkpegb"})

        scores = game.find_all("table", {"class": "sc-fzoJMP kKCmVs"})

        away_team = teams[0].text
        home_team = teams[1].text
        away_score, home_score = getScores(scores)
        game_content = [away_team, away_score, home_team, home_score]
        games_of_the_day.append(game_content)


def getScores(payload: object) -> object:
    """ getScores() returns the score for both away team and home team """
    for score in payload:
        away_score = score.find("div", {"class": "sc-fzpisO kIavKi"})
        home_score = score.find("div", {"class": "sc-fzpisO gezsIM"})
        away_score_text = away_score.text
        home_score_text = home_score.text
        return [away_score_text, home_score_text]


def printGames():
    for game in games_of_the_day:
        game_print = ' '.join(i for i in game)
        print(game_print)
        if game[1] > game[3]:
            print(f"{game[0]} Won")
        else:
            print(f"{game[2]} Won")
        print()


def main():
    mlbURL = getURL()
    data = getPayLoad(mlbURL)
    getGames(data)
    printGames()


if __name__ == "__main__":
    main()
