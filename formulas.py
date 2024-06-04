from utils import dados_usuario

def harris_benedict():
  genero = dados_usuario
  if genero == "homem":
    tmb = (13.7516 * peso) + (5.0033 * altura) - (6.755 * idade) + 66.473
  else:
    tmb = (9.5634 * peso) + (1.8496 * altura) - (4.6756 * idade) + 655.0955

def miflin_jeor():
  genero = dados_usuario
  if genero == "homem":
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
  else:
    tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161