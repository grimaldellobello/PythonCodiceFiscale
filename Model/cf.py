class cf:
    def __init__(self,nome, cognome, giorno, mese, anno, comune):
        self._nome = nome
        self._cognome = cognome
        self._giorno = giorno
        self._mese = mese
        self._anno = anno
        self._comune = comune

    def getNome(self):
        return self._nome

    def getCognome(self):
        return self._cognome

    def getGiorno(self):
        return self._giorno

    def getMese(self):
        return self._mese

    def getAnno(self):
        return self._anno

    def getComune(self):
        return self._comune
