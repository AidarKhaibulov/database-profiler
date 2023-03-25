import numpy as np


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


def simpleDecode(text, key, zeros, size, type):
    def addZeros(blockSize, blocks):
        dif = blockSize - len(blocks[-1])
        blocks[-1] = blocks[-1] + '\0' * dif

    blockSize = len(key) * size
    blocks = [text[i:i + blockSize] for i in range(0, len(text), blockSize)]

    addZeros(blockSize, blocks)
    answer = ''
    if(zeros):
        for block in blocks:
            answer += permutation(block, key, zeros, size, 1)
        answer = answer.replace('\0', '')
    else:
        blockCopy=blocks[-1]
        blockCopy=permutation(blockCopy,key,True,size,0)
        zerosPositions=[]
        for c in range(len(blockCopy)):
            if blockCopy[c]=='\0':
                zerosPositions.append(c)
        for c in zerosPositions:
            blocks[-1]=blocks[-1][0:c]+ '\0'+ blocks[-1][c:]
        blocks[-1]=blocks[-1][0:blockSize]
        for block in blocks:
            answer += permutation(block, key, zeros, size, 1)
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


def verticalDecode(text, key, zeros, size, type):
    answer = verticalAdapter(key, size, text, zeros, 1)
    return answer


def verticalAdapter(key, size, text, zeros, action):
    # 0 means code, 1 means decode
    f=False
    if(action==1 and not zeros):
        f=True
        action=0
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
        if(zeros):
            for i in range(rows):
                for j in range(columns):
                    answer += res[i][j]
        else:
            zerosPositions=[]
            for i in range(len(res[-1])):
                if res[-1][i]=='':
                    zerosPositions.append(i)
            newText=''
            rowCounterLimit=rows-1
            rowCounter=0

            inner = []
            m = []
            it = iter(text)
            for i in range(columns):
                for j in range(rows):
                    if (rowCounter == rowCounterLimit):
                        if(zerosPositions.__contains__(i)):
                            inner.append('\0')
                        else:
                            inner.append(it.__next__())
                        rowCounter=0
                        break
                    inner.append(it.__next__())
                    rowCounter+=1

                m.append(inner)
                inner = []
            m = np.array(m).transpose()
            res = m.copy()

            text=''
            for i in range(columns):
                for j in range(rows):
                    if(res[j][i]==''):
                        text+='\0'
                    else:
                        text+=res[j][i]

            answer = verticalAdapter(key, size, text, True, 1)
            return answer

    return answer

