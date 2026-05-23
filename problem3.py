#Word Frequency Counter
words=input("enter the words to count:")
dict={}
for i in words:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
print(dict)