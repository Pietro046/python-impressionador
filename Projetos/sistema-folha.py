salario_horas = float(input("Digite seu salario por hora: "))
horas_trabalhadas = float(input("Digite quantas horas trabalhou no mes: "))
salario_bruto = salario_horas * horas_trabalhadas

if salario_bruto <= 900:
  desconto = 0
elif salario_bruto <= 1500:
  desconto = 0.05
elif salario_bruto <= 2500:
  desconto = 0.1
else:
  desconto = 0.2

ir = salario_bruto * desconto
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
salario_liquido = salario_bruto - ir - inss

print(f"Seu salario bruto é {salario_bruto:.2f} reais")
print(f"(-) IR ({desconto *100}%) O IR do seu salario é {salario_bruto * desconto:.2f} reais")
print(f"(-) INSS (10%) O INSS é {salario_bruto * 0.1:.2f} reais")
print(f"FGTS (11%) O FGTS é {salario_bruto * 0.11:.2f} reais, lembrando que não desconta do salario")
print(f"Total de descontos {inss + ir:.2f}")
print(f"Seu salário liquido é {salario_liquido:.2f}")
