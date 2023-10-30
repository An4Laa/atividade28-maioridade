from datetime import date

today = date.today()
anoAtual = today.year

Maior_id = []
Menor_id = []

for itrm in range (8):
    anoNasc = int(input("Digite o ano de nascimento: "))
    if anoAtual - anoNasc >= 18 :
        Maior_id.append(anoNasc)
    else :
        Menor_id.append(anoNasc)

print(f"Lista dos maiores de idade: {Maior_id}")
print(f"Lista dos menores de idade: {Menor_id}")