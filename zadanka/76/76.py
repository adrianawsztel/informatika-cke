szyfr1 = []
szyfr1Key = None
with open('szyfr1.txt') as file:
    for line in file:
        szyfr1.append(line.strip())
    szyfr1Key = list(map(int, szyfr1[-1].split()))
    szyfr1.pop()

# 76.1

def szyfrowanko(keys, word):
    wordKeyed = list(word)
    n = len(keys)
    for i in range(len(word)):
        position = keys[(i % n)] - 1
        wordKeyed[i], wordKeyed[position] = wordKeyed[position], wordKeyed[i]
    return ''.join(wordKeyed)

for word in szyfr1:
    print(szyfrowanko(szyfr1Key, word))

# 76.2

szyfr2 = []
szyfr2Key = None
with open('szyfr2.txt') as file:
    for line in file:
        szyfr2.append(line.strip())
    szyfr2Key = list(map(int, szyfr2[-1].split()))
    szyfr2.pop()

for word in szyfr2:
    print(szyfrowanko(szyfr2Key, word))

# 76.3


def odszyfrowanie(keys, word):
    wordKeyed = list(word)
    n = len(keys)
    for i in range(len(word) - 1, -1, -1):
        position = keys[(i % n)] - 1
        wordKeyed[i], wordKeyed[position] = wordKeyed[position], wordKeyed[i]
    return ''.join(wordKeyed)

szyfr3 = None

with open('szyfr3.txt') as file:
    szyfr3 = file.readline().strip()

print(szyfr3)

odszyfrowanySzyfr3 = odszyfrowanie([6, 2, 4, 1, 5, 3], szyfr3)
print(odszyfrowanySzyfr3)