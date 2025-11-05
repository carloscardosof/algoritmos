#importando as funcoes de outro arquivo
import os
from funcoes import *

#print(entrada())

with open("dados/gastos.json", "r") as file:
    print(file.read())
