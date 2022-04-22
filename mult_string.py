"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly."""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        if int(num1) > int(num2):
            a = num1
            num1 = num2
            num2 = a

        num2 = reversed(num2)
        first = "0"
        for index,mul in enumerate(num2):
            plus = 0
            cifra = int(mul)
            lista2 = ''
            for mul2 in reversed(num1):
                cifra2 = int(mul2)*cifra+plus
                cifra2 = str(cifra2)
                lista2 = f"{lista2}{cifra2[-1:]}"
                #lista2 = f"{cifra2[-1:]}{lista2}"
                if len(cifra2)>1:
                    plus = int(cifra2[0:1])
                else:
                    plus = 0
            if plus!= 0:
                lista2 = f"{lista2}{plus}"
                #lista2 = f"{plus}{lista2}"
            if index != 0 :
                suma = self.__suma(first,lista2,index)
                first = suma
            else:
                first = lista2
        first = list(first)
        first.reverse()
        result = ""
        result = result.join(first)
        return result

    def __suma(self, st, nd, index):
        nd = index*"0"+nd
        zeros = len(nd)-len(st)
        st = st+zeros*"0"
        nd = list(nd)
        st = list(st)
        decena = 0
        sumando = 0
        resultado = ""
        for indx, digit in enumerate(st):
            digit_st = int(digit)
            digit_nd = int(nd[indx])
            sumando = digit_st + digit_nd + decena
            if sumando > 9 :
                decena = str(sumando)[:-1]
                decena = int(decena)
            else:
                decena = 0
            
            resultado = f"{resultado}{str(sumando)[-1:]}"
        if decena > 0:
            resultado = f"{resultado}{decena}"
        return resultado
