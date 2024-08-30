def ler_grid():
    with open('grid.txt') as f:
        a = f.read()
        return a.split("\n")

print(ler_grid())
a = ler_grid()
print(type(a))