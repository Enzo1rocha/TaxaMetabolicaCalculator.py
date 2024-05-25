def decimal_input(prompt):
  while True:
    try:
      valor = float(input(prompt))
      if valor > 0:
        return valor
      else:
        print("Apenas Números Positivos São Aceitos")
    except ValueError:
      print("Apenas Números São Aceitos")

def inteiro_input(prompt):
  while True:
    try:
      valor = int(input(prompt))
      if valor > 0:
        return valor
      else:
        print("Apenas Números Inteiros e Positivos São Aceitos")
    except ValueError:
      print("Apenas Números Inteiros e Positivos São Aceitos")
      
def dados_usuario():
  idade = inteiro_input("Informe Sua Idade:")
  peso = decimal_input("Informe Seu Peso (Kg):")
  altura = decimal_input("Informe Sua Altura (Cm):")
  while True:
    genero = str(input("Qual Seu Gênero? Homem/Mulher")).strip().lower()
    if genero in ["homem", "mulher"]:
      break
    else:
      print("Escolha Uma das Opcões")
  print("Niveis De Ativida Fisica:\n{}\nTaxa Metabolica: Apenas o Gasto em Repouso\n{}\nSedentario: Pouco ou Nenhum Exercício Fisico Semanal\n{}\nLeve: Exercícios 1/2 Dias na Semana\n{}\nModerado: Exercícios 3/5 Dias Na Semana\n{}\nIntenso: Exercícios 6/7 Dias na Semana\n{}\nAtleta: Exercícios 2x Por Dia\n{}".format("="*30, "-"*30, "-"*30, "-"*30, "-"*30, "-"*30, "="*30))
  while True:
    fisica = str(input("Escolha Seu Nivel de Atividade Fisica")).lower()
    if fisica in ["taxa metabolica", "sedentario", "leve", "moderado", "intenso", "atleta"]:
      break
    else:
      print("Escolha Uma das Opções Listadas")
  return idade, peso, altura, genero, fisica
  
  def harris_benedict():
    dados_usuario = genero
    if genero == "homem":
      tmb = (13.7516 * peso) + (5.0033 * altura) - (6.755 * idade) + 66.473
    else:
      tmb = (9.5634 * peso) + (1.8496 * altura) - (4.6756 * idade) + 655.0955

def miflin_jeor():
  dados_usuario = genero
  if genero == "homem":
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
  else:
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

def atividades_fisicas():
  if fisica == "taxa metabolica":
    tmb
  if fisica == "sedentario":
    tmb = tmb*1.90
  if fisica == "leve":
    tmb = tmb*1.375
  if fisica == "moderado":
    tmb = tmb*1.55
  if fisica == "intenso":
    tmb = tmb*1.725
  if fisica == "atleta":
    tmb = tmb*1.9
  
idade, peso, altura, genero, fisica = dados_usuario()
print("Olá, Sou uma Calculadora de Metabolismo Basal\nInforme a Formula Escolhida\n{}\n1 - Harris-Benedict\n{}\n2 - Mifflin-St-Jeor\n{}\nObservacão = Digite o Valor Corresponde".format("="*30, "-"*30, "="*30))
while True:
  escolha_formula = inteiro_input("Valor Correspondente:")
  if escolha_formula == 1:
    harris_benedict(genero, peso, altura, idade)
    break
  if escolha_formula == 2:
    miflin_jeor(genero, peso, altura, idade)
    break
  else:
    print("Digite O Valor de Uma Das Opcões Listadas")
  