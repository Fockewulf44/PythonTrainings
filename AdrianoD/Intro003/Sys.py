import sys
import re

path = str(sys.argv)
patn = re.sub(r"[\([{})\]]", "", path)
pathlist = patn.split('/')

print(pathlist)

for i in pathlist:
    if '.py' in i:
        print(i)