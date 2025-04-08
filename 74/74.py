lista = []
with open("hasla.txt") as plik:
    for line in plik:
        lista.append(line.strip())
print(lista)
ile = 0
for haslo in lista:
    if haslo.isdecimal():
        ile += 1
print(ile)
slownik = {}
for haslo in lista:
    if haslo in slownik:
        slownik[haslo] += 1
    else:
        slownik[haslo] = 1
for k, v in slownik.items():
    if v > 1:
        print(k)
ile = 0
for haslo in lista:
    cyfra = False
    mala = False
    duza = False
    for znak in haslo:
        if ord(znak) >= 48 and ord(znak) <= 57:
            cyfra = True
        if ord(znak) >= 65 and ord(znak) <= 90:
            duza = True
        if ord(znak) >= 97 and ord(znak) <= 122:
            mala = True
    if cyfra and mala and duza:
        ile += 1
print(ile)