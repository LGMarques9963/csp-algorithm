def ler_grid():
    with open('grid.txt') as f:
        a = f.read()
        return a.split("\n")

def ler_palavras():
    with open('lista_palavras.txt') as f:
        a = f.read()
        return a.split("\n")

print(ler_grid())
a = ler_grid()
print(type(a))
b = a[0].find(".")
print(b)
print(a[0][b])

palavras = ler_palavras()
print(palavras)