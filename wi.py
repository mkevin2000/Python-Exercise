name=input("Enter file: ")
if len(name)<1:
   name="mbox-short.txt"
handle=open(name)
count=dict()
for line in handle:
    if line.startswith("From"):
        words=line.split()
        email=words[1]
        count[email]=count.get(email, 0)+1
bigcount=None
bigemail=None       
for email,count in count.items():
    if bigcount is None or count>bigcount:
        bigemail=email
        bigcount=count
print(bigemail, bigcount)

