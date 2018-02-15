import json
import Model
import wxPython

# lato = int(input("inserisci un numero: "))
# area = lato * 4
# circ = lato ** 2
# m = "L'area è {}, il quadrato del numero è {}.".format(area, circ)
# print(m)
from Model import cf

nome = 'davide'  # input("inserisci il tuo nome")
cognome = 'grimaldi'  # input("inserisci il tuo cognome")
giornoS = '27'  # input("inserisci il giorno")
msS = '02'  # input("inserire il numero del mese")
anno = '92'  # input("inserire ultime due cifre anno")
comune = 'cerignola'  # input("inserisci comune")

momma = cf.getNome()


def toInt(x):  # quando chiamo questa fun. char in intero con try
    try:
        s = int(x)
    except:
        exit("lascia questa valle di lacrime")
    finally:
        return s


giorno = toInt(giornoS)
mese = toInt(msS)

listaN = []
m = int(len(nome))
for n in range(m):
    if (nome[n] == 'a') or (nome[n] == 'e') or (nome[n] == 'i') or (nome[n] == 'o') or (nome[n] == 'u'):
        print(n)
    elif int(len(listaN)) == 3:
        break
    else:
        listaN.extend(nome[n].upper())

listaG = []
s = int(len(cognome))
for n in range(s):
    if (cognome[n] == 'a') or (cognome[n] == 'e') or (cognome[n] == 'i') or (cognome[n] == 'o') or (cognome[n] == 'u'):
        print(n)
    elif int(len(listaG)) == 3:
        break
    else:
        listaG.extend(cognome[n].upper())

mesiA = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'T']


def importJson(filePath):
    f = open(filePath, 'r')
    with f:
        data = json.load(f)
        f.closed
        return data


def corCom(comune):
    diz = importJson('comuni.json')
    s = int(len(diz))
    dM = comune.replace(comune[0], comune[0].upper())
    for n in range(s):
        if dM == diz[n]['nome']:
            return diz[n]['codiceCatastale']


CIN_pari = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            "A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7", "I": "8",
            "J": "9", "K": "10", "L": "11", "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16",
            "R": "17", "S": "18", "T": "19", "U": "20", "V": "21", "W": "22", "X": "23", "Y": "24",
            "Z": "25"
            }
CIN_dispari = {"0": "1", "1": "0", "2": "5", "3": "7", "4": "9", "5": "13", "6": "15", "7": "17", "8": "19", "9": "21",
               "A": "1", "B": "0", "C": "5", "D": "7", "E": "9", "F": "13", "G": "15", "H": "17", "I": "19",
               "J": "21", "K": "2", "L": "4", "M": "18", "N": "20", "O": "11", "P": "3", "Q": "6",
               "R": "8", "S": "12", "T": "14", "U": "16", "V": "10", "W": "22", "X": "25", "Y": "24", "Z": "23"
               }

d = [listaG[0], listaG[1], listaG[2], listaN[0], listaN[1], listaN[2],
     anno[0], anno[1], mesiA[mese - 1], giornoS[0], giornoS[1],
     corCom(comune)[0], corCom(comune)[1], corCom(comune)[2], corCom(comune)[3]]
lun = int(len(d))

S1 = 0
S2 = 0
for n in range(lun):
    if n % 2 == 0:
        S1 = S1 + int(CIN_dispari[d[n]])
    else:
        S2 = S2 + int(CIN_pari[d[n]])

R = (S1 + S2) % 26
final_CIN = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F",
             "6": "G", "7": "H", "8": "I", "9": "J", "10": "K",
             "11": "L", "12": "M", "13": "N", "14": "O", "15": "P",
             "16": "Q", "17": "R", "18": "S", "19": "T", "20": "U",
             "21": "V", "22": "K", "23": "Y", "24": "W", "25": "Z"}

print('{}{}{}{}{}{}{}{}{}{}{}'.format(listaG[0], listaG[1], listaG[2],
                                      listaN[0], listaN[1], listaN[2], anno, mesiA[mese - 1], giorno,
                                      corCom(comune), final_CIN[str(R)]))
