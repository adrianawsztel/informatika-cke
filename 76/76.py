s = []
with open("szyfr1.txt") as file:
    for line in file:
        s.append(line.strip())

print(s)
def encryption(word, args):
    n = len(args)
    for i in range(len(word)):
        p = args[[i % n]] - 1
        encrypted[i], encrypted[p] = encrypted[p], encrypted[i]
    return encrypted