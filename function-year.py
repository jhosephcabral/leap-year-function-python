def ehBissexto(a):
    if (ano % 400 == 0) or (ano % 4 == 0) and not(ano % 100 == 0):
        return True
    else:
        return False

#--------------------------------------------

for ano in range(2000, 2022):
    if ehBissexto(ano):
        print(ano, " é bissexto")
    else:
        print(ano, " não é bissexto")