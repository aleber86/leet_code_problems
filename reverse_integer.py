"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer 
range [-231, 231 - 1], then return 0."""


class Solution:
    def reverse(self, x: int) -> int:
        if (x>=(2**31-1) or x<=-2**31):
            return 0
        result = ''
        if (x==0):
            return 0
        elif (x<0):
            str_int = str(x)
            str_int = str_int[1:]
            long = len(str_int)-1
            for i in range(long+1):
                result = result + str_int[long-i]
            result = int(result)
            result = -result
            
        elif (x>0):
            str_int = str(x)
            long = len(str_int)-1
            for i in range(long+1):
                result = result + str_int[long-i]    
            result = int(result)
        
        if (result>=(2**31-1) or result<=-2**31):
            return 0
        return result
        
