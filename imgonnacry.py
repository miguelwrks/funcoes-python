#Calcular a média das notas de uma matéria.

#Verificar se o aluno passou ou reprovou (por exemplo, se a média for maior ou igual a 6, está aprovado).

#Gerar um resumo/relatório exibindo o nome do aluno, as notas, a média e o status (Aprovado/Reprovado).#

# aluno digita seu nome, 
#aaluno digita as notas (que estarão dentro de uma lista,)
#vai definir a qtde de espoaços na lista c base em uma pergunta: qtas notas vai usar?
#aplicar um loop for in range (qtde de notas)
#dentro do loop pedir cada nota e ir somando em uma variavel (soma = soma+nota)

#usaremos o soma na função


print("Programa das funções - Notas\n")
nome = input(str('Digite seu nome:'))

qtde_notas = int(input('Qnatas notas irão ser calculadas?:'))
notas = []
for i in range(qtde_notas):
    nota = float(input(f'Digite a {i+1} nota:')) #+1 pq começa c zero ai p deixar o usuario digitando como se fosse 1
    notas.append(nota) #vai adicionar a nota dentro da lista (notas)


soma_total_notas = 0 # vai somar todas as notas da lista
for nota in notas: #para as notas (nota) na lista notas, ele vai somar elas
    soma_total_notas = soma_total_notas+nota
    
print(soma_total_notas)

#calcular media das notas agr
def media_notas():
    print(f'As notas a serem usadas são: {notas}\n que somaram no total: {soma_total_notas} e serão divididas por {qtde_notas}.')
    
    media = (soma_total_notas/qtde_notas)
    
    return print(media)


media_notas()
    
if media_notas(media) >= 6:
    print('aprovado')