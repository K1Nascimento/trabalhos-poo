def printDecimal(x):
    return x
def printOctal(x):
    return oct(x)
def printHexa(x):
    return hex(x)
def printBin(x):
    return bin(x)
def imprimirTabela():
    print("Decimal",'\t','Octal','\t','Hexadecimal','\t','Binário','\n')
    print('-------', '\t','----- ','-----------    ', '--------', '\n')
    i = 0
    while i<=255:
        print('', printDecimal(i),'\t\t', printOctal(i), '\t', printHexa(i), '\t\t', printBin(i), '\n')
        i = i + 1
imprimirTabela()