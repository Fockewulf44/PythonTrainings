#Hackinscience - Playing with Anagrams
# https://www.hackinscience.org/exercises/is_anagram

"character"
"limit"
# 1st iteration
# Letter f; replace f with "" --> "real un"

# 2nd iteration
# Letter u; replace u with "" --> "real n"

# def is_anagram(str1: str, str2: str) -> bool:
    
#     for character in str1:
#         str2 = str2.replace(character,"")
    
#     if str2.replace(" ","") == "":
#         return True
#     else:
#         return False
    
# result = is_anagram("character", "limit")
# print(result)

def is_anaram(str1: str, str2: str) -> bool:
    
    str1_dict=[]
    for character in str1:
        ind1 = str2.find(character)
        str2 = str2(0:ind1) + str2(0:ind1+1)
        
