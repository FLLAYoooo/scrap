# ensure you have Python (3  or latest)
# ensure you have pip installer

from Scraper import Scraper
from TrackerGG import TrackerGG
from Cleaner import Cleaner

# L'url du site que je souhaite Scraper

baseUrl = "https://tracker.gg"
uri = "/lol/leaderboards/stats/all/LeaguePoints?region=EUW&queueType=RANKED_SOLO_5x5&page="

TrackerGGInstance = TrackerGG(baseUrl, uri, 10)

scraper = Scraper(TrackerGGInstance, "linksList.csv", "infoss.csv")
scraper.exec()

clean = Cleaner("infoss.csv")
clean.DuplicateDel(["pseudo","lp","wr","kp","gm","vm","champ1","champ2","champ3"])
clean.nullValues()
clean.SaveData("infoss.csv")

print("Done")