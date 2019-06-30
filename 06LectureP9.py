animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def howMany(aDict):
    result = 0
    if aDict == {}:
        return result
    for i in aDict.values():
        result += len(i)
    return result

def biggest(aDict):
    if aDict == {}:
        return None
    key_list = aDict.keys()
    key = key_list[0]
    for i in key_list:
        if len(aDict[i]) > len(aDict[key]):
            key = i
    return key





test = {}
test2 = {'a':[]}
#print(howMany(animals))
#print(howMany(test))
print(biggest(animals))
print(biggest(test))
print(biggest(test2))
