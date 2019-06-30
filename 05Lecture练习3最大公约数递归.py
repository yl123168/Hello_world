def printMove(fr,to):
    print("move form %s to %s"%(fr,to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
        
Towers(3,"middle","target","spare")