from Toolkit import Toolkit
from TrackerGGEntry import TrackerGGEntry

class TrackerGG:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = ["pseudo","lp","wr", "kp", "gm", "vm", "champ1", "champ2", "champ3"]


    def setPageMax(self, pageMax):
        self.nbPage = pageMax + 1
        return self
    

    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls


    def setEndpoints(self, soup):
        #ATTENTION, la suite de cette fonction ne marche que pour mon site, c'est un exemple
        #l'exercice etant de refaire une fonction pour VOTRE site a scraper
        links = []
        tbody = soup.find("tbody")
        for player in tbody:

            rankStat = soup.find("td",{"class": "stat highlight"})
            currentRank = rankStat.find("div").text

            a = player.find('a')
            try: 
                links.append(a['href'])
            except:
                pass

        self.endpoints.extend(Toolkit.addBaseUrl(self.baseUrl, links))
        print("Endpoints Done")
        return self.endpoints


    def getEndpoints(self):
        return self.endpoints


    def getFinalFieldNames(self):
        return self.finalFileNameFields
        

    def getInfoByPage(self, soup):
        fiches = []
        try:
            pseudo = Toolkit.tryToCleanOrReturnBlank(soup.find("span",{"class": "trn-ign__username"}))
            lp = Toolkit.tryToCleanOrReturnBlank(soup.find("span",{"class": "stat__value"}))
            performance = soup.find("div",{"class": "performance-score__stats"})
            performanceId = 0
        
            for elements in performance:
                if performanceId == 0:
                    wr = Toolkit.tryToCleanOrReturnBlank(elements.find("div",{"class": "stat__value"}))
                if performanceId == 1:
                    kp = Toolkit.tryToCleanOrReturnBlank(elements.find("div",{"class": "stat__value"}))
                if performanceId == 2:
                    gm = Toolkit.tryToCleanOrReturnBlank(elements.find("div",{"class": "stat__value"}))
                if performanceId == 3:
                    vm = Toolkit.tryToCleanOrReturnBlank(elements.find("div",{"class": "stat__value"}))
                performanceId += 1
            championList = soup.find("div",{"class": "champions__list"})
            championListId = 0
            for champion in championList:
                if championListId == 0:
                    champ1 = Toolkit.tryToCleanOrReturnBlank(champion.find("div",{"class": "name"}))
                if championListId == 1:
                    champ2 = Toolkit.tryToCleanOrReturnBlank(champion.find("div",{"class": "name"}))
                if championListId == 2:
                    champ3 = Toolkit.tryToCleanOrReturnBlank(champion.find("div",{"class": "name"}))
                championListId += 1
        except:
            pseudo = ""
            lp = ""
            wr = ""
            kp = ""
            gm = ""
            vm = ""
            champ1 = ""
            champ2 = ""
            champ3 = ""


        fiche = TrackerGGEntry(pseudo, lp, wr, kp, gm, vm, champ1, champ2, champ3)
        fiches.append(fiche)
        self.result.extend(fiches)
        return fiches


    def getResult(self):
        return self.result


    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result