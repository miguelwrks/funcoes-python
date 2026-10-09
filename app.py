import os

def clear(): #limpar terminal
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print("Programa das funções - Notas\n")
nome = input(str('Digite seu nome: '))

qtde_notas = int(input('Qnatas notas irão ser calculadas?:'))
notas = [] #lista, pra receber vários valores
for i in range(qtde_notas):
    nota = float(input(f'Digite a {i+1} nota:')) #+1 pq começa c zero ai p deixar o usuario digitando como se fosse 1
    notas.append(nota) #vai adicionar a nota dentro da lista (notas)


soma_total_notas = 0 # vai somar todas as notas da lista
for nota in notas: #para as notas (nota) na lista notas, ele vai somar elas
    soma_total_notas = soma_total_notas+nota
    

#calcular media das notas 
def media_notas():
   # print(f'As notas a serem usadas são: {notas}\n que somaram no total: {soma_total_notas} e serão divididas por {qtde_notas}.')
    media = (soma_total_notas/qtde_notas)
    return media


def verificar_aprovacao(media_aluno): #aprovação do aluno
    #media_aluno = parametro pra poder verificar a logica
    return media_aluno>= 6 # vai gerar um valor booleano, p armazenar a media sem printar na tela



#Gerar um resumo/relatório exibindo o nome do aluno, as notas, a média e o status (Aprovado/Reprovado).#
def relatorio():
    aprov = verificar_aprovacao(media)
    
    if aprov: #true convertido pra texto
        situação = 'APROVADO'
    else: #false convertido pra texto
        situação = 'REPROVADO'
        
    #relatório
    print("\n================\nRELATÓRIO FINAL\n================")
    print(f"Aluno:    {nome}")
    print(f"Notas:    {notas}")
    print(f"Média:    {media:.2f}")
    print(f"Situação: {situação}")
    

media = media_notas()
clear()
relatorio()
