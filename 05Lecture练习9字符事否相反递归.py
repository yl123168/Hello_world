def semordnilapWrapper(str1, str2):
#     if len(str1) == 1 or len(str2) == 1:
#         return False
#     if str1 == str2:
#         return False
#     return semordnilap(str1, str2)
#     
# def semordnilap(str1, str2):
#     if len(str1) == 1 and len(str2) == 1:
#         return str1[0] == str2[-1]
#     else:
#         return semordnilap(str1[1:],str2[:-1])
# 
# print(semordnilapWrapper('tact ','  act'))



    # If strings aren't the same length, they cannot be semordnilap
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter
    # of str2
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False