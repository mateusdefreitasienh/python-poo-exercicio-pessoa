class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    def apresentar_dados(self):
        print(f"{self.nome} | {self.idade} | {self.altura}")