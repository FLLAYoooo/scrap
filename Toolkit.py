import csv

class Toolkit:
    def tryToCleanOrReturnBlank(str):
        try:
            result = str.getText().strip()
        except:
            result = ""
        return result

    def fileWriter(file,fieldnames, data):
        with open(file, 'w', encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    def addBaseUrl(baseUrl, urls):
        res = []
        for url in urls:
            res.append(baseUrl + url)
        return res