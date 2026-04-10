sentence=input("Enter a sentence: ")
count=dict()
words=sentence.split()
for word in words:
    count[word]=count.get(word, 0)+1
print(count)
bigcount=None
bigword=None
for word,count in count.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword, bigcount)        