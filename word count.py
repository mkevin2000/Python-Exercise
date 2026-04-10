text="truck rate truck load rate load load"
counts={}
words=text.split()
for w in words:
    counts[w]=counts.get(w,0)+1
print(counts)    