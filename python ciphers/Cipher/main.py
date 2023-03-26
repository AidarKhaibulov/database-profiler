import random

import coding

def check():
    args = currentCipher.split()
    print('id:', args[0])
    if (args[1] == '1'):
        alg = 'Простая перестановка'
    elif args[1] == '2':
        alg = 'Вертикальная перестановка'
    elif args[1] == '3':
        alg = 'Rail Fence'
    else:
        alg = 'Множественная перестановка'
    print('Алгоритм:', alg)
    if args[1] == '1' or args[1] == '2'or args[1] == '3' or args[1] == '4':
        print('Ключ:', args[2])
        print('С добавлением нулей? ' + args[3])
        if args[1]!='4':
            print('Количество символов в элементе: ' + args[4])
            print('Тип элемента: ' + args[5])

currentCipher = ''
print("Выберите действие:\n"
      "1 - Ввести параметры шифрования вручную\n"
      "2 - Сгенерировать ключ\n"
      "3 - Выбрать шифровку из базы")
choice = input()
if choice == '1':

    print("Выберите алгоритм:\n"
          "1 - Простая перестановка\n"
          "2 - Вертикальная перестановка\n"
          "3 - Rail Fence\n"
          "4 - Множественная перестановка\n")
    inpt = input()
    currentCipher += inpt
    currentCipher += ' '
    if inpt == '1' or inpt == '2' or inpt == '3' or inpt == '4':

        if (inpt == '3'):
            print("Введите m и n через запятые")
        if inpt=='4':
            print('Введите id применяемых шифровок через запятые')
        else:
            print("Введите ключ через запятые:")
        currentCipher += input()
        print("Выберите способ шифрования последнего блока:\n"
              "1 - С нулями\n"
              "2- Без нулей")
        if input() == '1':
            currentCipher += ' True '
        else:
            currentCipher += ' False '

        if inpt!='4':
            print("Введите количество символов в элементе блока")
            currentCipher += input()
            print("Выберите тип элемента:\n"
                  "1 - Символы\n"
                  "2 - Биты\n"
                  "3 - Байты")
            tpe = input()
            if tpe == '1':
                currentCipher += ' символы'
            elif tpe == '2':
                currentCipher += ' биты'
            else:
                currentCipher += ' байты'
        print("Шифровка задана успешно, сохранить в базе данных?(y/n)")
        if (input() == 'y'):
            print('Введите id, под которым будет сохранена шифровка')
            id = input()
            newText = ''
            fl = False
            with open("CIPHERS.txt") as f:
                for line in f:
                    if (line != '\n'):
                        ids = line.split()[0]
                    if (line != '\n' and int(ids) == int(id)):
                        print("Шифровка с таким ключом уже существует, выполняется перезаписывание")
                        newText += id + " " + currentCipher + '\n'
                        fl = True
                    else:
                        if (line != '\n'):
                            newText += line.rstrip() + '\n'
                if (not fl):
                    print("Шифровка сохранена")
                    newText += id + " " + currentCipher + '\n'
                f = open("CIPHERS.txt", "w")
                f.write(newText)
                f.close()
if choice == '2':
    if(random.randint(0, 1)==0):
        zeros=True
    else:
        zeros=False
    c=random.randint(0, 2)
    if(c==1):
        type='символы'
    elif c==2:
        type = 'биты'
    else:
        type='байты'
    print('Введите максимальную длину текста для генерируемой шифровки:')
    textSize=int(input())
    size=random.randint(1,textSize)
    print("Выберите алгоритм для генерации случайного ключа:\n"
          "1 - Простая перестановка\n"
          "2 - Вертикальная перестановка\n"
          "3 - Rail Fence\n"
          "4 - Множественная перестановка\n")
    q=input()
    if(q=='4'):
        
        pass
    elif q=='3':
        n=random.randint(2,textSize)
        m=random.randint(2,textSize)
        key=str(n)+','+str(m)

        currentCipher = q + ' ' + key + ' ' + str(zeros) + ' ' + str(size) + ' ' + type

        print('Введите id, под которым будет сохранена шифровка')
        id = input()
        newText = ''
        fl = False
        with open("CIPHERS.txt") as f:
            for line in f:
                if (line != '\n'):
                    ids = line.split()[0]
                if (line != '\n' and int(ids) == int(id)):
                    print("Шифровка с таким ключом уже существует, выполняется перезаписывание")
                    newText += id + " " + currentCipher + '\n'
                    currentCipher = id + ' ' + currentCipher
                    fl = True
                else:
                    if (line != '\n'):
                        newText += line.rstrip() + '\n'
            if (not fl):
                print("Шифровка сохранена")
                newText += id + " " + currentCipher + '\n'
                currentCipher = id + ' ' + currentCipher
            f = open("CIPHERS.txt", "w")
            f.write(newText)
            f.close()

        print(currentCipher)

    else:
        ls=list(range(0,textSize))
        random.shuffle(ls)
        key=''
        for e in ls:
            key+=str(e)+','
        key=key[0:-1]

        currentCipher=q+' '+ key+' '+str(zeros)+' '+str(size)+' '+ type

        print('Введите id, под которым будет сохранена шифровка')
        id = input()
        newText = ''
        fl = False
        with open("CIPHERS.txt") as f:
            for line in f:
                if (line != '\n'):
                    ids = line.split()[0]
                if (line != '\n' and int(ids) == int(id)):
                    print("Шифровка с таким ключом уже существует, выполняется перезаписывание")
                    newText += id + " " + currentCipher + '\n'
                    currentCipher = id + ' ' + currentCipher
                    fl = True
                else:
                    if (line != '\n'):
                        newText += line.rstrip() + '\n'
            if (not fl):
                print("Шифровка сохранена")
                newText += id + " " + currentCipher + '\n'
                currentCipher=id+' '+currentCipher
            f = open("CIPHERS.txt", "w")
            f.write(newText)
            f.close()

        print(currentCipher)

else:
    print("Введите id:")
    id=int(input())
    with open("CIPHERS.txt") as f:
        for line in f:
            if (line != '\n'):
                ids = line.split()[0]
            if (line != '\n' and int(ids) == id):
                currentCipher= line.rstrip()
                break
while(True):
    print("Текущая шифровка:")
    check()
    print()
    print('Выбор формата ввода сообщения:\n1 - Ввод в консоль\n2 - Считать с файла')
    if input()=='1':
        text=input('Введите текст\n')
        print("Выберите действие\n1 - Шифрование\n2 - Pасшифрование")
        # code
        coddec=input()
        if coddec=='1':
            args = currentCipher.split()
            if (args[3] == 'True'):
                args[3] = True
            else:
                args[3] = False
            if(args[1]=='1' or args[1]=='2' or args[1]=='3' or args[1]=='4'):
                list=[]
                for c in args[2]:
                    if(c!=','):
                        list.append(int(c))
                if(args[1]=='1'):
                    print(coding.simpleCode(text,list,(args[3]),int(args[4]),args[5]))
                elif(args[1]=='2'):
                    print(coding.verticalCode(text, list, (args[3]), int(args[4]), args[5]))
                elif (args[1] == '3'):
                    print(coding.railFenceCode(text, list, (args[3]), int(args[4]), args[5]))
                else:
                    print(coding.multipleCode(text, list, (args[3])))
                print('Расшифровать полученное сообщение?(y/n)')
                if input()=='y':
                    coddec='2'
                    if (args[1] == '1'):
                        text=coding.simpleCode(text,list,(args[3]),int(args[4]),args[5])
                    elif (args[1] == '2'):
                        text=coding.verticalCode(text,list,(args[3]),int(args[4]),args[5])
                    elif (args[1] == '3'):
                        text=coding.railFenceCode(text,list,(args[3]),int(args[4]),args[5])
                    else:
                        text=coding.multipleCode(text,list,(args[3]))


        # decode
        if coddec=='2':
            args = currentCipher.split()
            if(args[3]=='True'):
                args[3]=True
            else:
                args[3]=False
            if(args[1]=='1' or args[1]=='2' or args[1]=='3' or args[1]=='4'):
                list=[]
                for c in args[2]:
                    if (c != ','):
                        list.append(int(c))
                if (args[1] == '1'):
                    print(coding.simpleDecode(text, list, (args[3]), int(args[4]), args[5]))
                elif (args[1] == '2'):
                    print(coding.verticalDecode(text, list, (args[3]), int(args[4]), args[5]))
                elif (args[1] == '3'):
                    print(coding.railFenceDecode(text, list, (args[3]), int(args[4]), args[5]))
                else:
                    print(coding.multipleDecode(text, list, (args[3])))

# print(coding.simpleCode('aabbccddeeffgghh',[3,2,1,0],False,1,'символы'))
# print(coding.simpleCode('abcdefghpq',[1,3,0,2],False,1,'символы'))
# print(coding.simpleCode('00001111000011110000111100001111',[7,6,5,4,3,2,1,0],False,1,'символы'))
# print(coding.simpleCode('0123456701234567',[7,6,5,4,3,2,1,0],False,1,'символы'))
# print(coding.simpleCode('01234567012345670000111100001111',[7,6,5,4,3,2,1,0],False,2,'символы'))


# простая c нулями
'''
print(coding.simpleCode('abcdefghpq',[1,3,0,2],True,1,'символы'))
print(coding.simpleDecode('cadbgehf\0p\0q',[1,3,0,2],True,1,'символы'))
print()
'''
# простая без нулей
'''
print(coding.simpleCode('abcdefghpqk',[1,3,0,2],False,1,'символы'))
print(coding.simpleDecode('cadbgehfkpq',[1,3,0,2],False,1,'символы'))
'''

# вертикальная с нулями
'''
print(coding.verticalCode('aAbBcCdDeEfFgGhHpq',[1,3,0,2],True,2,'символы'))
print(coding.verticalDecode('cg\0CG\0aepAEqdh\0DH\0bf\0BF\0',[1,3,0,2],True,2,'символы'))
'''
# вертикальная без нулей
'''
print(coding.verticalCode('abcdefghpq',[1,3,0,2],False,1,'символы'))
print(coding.verticalDecode('cgaepdhbfq',[1,3,0,2],False,1,'символы'))
'''

# print(coding.railFenceCode('abcdefgh',[3,8],True,1,'символы'))
# print(coding.railFenceCode('abcdefghpqk',[3,4],True,1,'символы'))
# print(coding.railFenceCode('abcdefghpqk',[3,4],False,1,'символы'))

# print(coding.railFenceCode('aabbccddeeffgghh', [3, 4], True, 2, 'символы'))
# print(coding.railFenceDecode('aabbddcceeffhhgg', [3, 4], True, 2, 'символы'))


# rail fence с нулями
'''
print(coding.railFenceCode('abcdpq', [3, 4], True, 1, 'символы'))
print(coding.railFenceDecode('abdcpq\0\0', [3, 4], True, 1, 'символы'))
'''

# rail fence без нулей
'''
print(coding.railFenceCode('abcdefghp', [3, 5], False, 1, 'символы'))
print(coding.railFenceDecode('aebdcfgph', [3, 5], False, 1, 'символы'))
'''

# print(coding.railFenceCode('01010101000011110101010100001111', [3, 4], True, 1, 'биты'))
# print(coding.railFenceDecode('01100110000011110110011000001111', [3, 4], True, 1, 'биты'))

'''
print(coding.multipleCode('abcdpq', [1,2,4],False))
print(coding.multipleDecode('d\0\0cbqpa', [1,2,4],False))
'''