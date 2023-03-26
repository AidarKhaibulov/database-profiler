import numpy as np


def multipleCode(text, key,zeros):
    algorithms = []
    with open("CIPHERS.txt") as f:
        for line in f:
            if (line != '\n'):
                ids = line.split()[0]
            if (line != '\n' and key.__contains__(int(ids))):
                algorithms.append(line[0:-1])
    for alg in algorithms:
        args = alg.split()
        key = []
        for i in args[2]:
            if i != ',':
                key.append(int(i))
        if (args[1] == '1'):
            text = simpleCode(text, key, bool(args[3]), int(args[4]), 'символы')
        elif (args[1] == '2'):
            text = verticalCode(text, key, bool(args[3]), int(args[4]), 'символы')
        else:
            text = railFenceCode(text, key, bool(args[3]), int(args[4]), 'символы')
    return text


def multipleDecode(text, key,zeros):
    algorithms = []
    with open("CIPHERS.txt") as f:
        for line in f:
            if (line != '\n'):
                ids = line.split()[0]
            if (line != '\n' and key.__contains__(int(ids))):
                algorithms.append(line[0:-1])
    for alg in algorithms[::-1]:
        args = alg.split()
        key = []
        for i in args[2]:
            if i != ',':
                key.append(int(i))
        if (args[1] == '1'):
            text = simpleDecode(text, key, bool(args[3]), int(args[4]), 'символы',True)
        elif (args[1] == '2'):
            text = verticalDecode(text, key, bool(args[3]), int(args[4]), 'символы',True)
        else:
            text = railFenceDecode(text, key, bool(args[3]), int(args[4]), 'символы',True)
    if zeros:
        return text
    else:
        return text.replace('\0','')


def railFenceCode(text, key, zeros, size, type):
    if (type == 'биты'):
        finalSize = 8
    else:
        finalSize = key[1] * size
    blocks = [text[i:i + finalSize] for i in range(0, len(text), finalSize)]

    dif = finalSize - len(blocks[-1])
    blocks[-1] = blocks[-1] + '\0' * dif

    answer = ''
    for block in blocks:
        if (type == 'биты'):
            answer += railFenceCode(block, key, zeros, size, 'символы')
        else:
            m = createMatrix(key[0], key[1], block, size, 0)
            answer += matrixTraverse(key[0], key[1], m, text)

    if zeros:
        return answer
    else:
        return answer.replace('\0', '')


def railFenceDecode(text, key, zeros, size, type,spec=False):
    blocks = [text[i:i + key[1] * size] for i in range(0, len(text), key[1] * size)]

    dif = key[1] * size - len(blocks[-1])
    blocks[-1] = blocks[-1] + '\0' * dif

    if (not zeros):
        m = createMatrix(key[0], key[1], blocks[-1], size, 0)
        s = ''
        s += matrixTraverse(key[0], key[1], m, text)
        zeroPositions = []
        for i in range(len(s)):
            if (s[i] == '\0'):
                zeroPositions.append(i)

        for i in zeroPositions:
            blocks[-1] = blocks[-1][0:i] + '\0' + blocks[-1][i:]
        blocks[-1] = blocks[-1][0:key[1]]

    answer = ''
    for block in blocks:
        m = createMatrix(key[0], key[1], block, size, 1)

        it = iter(block)
        for i in range(key[0]):
            for j in range(key[1]):
                if (m[i][j] == '?'):
                    m[i][j] = ''
                    for q in range(size):
                        m[i][j] += it.__next__()
        i = 0
        j = 0
        dir = True
        for q in range(key[1]):
            if j == key[0] - 1:
                dir = False
            if j == 0:
                dir = True
            answer += m[j][i]
            if (dir):
                j += 1
            else:
                j -= 1
            i += 1

    if spec:
        return answer
    else:
        return answer.replace('\0', '')


def matrixTraverse(rows, columns, m, text):
    answer = ''
    for i in range(rows):
        for j in range(columns):
            if m[i][j] == '\x00':
                answer += '\0'
            else:
                answer += m[i][j]
    return answer


def createMatrix(rows, columns, text, size, action):
    m = []
    for i in range(rows):
        inner = []
        for j in range(columns):
            inner.append('')
        m.append(inner)

    if (action == 0):
        i = 0
        j = 0
        dir = True
        for q in range(columns):
            if j == rows - 1:
                dir = False
            if j == 0:
                dir = True
            if text[i] == '\0':
                m[j][i] = '\0'
            else:
                m[j][i] = text[q * size:(q + 1) * size]
            if (dir):
                j += 1
            else:
                j -= 1
            i += 1
        return m
    else:
        i = 0
        j = 0
        dir = True
        for q in range(columns):
            if j == rows - 1:
                dir = False
            if j == 0:
                dir = True
            m[j][i] = '?'
            if (dir):
                j += 1
            else:
                j -= 1
            i += 1
        return m


def permutation(block, key, zeros, size, action):
    oldBlock = []
    for l in range(len(block) // size):
        oldBlock.append(block[l * size:(l + 1) * size])
    newBlock = oldBlock.copy()
    for i in range(len(key)):
        if action == 1:
            newBlock[i] = oldBlock[key[i]]
        else:
            newBlock[key[i]] = oldBlock[i]
    if not zeros and oldBlock[-1].__contains__('\0'):
        for j in range(len(newBlock)):
            if newBlock[j].__contains__('\0'):
                newBlock[j] = ''
    return ''.join(newBlock)


def simpleDecode(text, key, zeros, size, type,spec=False):
    def addZeros(blockSize, blocks):
        dif = blockSize - len(blocks[-1])
        blocks[-1] = blocks[-1] + '\0' * dif

    blockSize = len(key) * size
    blocks = [text[i:i + blockSize] for i in range(0, len(text), blockSize)]

    addZeros(blockSize, blocks)
    answer = ''
    if (zeros):
        for block in blocks:
            answer += permutation(block, key, zeros, size, 1)
        if spec:
            answer = answer
        else:
            answer = answer.replace('\0', '')
    else:
        blockCopy = blocks[-1]
        blockCopy = permutation(blockCopy, key, True, size, 0)
        zerosPositions = []
        for c in range(len(blockCopy)):
            if blockCopy[c] == '\0':
                zerosPositions.append(c)
        for c in zerosPositions:
            blocks[-1] = blocks[-1][0:c] + '\0' + blocks[-1][c:]
        blocks[-1] = blocks[-1][0:blockSize]
        for block in blocks:
            answer += permutation(block, key, zeros, size, 1)
        if spec:
            answer = answer
        else:
            answer = answer.replace('\0', '')
    return answer


def simpleCode(text, key, zeros, size, type):
    def addZeros(blockSize, blocks):
        dif = blockSize - len(blocks[-1])
        blocks[-1] = blocks[-1] + '\0' * dif

    blockSize = len(key) * size
    blocks = [text[i:i + blockSize] for i in range(0, len(text), blockSize)]
    addZeros(blockSize, blocks)
    answer = ''
    for block in blocks:
        answer += permutation(block, key, zeros, size, 0)
    return answer


def verticalCode(text, key, zeros, size, type):
    answer = verticalAdapter(key, size, text, zeros, 0)
    return answer


def verticalDecode(text, key, zeros, size, type,spec=False):
    if spec:
        answer = verticalAdapter(key, size, text, zeros, 1,True)
    else:
        answer = verticalAdapter(key, size, text, zeros, 1)
    return answer


def verticalAdapter(key, size, text, zeros, action,spec=False):
    # 0 means code, 1 means decode
    f = False
    if (action == 1 and not zeros):
        f = True
        action = 0
    if (len(text) % (len(key) * size)) != 0:
        text = text + '\0' * (len(key) * size - (len(text) % (len(key) * size)))
    rows = len(text) // (len(key) * size)
    columns = len(key) * size
    inner = []
    m = []
    it = iter(text)
    if (action == 0):
        for i in range(rows):
            for j in range(columns):
                inner.append(it.__next__())
            m.append(inner)
            inner = []
        m = np.array(m)
        res = np.array(m).copy()
    else:
        for i in range(columns):
            for j in range(rows):
                inner.append(it.__next__())
            m.append(inner)
            inner = []
        m = np.array(m).transpose()
        res = m.copy()

    for i in range(len(key)):
        if (action == 0):
            res[:, key[i] * size:key[i] * size + size] = m[:, i * size: (i + 1) * size]
        else:
            res[:, i * size: (i + 1) * size] = m[:, key[i] * size:key[i] * size + size]

    answer = ''
    if (f and action == 0 and not zeros):
        action = 1
    if (action == 0):
        for i in range(columns):
            for j in range(rows):
                if (zeros and res[j][i] == ''):
                    answer += '\0'
                else:
                    answer += res[j][i]
    else:
        if (zeros):
            for i in range(rows):
                for j in range(columns):
                    if spec:
                        if res[i][j]=='':
                            answer+='\0'
                        else:
                            answer += res[i][j]

                    else:
                        answer += res[i][j]
        else:
            zerosPositions = []
            for i in range(len(res[-1])):
                if res[-1][i] == '':
                    zerosPositions.append(i)
            newText = ''
            rowCounterLimit = rows - 1
            rowCounter = 0

            inner = []
            m = []
            it = iter(text)
            for i in range(columns):
                for j in range(rows):
                    if (rowCounter == rowCounterLimit):
                        if (zerosPositions.__contains__(i)):
                            inner.append('\0')
                        else:
                            inner.append(it.__next__())
                        rowCounter = 0
                        break
                    inner.append(it.__next__())
                    rowCounter += 1

                m.append(inner)
                inner = []
            m = np.array(m).transpose()
            res = m.copy()

            text = ''
            for i in range(columns):
                for j in range(rows):
                    if (res[j][i] == ''):
                        text += '\0'
                    else:
                        text += res[j][i]

            answer = verticalAdapter(key, size, text, True, 1)
            return answer

    return answer
