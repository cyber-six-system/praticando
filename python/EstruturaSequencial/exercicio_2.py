def isNum(x):
    
    while not x.isnumeric():
            x = input("Digite um número: ")
            
    return "número %d foi informado!" % int(x)

print(isNum(input()))
