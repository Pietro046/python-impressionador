vitorias = input("Digite quantas vitórias seu time teve: ")
empates = input("Digite quantos empates seu time teve: ")
derrotas = input("Digite quantas derrotas seu time teve: ")


if vitorias == "" or empates == "" or derrotas == "":
  print("Digite um valor existente")
else:
  vitorias = int(vitorias)
  empates = int(empates)
  derrotas = int(derrotas)
  jogos_disputados = vitorias + empates + derrotas
  

  if jogos_disputados == 0:
    print("Digite um valor diferente de 0")
  else:  
    pontos = vitorias * 3 + empates * 1
    aproveitamento = round(pontos / (jogos_disputados * 3) * 100, 2)
  
    if aproveitamento <= 40:
      print(f"Seu time esta com grandes chances de cair para a série B do campeonato, o aproveitamento do seu time é de {aproveitamento}%")
    elif aproveitamento <=65:
      print(f"Seu time esta com grandes chances de ficar no meio da tabela do campeonato, o aproveitamento do seu time é de {aproveitamento}%")
    else:
      print(f"Seu time esta com grandes chances de ficar no G4 da tabela do campeonato, o aproveitamento do seu time é de {aproveitamento}%")
