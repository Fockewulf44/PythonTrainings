#Hackinscience - Playing with Anagrams
# https://www.hackinscience.org/exercises/is_anagram

"funeral"
"real fun"

def is_anagram(str1: str, str2: str) -> bool:
    
    for c in str1:
        str2 = str2.replace(c,"")
    
    if str2.replace(" ","") == "":
        return True
    else:
        return False
    
result = is_anagram("funeral", "real fun")
print(result)