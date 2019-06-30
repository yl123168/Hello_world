def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new_tup = ()
    if aTup == ():
        return ()
    for i in range(0,len(aTup),2):
        new_tup += (aTup[i],)
    return new_tup

print(oddTuples((1,2,'s',4,(5,"ss"),6)))