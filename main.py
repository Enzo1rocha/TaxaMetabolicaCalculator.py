from utils import dados_usuario, inteiro_input
from formulas import harris_benedict, miflin_jeor


print("------ CALCULADORA DE TMB ------")
dados_usuario()

while True:
  print(f"{'='*30}\n{'ESCOLHA DE FORMULAS':^30}\n{'='*30}\n1 - Harris Benedict\n{'-'*30}\n2 - Miflin St Jeor\n{'='*30}")
  escolha_formulas = inteiro_input("Escolha Uma...")
  if escolha_formulas in [1, 2]:
    break
  
if escolha_formulas == 1:
  tmb = harris_benedict
elif escolha_formulas == 2:
  tmb = miflin_jeor
  