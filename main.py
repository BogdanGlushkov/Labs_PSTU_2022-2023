import numpy as NP


def printTable(vector):
    print('xyzw  f')
    for el in range(16):
        n = '0' * (4 - len(NP.binary_repr(el))) + NP.binary_repr(el)
        print(n + '  ' + vector[el])


def makeSDNF(vector):
    options = []
    for el in range(16):
        option = ''
        if vector[el] == '1':
            n = '0' * (4 - len(NP.binary_repr(el))) + NP.binary_repr(el)
            if n[0] == '1':
                option += 'x'
            else:
                option += 'X'
            if n[1] == '1':
                option += 'y'
            else:
                option += 'Y'
            if n[2] == '1':
                option += 'z'
            else:
                option += 'Z'
            if n[3] == '1':
                option += 'w'
            else:
                option += 'W'
            options.append(option)
    return options


def showSDNF(options):
    quote = ''
    for i in range(len(options)):
        if i != len(options) - 1:
            quote += (options[i]) + ' + '
        else:
            quote += (options[i])
    print(f'\nSDNF = {quote}\n')


def showMDNF(otvet):
    quote = ''
    for i in range(len(otvet)):
        if i != len(otvet) - 1:
            quote += (otvet[i]) + ' + '
        else:
            quote += (otvet[i])
    print(f'\nMDNF = {quote}')


def printInvTable(options):
    lastRespond = []
    quote = ''
    mainotvet = []
    for i in range(len(options)):
        quote += (options[i]) + ' '
    print(f'    {quote}')

    for elOptions in options:
        for elStr in options:
            if elOptions != elStr:
                count = 0
                otvet = ''
                for i in range(4):
                    if elOptions[i] == elStr[i] and count != 3:
                        count += 1
                        otvet += elOptions[i]
                        if count == 3:
                            if otvet not in mainotvet:
                                mainotvet.append(otvet)
                                makeOtvet(otvet, elOptions, elStr, options, lastRespond)
    showMDNF(lastRespond)


def makeOtvet(otvet, elOptions, elStr, options, lastRespond):
    # print(options.index(elOptions))
    # print(options.index(elStr))
    if abs(options.index(elOptions) - options.index(elStr)) == 1:
        lastRespond.append(otvet)
    otvet += '   '
    if options.index(elOptions) < options.index(elStr):
        if options.index(elOptions) == 0:
            otvet += '+'
        else:
            otvet += ' ' + '     ' * (options.index(elOptions) - 1) + '    +'
        otvet += '     ' * (options.index(elStr) - 1 - options.index(elOptions)) + '    +'
    else:
        if options.index(elStr) == 0:
            otvet += '+'
        else:
            otvet += ' ' + '     ' * (options.index(elStr) - 1) + '    +'
        otvet += '     ' * (options.index(elOptions) - 1 - options.index(elStr)) + '    +'

    print(otvet)


quote = 0
while len(str(quote)) != 16:
    quote = input('Введите вектор функции: ')
printTable(quote)
showSDNF(makeSDNF(quote))
printInvTable(makeSDNF(quote))