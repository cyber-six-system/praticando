
def isNum(x):
    while not x.isnumeric():
            x = input("Digite um número: ")
    return x

def soma(x, y):
    return int(x) + int(y)


result = soma(isNum(input()), isNum(input()))

print("Resultado %d da soma dos números" % int(result))
