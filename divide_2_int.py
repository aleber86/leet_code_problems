"""Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer 
range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, 
and if the quotient is strictly less than -2^31, then return -2^31."""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor == 0:
            return

        if(dividend <= 0 and divisor < 0) or (dividend >= 0 and divisor > 0):
            sign = True
        elif(dividend >= 0 and divisor <0) or (dividend <= 0 and divisor > 0):
            sign = False
            
       
                
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        str_divisor = str(divisor)
        len_divisor = len(str_divisor)
  
        str_dividend = str(dividend)
        len_dividend = len(str_dividend)
  
        n = 0
        rest = 0
        i_hi = 1
        i_lo = 0
 
        ran = len_dividend

        while i_hi <= ran:
            q = 0
            rest = str(rest)
            div = rest + str(str_dividend[i_lo:i_hi])
            div = int(div)
         
            if div >= divisor:
                while div >= divisor:
                    div = div - divisor
                    q = q + 1
                q = str(q)
                for j in range(i_hi,ran):
                    q = q+'0'
                n = n + int(q)

                i_lo=i_hi
            else:

                i_lo+=1
            rest = div
            i_hi+=1
             
        
        if sign:
            n = int(n)
        else:
            n = int(-n)
#        if ((dividend < -2**31 or divisor > 2**31-1)):
#            return 2**31-1

        if (n < -2**31 or n > 2**31-1):
            return 2**31-1
        
        return n
