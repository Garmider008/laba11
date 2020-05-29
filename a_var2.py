from random import randint
import struct


def generateFile(filename='f'):
    components = randint(2, 100)
    while (components % 5 != 0) and (components % 2 != 0):
        components += 1
    with open(filename, 'wb') as f:
        listToWrite = []
        for i in range(components // 2):
            listToWrite.append(randint(-100, -1))
            listToWrite.append(randint(1, 100))
        packedInt = struct.pack(f'{len(listToWrite)}i', *listToWrite)
        f.write(packedInt)


def writeToG(filename='g', filenameRead='f'):
    with open(filenameRead, 'rb') as f:
        listn = sorted([i[0] for i in struct.iter_unpack('i', f.read())])
    newList = []
    with open('g', 'wb') as g:
        for i in range(len(listn) // 3):
            flag = False if i % 2 != 0 else True
            listn = sorted(listn, reverse=flag)
            newList.extend(listn[0:3])
            listn = listn[3::]
        newList.extend(listn)
        print(newList)
        packedInt = struct.pack(f'{len(newList)}i', *newList)
        g.write(packedInt)


if name == 'main':
    # якщо скрипт запущений на пряму, тільки тоді буде виконаний код нижче
    generateFile()
    writeToG()