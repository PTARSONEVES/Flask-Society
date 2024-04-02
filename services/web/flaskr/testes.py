import numpy as np
from array import *
#from .database import db

bolas_str = []
bolas_num = []
bolas_qtd = []
def geraBolas(numbolas,qtd):
    for bola in range(numbolas+1):
        bolas_num.append(bola)
        bolas_qtd.append(qtd)
        numero=str(bola)
        if len(numero)==1:
            numero='0'+numero
        bolas_str.append(numero)
    pass
numbolas=25
qtd=0
geraBolas(numbolas,qtd)
for bola in bolas_num:
    frase='Bola '+str(bolas_num[bola])+": "+bolas_str[bola]+"("+str(bolas_qtd[bola])+" vez(es))"
    print(frase)
