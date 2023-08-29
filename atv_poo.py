# 1.

# class Bola:
#     def __init__(self, cor, circ, material):
#         self.cor = cor
#         self.circ = circ
#         self.material = material

#     def trocaCor(self, nova_cor):
#         self.cor = nova_cor

#     def mostrarCor(self):
#         return self.cor


# nova_bola = Bola(cor="vermelho", circ=25, material="borracha")
# print("Cor atual:", nova_bola.mostrarCor()) 

# nova_bola.trocaCor("azul")
# print("Cor após troca:", nova_bola.mostrarCor())


# _________________________________________________________________________

# 2.


# class Quadrado:
#     def __init__(self, tamanho_lado):
#         self.tamanho_lado = tamanho_lado

#     def mudarLado(self, novo_lado):
#         self.tamanho_lado = novo_lado

#     def retornarLado(self):
#         return self.tamanho_lado

#     def calcularArea(self):
#         return self.tamanho_lado ** 2


# novo_quadrado = Quadrado(tamanho_lado=5)
# print("Lado:", novo_quadrado .retornarLado()) 
# print("Área:", novo_quadrado .calcularArea())

# novo_quadrado.mudarLado(7)
# print("Novo lado:", novo_quadrado.retornarLado())  
# print("Nova área:", novo_quadrado.calcularArea())


# _________________________________________________________________________

# 3.

# class Retangulo:
#     def __init__(self, lado_a, lado_b):
#         self.lado_a = lado_a
#         self.lado_b = lado_b

#     def mudarLados(self, novo_lado_a, novo_lado_b):
#         self.lado_a = novo_lado_a
#         self.lado_b = novo_lado_b

#     def retornarLados(self):
#         return self.lado_a, self.lado_b

#     def calcularArea(self):
#         return self.lado_a * self.lado_b

#     def calcularPerimetro(self):
#         return 2 * (self.lado_a + self.lado_b)


# def main():
#     lado_a = float(input("Informe o comprimento do retângulo: "))
#     lado_b = float(input("Informe a largura do retângulo: "))

#     meu_retangulo = Retangulo(lado_a, lado_b)

#     area = meu_retangulo.calcularArea()
#     perimetro = meu_retangulo.calcularPerimetro()

#     print(f"Área do retângulo: {area}")
#     print(f"Perímetro do retângulo: {perimetro}")

#     tamanho_piso = float(input("Informe o tamanho do piso: "))
#     tamanho_rodape = float(input("Informe o tamanho do rodapé: "))

#     area_piso = tamanho_piso ** 2
#     area_rodape = tamanho_rodape * 2 * (lado_a + lado_b)

#     quantidade_pisos = area / area_piso
#     quantidade_rodapes = perimetro / tamanho_rodape

#     print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
#     print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.2f}")

# if __name__ == "__main__":
#     main()


# _________________________________________________________________________

# 4.
# class Pessoa:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura

#     def envelhecer(self, anos):
#         self.idade += anos
#         if self.idade < 21:
#             self.altura += 0.5 * anos

#     def engordar(self, peso_ganho):
#         self.peso += peso_ganho

#     def emagrecer(self, peso_perdido):
#         self.peso -= peso_perdido

#     def crescer(self, altura_ganha):
#         self.altura += altura_ganha

#     def mostrarInformacoes(self):
#         print(f"Nome: {self.nome}")
#         print(f"Idade: {self.idade} anos")
#         print(f"Peso: {self.peso} kg")
#         print(f"Altura: {self.altura:.2f} metros")


# pessoa = Pessoa(nome="andre", idade=18, peso=70, altura=1.65)
# pessoa.mostrarInformacoes()

# pessoa.envelhecer(3)
# pessoa.engordar(5)
# pessoa.crescer(0.1)
# pessoa.mostrarInformacoes()


# _________________________________________________________________________

# 5.

# class ContaCorrente:
#     def __init__(self, numero_conta, nome, saldo=0):
#         self.numero_conta = numero_conta
#         self.nome = nome
#         self.saldo = saldo

#     def alterarNome(self, novo_nome):
#         self.nome = novo_nome

#     def deposito(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
#         else:
#             print("O valor do depósito deve ser positivo.")

#     def saque(self, valor):
#         if valor > 0 and valor <= self.saldo:
#             self.saldo -= valor
#             print(f"Saque de R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")
#         elif valor <= 0:
#             print("O valor do saque deve ser positivo.")
#         else:
#             print("Saldo insuficiente para o saque.")

#     def mostrarInformacoes(self):
#         print(f"Número da Conta: {self.numero_conta}")
#         print(f"Nome do Correntista: {self.nome}")
#         print(f"Saldo: R${self.saldo:.2f}")


# conta = ContaCorrente(numero_conta="12345", nome="Paula")
# conta.mostrarInformacoes()

# conta.deposito(500)
# conta.saque(200)
# conta.alterarNome("Ana Paula Souza")
# conta.mostrarInformacoes()


# _________________________________________________________________________
# 6.
# class TV:
#     def __init__(self):
#         self.canal = 1
#         self.volume = 10

#     def alterar_canal(self, novo_canal):
#         if 1 <= novo_canal <= 100:
#             self.canal = novo_canal
#             print(f"Canal alterado para {self.canal}")

#     def aumentar_volume(self):
#         if self.volume < 100:
#             self.volume += 1
#             print(f"Volume aumentado para {self.volume}")

#     def diminuir_volume(self):
#         if self.volume > 0:
#             self.volume -= 1
#             print(f"Volume diminuído para {self.volume}")

#     def mostrar_informacoes(self):
#         print(f"Canal: {self.canal}")
#         print(f"Volume: {self.volume}")


# tv = TV()
# tv.mostrar_informacoes()

# tv.aumentar_volume()
# tv.diminuir_volume()
# tv.alterar_canal(5)
# tv.mostrar_informacoes()

# _________________________________________________________________________
# 7.
# class BichinhoVirtual:
#     def __init__(self, nome):
#         self.nome = nome
#         self.fome = 50
#         self.saude = 50
#         self.idade = 1

#     def alterar_nome(self, novo_nome):
#         self.nome = novo_nome

#     def alterar_fome(self, nova_fome):
#         self.fome = nova_fome

#     def alterar_saude(self, nova_saude):
#         self.saude = nova_saude

#     def alterar_idade(self, nova_idade):
#         self.idade = nova_idade

#     def retornar_nome(self):
#         return self.nome

#     def retornar_fome(self):
#         return self.fome

#     def retornar_saude(self):
#         return self.saude

#     def retornar_idade(self):
#         return self.idade

#     def calcular_humor(self):
#         humor = (self.fome + self.saude) / 2
#         return humor

# bichinho = BichinhoVirtual(nome="Fofinho")
# print("Humor:", bichinho.calcular_humor())  

# bichinho.alterar_fome(70)
# bichinho.alterar_saude(30)
# print("Novo humor:", bichinho.calcular_humor())  

# bichinho.alterar_nome("Fofura")
# print("Nome:", bichinho.retornar_nome())  

# _________________________________________________________________________
# 8.
# class Macaco:
#     def __init__(self, nome):
#         self.nome = nome
#         self.bucho = []

#     def comer(self, alimento):
#         self.bucho.append(alimento)

#     def ver_bucho(self):
#         print(f"Conteúdo do bucho de {self.nome}: {self.bucho}")

#     def digerir(self):
#         if self.bucho:
#             print(f"{self.nome} está digerindo...")
#             self.bucho = []
#         else:
#             print(f"{self.nome} não tem nada no bucho para digerir.")


# macaco1 = Macaco(nome="Bobby")
# macaco2 = Macaco(nome="Lulu")

# macaco1.comer("Banana")
# macaco1.comer("Maçã")
# macaco2.comer("Nozes")

# macaco1.ver_bucho() 
# macaco2.ver_bucho() 

# macaco1.digerir()
# macaco1.ver_bucho()  

# _________________________________________________________________________
# 9.
# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def mostrar(self):
#         print(f"Ponto: ({self.x}, {self.y})")

# class Retangulo:
#     def __init__(self, largura, altura, ponto_inicial):
#         self.largura = largura
#         self.altura = altura
#         self.ponto_inicial = ponto_inicial

#     def encontrar_centro(self):
#         centro_x = self.ponto_inicial.x + self.largura / 2
#         centro_y = self.ponto_inicial.y + self.altura / 2
#         return Ponto(centro_x, centro_y)

# # Exemplo de uso da classe Ponto e Retangulo
# ponto = Ponto(2, 3)
# ponto.mostrar()

# retangulo = Retangulo(largura=5, altura=4, ponto_inicial=ponto)
# centro = retangulo.encontrar_centro()
# centro.mostrar()  # Saída: Ponto: (4.5, 5.5)

# _________________________________________________________________________
# 10.

# class BombaCombustivel:
#     def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
#         self.tipo_combustivel = tipo_combustivel
#         self.valor_litro = valor_litro
#         self.quantidade_combustivel = quantidade_combustivel

#     def abastecer_por_valor(self, valor):
#         litros_abastecidos = valor / self.valor_litro
#         if litros_abastecidos <= self.quantidade_combustivel:
#             self.quantidade_combustivel -= litros_abastecidos
#             print(f"Abastecidos {litros_abastecidos:.2f} litros. Saldo: {self.quantidade_combustivel:.2f} litros")
#         else:
#             print("Quantidade de combustível insuficiente.")

#     def abastecer_por_litro(self, litros):
#         valor_pago = litros * self.valor_litro
#         if litros <= self.quantidade_combustivel:
#             self.quantidade_combustivel -= litros
#             print(f"Abastecidos {litros:.2f} litros. Valor: R${valor_pago:.2f}")
#         else:
#             print("Quantidade de combustível insuficiente.")

#     def alterar_valor(self, novo_valor):
#         self.valor_litro = novo_valor

#     def alterar_combustivel(self, novo_combustivel):
#         self.tipo_combustivel = novo_combustivel

#     def alterar_quantidade_combustivel(self, nova_quantidade):
#         self.quantidade_combustivel = nova_quantidade

# # Exemplo de uso da classe BombaCombustivel
# bomba = BombaCombustivel(tipo_combustivel="Gasolina", valor_litro=5
