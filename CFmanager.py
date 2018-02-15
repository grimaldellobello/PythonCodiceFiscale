from prova.View.Prova import importJson


class CFmanager:

    diz = importJson('cf.json')

    def addCodF(self,nome, cognome, giorno, mese, anno, comune):
        CF = CF("nome","cognome","giorno","mese","anno","comune")

