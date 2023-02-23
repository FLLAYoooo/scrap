class TrackerGGEntry:
    def __init__(self,pseudo,lp,wr, kp, gm, vm, champ1, champ2, champ3):
        
        self.pseudo = pseudo
        self.lp = lp
        self.wr = wr
        self.kp = kp
        self.gm = gm
        self.vm = vm
        self.champ1 = champ1
        self.champ2 = champ2
        self.champ3 = champ3
        
    def getDictEntry(self):
        return {
            "pseudo":self.pseudo,
            "lp":self.lp,
            "wr":self.wr,
            "kp":self.kp,
            "gm":self.gm,
            "vm":self.vm,
            "champ1":self.champ1,
            "champ2":self.champ2,
            "champ3":self.champ3
        }