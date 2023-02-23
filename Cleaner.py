import pandas as pd
import numpy as np
import re

class Cleaner:
    def __init__(self, path):
        data = pd.read_csv(path)
        Cleaner.text = data

    def CategVerif(self):
        return Cleaner.text.isnull().sum()

    def LineVerif(self, categ):
        return Cleaner.text.loc[Cleaner.text[categ].isnull(), :]

    def MissingCateg(self, categ, nameToPut):
        Cleaner.text.loc[Cleaner.text[categ].isnull(), categ] = nameToPut

    def DuplicateDel(self, categList):
        """categList like ["date_operation", "libelle", "montant", "solde_avt_ope", "categ"]"""
        Cleaner.text.drop_duplicates(subset=categList, inplace=True, ignore_index=True)

    def DuplicateVerif(self, categList):
        """categList like ["date_operation", "libelle", "montant", "solde_avt_ope", "categ"]"""
        return Cleaner.text.loc[Cleaner.text[categList].duplicated(keep=False),:]

    def VerifDate(self):
        print(Cleaner.text.dtypes)

    def ConvertDate(self, categ):
        Cleaner.text[categ] = pd.to_datetime(Cleaner.text[categ])

    def SaveData(self, name):
        Cleaner.text.to_csv(name, index=False)

    def nullValues(self):
        Cleaner.text.dropna(inplace=True)