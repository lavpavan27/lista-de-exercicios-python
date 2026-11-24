regiao = input("Digite a região: ").upper()
 
if regiao == "SE" or regiao == "S":
    print("Frete: R$ 15")
elif regiao == "CO":
    print("Frete: R$ 25")
elif regiao == "NE" or regiao == "N":
    print("Frete: R$ 35")
else:
    print("Região inválida")
 