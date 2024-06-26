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