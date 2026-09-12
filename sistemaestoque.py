produto = input("Digite o produto: ")
categoria = input("Digite a categoria: ")
estoque = (input("Digite a quantidade no estoque: "))

if produto and categoria and estoque:
  estoque = int(estoque)
  if categoria == "bebidas":
    if estoque <= 75:
      print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")
    else:
      pass
  elif categoria == "alimentos":
    if estoque <= 50:
      print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")
    else:
      pass
  else:
    if categoria == "limpeza":
      if estoque <= 30:
        print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")
else:
  print("Preencha todas informações")        
