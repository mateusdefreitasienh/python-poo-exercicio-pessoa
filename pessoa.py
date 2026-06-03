from utils import *

class Pessoa:
    def __init__(self):
        self.nome = input_nome("Digite o nome: ")
        self.idade = input_int("Digite a idade: ", 0, 150)
        self.altura = input_float("Digite sua altura [m]: " , 0.0, 3.00)
        
    def apresentar_dados(self):
        print(f"{self.nome} | {self.idade} | {self.altura}")