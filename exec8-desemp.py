faltas = int(input("Número de faltas: "))
vendas = float(input("Valor das vendas: "))
 
if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")