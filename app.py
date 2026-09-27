# entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts: "))
tempo_uso_dia = float(input("Digite o tempo de uso do aparelho em horas: "))


# processamento
consumo_diario = (potencia * tempo_uso_dia) / 1000  # Convertendo para kWh
consumo_mensal = consumo_diario * 30  # Considerando 30 dias no mês
custo_mensal = consumo_mensal * 0.85  # Considerando o custo de R$ 0,85 por kWh

# saída
print(f"---resultado---")
print(f"O consumo diário do aparelho {aparelho} é de {consumo_diario:.2f} kWh.")
print(f"O consumo mensal do aparelho {aparelho} é de {consumo_mensal:.2f} kWh.")
print(f"O custo mensal baseado no consumo do aparelho {aparelho} é de R$ {custo_mensal:.2f}.")

print(f"Lembre-se de que esses valores são estimativas e podem variar dependendo do uso real do aparelho e da tarifa de energia elétrica.")
print(f"utilize o consumo de energia de forma consciente para economizar e preservar o meio ambiente.")

print(f"Obrigado por utilizar o programa de cálculo de consumo de energia!")

