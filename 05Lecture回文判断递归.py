def isPalind(s):
    def toChar(s):
        char = ''
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz":
                char += i 
        return char
    
    def is_pal(s):
        s = toChar(s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    
    return is_pal(s)
            
print(isPalind("aba b  a ba"))