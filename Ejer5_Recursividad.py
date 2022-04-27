#Desarrollar una función que permita convertir un número romano en un número decimal.

dic_Romano = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
def numeroDecimal(letras):

    if (len(letras)== 1):
        return dic_Romano[letras]
    elif (len(letras) == 2 and dic_Romano[letras[0]] < dic_Romano[letras[1]]):
        return dic_Romano[letras[1]] - dic_Romano[letras[0]]
    elif (dic_Romano[letras[0]] < dic_Romano[letras[1]]):
        return dic_Romano[letras[1]] - dic_Romano[letras[0]] + numeroDecimal(letras[2:])    
    else:
        return dic_Romano[letras[0]] + numeroDecimal(letras[1:len(letras):1])

print(numeroDecimal("IX"))
    