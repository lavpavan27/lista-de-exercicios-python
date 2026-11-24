 faturamento = float(input("Faturamento: "))
 
if faturamento > 100000:
    print("Limite aprovado: R$ 20.000")
elif faturamento >= 50000:
    print("Limite aprovado: R$ 10.000")
else:
    print("Crédito Reprovado")