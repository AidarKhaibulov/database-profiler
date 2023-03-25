import coding

#print(coding.simpleCode('aabbccddeeffgghh',[3,2,1,0],False,1,'символы'))
#print(coding.simpleCode('abcdefghpq',[1,3,0,2],False,1,'символы'))
#print(coding.simpleCode('00001111000011110000111100001111',[7,6,5,4,3,2,1,0],False,1,'символы'))
#print(coding.simpleCode('0123456701234567',[7,6,5,4,3,2,1,0],False,1,'символы'))
#print(coding.simpleCode('01234567012345670000111100001111',[7,6,5,4,3,2,1,0],False,2,'символы'))


#простая c нулями
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
