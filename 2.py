import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados
@dataclass
class Familia:
    salario: float
    filhos: int

Quantidade_de_familias = 2

lista_de_familias = []

print("\n======= Solicitando Dados das Famílias =======")
for i in range(Quantidade_de_familias):
    familia = Familia(
        salario = float(input("Digite o salário da família: ")),
        filhos = int(input("Digite o número de filhos da família: "))
    )
    lista_de_familias.append(familia)

print("\n======= Exibindo Dados das Famílias =======")
for familia in lista_de_familias:
    print(f"Salário: R$ {familia.salario:.2f}")
    print(f"Número de Filhos: {familia.filhos}")

nome_do_arquivo = "Lista_de_familias.txt"

with open(nome_do_arquivo, "w") as arquivo_familias:
    # Percorrendo a lista e escrevendo no arquivo uma família por linha
    for familia in lista_de_familias:
        arquivo_familias.write(f"{familia.salario}, {familia.num_filhos}\n")

print("\n======= Dados das famílias salvos com sucesso! =======")

# Lendo dados de um arquivo
# Limpando a lista de famílias
lista_de_familias = []
print("\n======= Acessando dados de um arquivo =======")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        salario, num_filhos = linha.strip().split(",")
        lista_de_familias.append(Familia(salario=float(salario), num_filhos=int(num_filhos)))

print("\n\n======= Exibindo dados das famílias do arquivo =======")
for familia in lista_de_familias:
    print(f"Salário: R$ {familia.salario:.2f}")
    print(f"Número de Filhos: {familia.num_filhos}")