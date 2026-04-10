name=input("Enter file name: ")
handle=open(name)
counts={}
for line in handle:
    if not line.startswith("From "):
        continue
    words=line.split()
    hour=words[5].split(":")[0]
    counts[hour]=counts.get(hour,0)+1
for hour, counts in sorted(counts.items()):
    print(hour, counts)
