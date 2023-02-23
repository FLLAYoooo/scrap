import requests 
from bs4 import BeautifulSoup 
from Toolkit import Toolkit
import time

class Scraper:
    def __init__(self, ScrapInstance, linkFile, finalFile):
        self.setScrapInstance(ScrapInstance)
        self.setFinalFile(finalFile)
        self.setLinkFile(linkFile)
        self.finalFileNameFields = self.ScrapInstance.getFinalFieldNames()
        self.linkFileNameFields = ['link']

    def setScrapInstance(self, instance):
        self.ScrapInstance = instance
        return self

    def setLinkFile(self, filePath):
        self.linkFile = filePath
        return self

    def setFinalFile(self, filePath):
        self.finalFile = filePath
        return self

    def swoup(self, url, process):
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            return process(soup)
        else:
            print("ERROR: Failed Connect on :" + str(url))
            return False

    def swoupMultiple(self, urls, process):
        result = []
        MAX = 0
        for url in urls:
            if MAX < 1000:
                soup = self.swoup(url, process)
                if hasattr(soup, '__len__'):
                    result.extend(soup)
                else: 
                    result.append(soup)
                time.sleep(5)
                MAX += 1
                print(MAX)
        return result

    def exec(self):
        self.swoupMultiple(self.ScrapInstance.getLinks(), self.ScrapInstance.setEndpoints)
        rows= []
        for url in self.ScrapInstance.getEndpoints():
            row = {}
            row["link"] = url
            rows.append(row)
        Toolkit.fileWriter(self.linkFile, self.linkFileNameFields, rows)

        self.swoupMultiple(self.ScrapInstance.getEndpoints(), self.ScrapInstance.getInfoByPage)
        Toolkit.fileWriter(self.finalFile, self.finalFileNameFields, self.ScrapInstance.getDictResult())