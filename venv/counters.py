from collections import Counter, defaultdict

li = [1,2,3,4,2,5,6,3,4,6,7,8,3,4,45,6,7]

sentence = "The queer brown star jumed oof - I mean off - the froggy dew (jew?)"

print(Counter(sentence))
print(Counter(li))

dictionart = defaultdict(lambda: 'does not exist',{'a':1, 'b':2, 'c':3})

print (dictionart['d'])