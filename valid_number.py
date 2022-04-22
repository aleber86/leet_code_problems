"""A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number."""


class Solution:
    
    def try_value_up(self, index, string):
        try:
            sub = string[index + 1: ]           
            int(sub)
            sub = string[index + 1: ] + '0'
            int(sub)
            
            return True    
        
        except:
            return False
        
    
    def try_value_down(self, index, string):
        try:
            sub = string[0:index]
            float(sub)
            sub = sub + '0'
            float(sub)
            return True
        except:
            return False
        
    
    def isNumber(self, s: str) -> bool:
        
        valid = False #return value -> if valid True
        
        symbol = ['+','-','.','e','E']
        
        #positive = 0
        #negative = 0
        
        sym_pos = []
        
        for sym in symbol:
            counter = s.count(sym)
            if counter > 1 and (sym != '+' and sym != '-'):
                return False
            if counter > 2:
                return False
                         
            index = s.find(sym)
         
            if index < 0:
                index = False
            sym_pos.append(index)
        
        
        e_value = False
        
        if sym_pos[4]>0 and sym_pos[3]>0:
            #Exponential symbol must be e or E
            return False
        elif sym_pos[4]>0 and (not sym_pos[3]):
            index_num = sym_pos[4]
            e_value = True
        elif (not sym_pos[4]) and sym_pos[3] > 0:
            index_num = sym_pos[3]
            e_value = True
            
        else:
            
            try:
                float(s)
                float(s+'0')
                return True
            except:
                return False
            
        if e_value:
            valid_l = self.try_value_up(index_num, s)
            valid_r = self.try_value_down(index_num, s)
            
            if not(valid_l) or not(valid_r):return False
            
        valid = True
        
        return valid
        
