#Desenvolva o código-fonte em Python,
#seguindo as boas práticas de programação, incluindo
#comentários explicativos e estruturação lógica do código. A
#solução será avaliada quanto à sua funcionalidade e
#adequação ao problema apresentado. A qualidade do
#código-fonte e a aplicação das estruturas de programação
#vistas na disciplina serão observadas. Entre as estruturas
#aplicadas na solução, devem estar presentes:
#• Conceitos de entrada, processamento e saída de dados (usar
#fstrings);
#• Armazenamento de dados em variáveis e listas;
#• Utilização de estruturas condicionais e de repetição;
#• Construção de funções (com passagem de parâmetros e
#retorno) para as principais funcionalidades da solução.
#• Entregável: Arquivo .py com o código-fonte desenvolvido.

import matplotlib.pyplot as plt
from random import randint

total_corridas=[1,2,3,4,5,6,7,8,9,10,11,12]
def plts_posicao():
    dic_posicao = {}
    print("Posição dos pilotos por corrida")
    for i in range(2):
        nome=input("Adicione o nome do piloto: ").upper()
        lista = []
        for j in range(12):
            #resultado= int(input(f"Insira a posição do piloto na {i+1}º corrida: "))
            resultado=randint(1,22)
            lista.append(resultado)

        dic_posicao[nome]=lista
    print("="*25)
    return dic_posicao

def plts_pontuacao():
    dic_pontuacao={}
    print("Pontuação dos pilotos por corrida")
    for i in range(2):
        nome = input("Adicione o nome do piloto: ").upper()
        lista = []
        for j in range(12):
            #resultado = int(input(f"Insira a pontuação do piloto na {i + 1}º corrida: "))
            resultado= randint(0, 27)
            lista.append(resultado)

        dic_pontuacao[nome] = lista
        dic_pontuacao[f"total {i+1}º piloto"]=sum(lista)
    print("=" * 25)
    return dic_pontuacao

posicao= plts_posicao()
pontuacao= plts_pontuacao()

print(posicao)
print(pontuacao)
piloto1, piloto2= posicao.keys()



plt.figure(figsize=(12, 6))
plt.suptitle(f"Posição por corrida {piloto1} e {piloto2}", fontsize=16)

# Configurações dos eixos
xpoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Plot 1
ypoints1 = posicao[piloto1]
plt.subplot(1, 2, 1)
plt.plot(xpoints, ypoints1, marker='o')
plt.title(f"Posição por corrida {piloto1}", loc='center')
plt.xlabel("Corridas")
plt.ylabel("Posição")

# Plot 2
ypoints2 = posicao[piloto2]
plt.subplot(1, 2, 2)
plt.plot(xpoints, ypoints2, marker='o')
plt.title(f"Posição por corrida {piloto2}", loc='center')
plt.xlabel("Corridas")
plt.ylabel("Posição")

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajusta automaticamente os subplots para caber na figura
plt.show()


#plot 2:
xpoints= [1,2,3,4,5,6,7,8,9,10,11,12]
ypoints= posicao [piloto2]

plt.subplot(1, 2, 2)
plt.plot(xpoints , ypoints)

plt.show()