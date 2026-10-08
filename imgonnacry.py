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
    

#calcular media das notas agr
def media_notas():
    print(f'As notas a serem usadas são: {notas}\n que somaram no total: {soma_total_notas} e serão divididas por {qtde_notas}.')
    media = (soma_total_notas/qtde_notas)
    return media


def verificar_aprovacao(media_aluno):
    #media_aluno = parametro pra poder verificar a logica
    if media_aluno>= 6:
        print('aprovado')
    else:
        print('reprovado')

media = media_notas()
verificar_aprovacao(media)

#oq eu quero: programa verifica, armazena, exibe apenas quando for mostrar o relatório e não na funcao
#entao aprovado teria que ser true e reprovado false, ai a função n deveria exibir nada, apenas armazenar



#Gerar um resumo/relatório exibindo o nome do aluno, as notas, a média e o status (Aprovado/Reprovado).#
def relatorio():
    situação = verificar_aprovacao(media)
    print(f'{nome}, as suas notas foram: {notas} respectivamente,\ncom uma média de {media} e você foi {situação}')
    
