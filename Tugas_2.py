

def desimalTobiner(X):
    biner = ''
    while X != 0:
        sisa = X % 2
        X = X//2
        biner = str(sisa) + biner
    print('Nilai Biner = ', biner)


def desimalToOktal(X):
    oktal = ''
    while X != 0:
        sisa = X % 8
        X = X//8
        oktal = str(sisa) + oktal
    print('Nilai Oktal = ', oktal)


def desimalToHexa(X):
    hexa = ''
    while X != 0:
        sisa = X % 16
        X = X//16
        if sisa == 10:
            hexa = 'A' + hexa
        elif sisa == 11:
            hexa = 'B' + hexa
        elif sisa == 12:
            hexa = 'C' + hexa
        elif sisa == 13:
            hexa = 'D' + hexa
        elif sisa == 14:
            hexa = 'E' + hexa
        elif sisa == 15:
            hexa = 'F' + hexa
        else:
            hexa = str(sisa) + hexa
    print('Nilai Hexa = ', hexa)


def binerToDesimal(X):
    floor = len(X) - 1
    desimal = 0
    for i in range(len(X)):
        iBin = int(X[i])
        iDes = iBin * (2 ** floor)
        desimal += iDes
        floor -= 1
    print('Nilai Desimal = ', desimal)


def binerToOktal(X):
    odig = 0
    mul = chk = 1
    onum = ''

    while X != 0:
        sisa = X % 10
        odig += (sisa * mul)

        if chk % 3 == 0:
            onum += str(odig)
            mul = chk = 1
            odig = 0
        else:
            mul *= 2
            chk += 1

        X = int(X / 10)

    if chk != 1:
        onum += str(odig)

    print('Nilai Oktal = ', onum[::-1])


def binerToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1

    count = 1

    hexaDeciNum = ['0'] * 100

    i = 0
    while bnum != 0:
        sisa = bnum % 10
        temp = temp + (sisa*mul)

        if count % 4 == 0:

            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1

        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)

    if count != 1:
        hexaDeciNum[i] = chr(temp+48)

    if count == 1:
        i = i-1
    print('Nilai Hexa = ', ''.join(hexaDeciNum[i::-1]))


def oktalToDesimal(X):
    desimal = 0
    base = 1
    while X != 0:
        sisa = X % 10
        X = X//10
        desimal += sisa * base
        base *= 8
    print('Nilai Desimal = ', desimal)


def oktalToBiner(X):

    bnum = bin(X)

    print('Nilai Biner = ', bnum[2:])


def oktalToHexa(X):

    hnum = hex(X)

    print('Nilai Hexa = ', hnum[2:])
