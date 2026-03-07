#Password Strength Validator
class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ##Write your code here
        
        for p in passwords:
            if (len(p) >= 8 and
                any(c.isupper() for c in p) and
                any(c.isdigit() for c in p) and
                any(c in "@#$" for c in p)):
                
                strong.append(p)
       
        return strong