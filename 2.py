"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salario e numero de filhos das familias da cidade.
A prefeitura deseja saber:
a) total de familias que responderam a pesquisa;
b) média do salário da população;
c) media do numero de filhos;
d) maior salario;
e) menor salario.
Crie um menu com as seguintes opcoes.
Código | Descrição
     1 | Adicionar familia
     2 | Exibir resultados
     3 | Sair
Ao adicionar uma familia, deve-se limpar o terminal e apresentar o menu novamente.
1. Salve os dados em um arquivo com nome: pesquisa_prefeitura.txt
2.0 programa deve ler o arquivo para exibir os dados salvos.



Turma - G93313

Nome das componentes.
1 - Jamile Souza Reis
2 - Rayane Costa dos Santos
3 - Araúna Noemi
"""


import os
from dataclasses import dataclass
os.system("cls || clear")

# Estrutura de dados
salario = []
filhos = []
lista_de_familias = []
familias = []


print("""
   ======= Menu =======
----------------------------
Código | Descrição         |
-------|-------------------|
 1     | Adicionar Família |
 2     | Exibir Resultados |
 3     | Sair              |""")

while True:
    opcao = int(input("Digite o código da opção desejada: "))

    if opcao == 1:
        filhos = int(input("Digite quantos filhos você tem: "))
        filhos.append(filhos)
        salario = int(input("Digite o seu salário: "))
        salario.append(salario)
        familias.append(1)
        os.system ("cls || clear")
        
        total_de_familias = sum(familias)
        soma_dos_salarios = sum(salario)
        soma_dos_filhos = sum(filhos)
        maior_salario = max(salario)
        menor_salario = min(salario)

        media_filhos = soma_dos_filhos / total_de_familias
        media_de_salarios = soma_dos_salarios / total_de_familias

    elif opcao == 2:
        print(f"Total de familias: {total_de_familias}")
        print(f"Média de salário: {media_de_salarios}")
        print(f"Média de filhos: {media_filhos}")
        print(f"Maior Salário: {maior_salario}")
        print(f"Menor Salário: {menor_salario}")

    elif opcao == 3:
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")

nome_do_arquivo = "Pesquisa_de_Habitantes.txt"

with open(nome_do_arquivo, "w") as Pesquisa_de_Habitantes:
    Pesquisa_de_Habitantes.write(f"Total de familias: {total_de_familias}")
    Pesquisa_de_Habitantes.write(f"Média de salário: {media_de_salarios}")
    Pesquisa_de_Habitantes.write(f"Média de filhos: {media_filhos}")
    Pesquisa_de_Habitantes.write(f"Maior Salário: {maior_salario}")
    Pesquisa_de_Habitantes.write(f"Menor Salário: {menor_salario}")


Pesquisa_de_Habitantes.close()
print("======= Dados Salvo com Sucesso! ========")

with open(nome_do_arquivo, "r")as arquivo_de_origem:
    for linha in arquivo_de_origem:
        linha.strip().split("\n")

Pesquisa_de_Habitantes.close()


print(f"Total de familias: {total_de_familias}")
print(f"Média de salário: {media_de_salarios}")
print(f"Média de filhos: {media_filhos}")
print(f"Maior Salário: {maior_salario}")
print(f"Menor Salário: {menor_salario}")