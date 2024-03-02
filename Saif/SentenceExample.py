# Sentences

sentence = "This food is very spicy and hurts when I eat"

sentencesplit = sentence.split(" ")
print(sentencesplit)

LongestWord = ""
LongestLength = 0

for word in sentencesplit:
    if len(word) > LongestLength:
        LongestLength = len(word)
        LongestWord = word
        
print(LongestWord)
print(LongestLength)