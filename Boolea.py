messages = [
    "Load 1 picked up in Dallas",
    "Rate is 2.7 per mile",
    "Driver says no issues",
    "Load 3 delivered",
    "Finished for today"]
keyword= input("Enter a keyword: ").strip().lower()
found=False
for message in messages:
    if keyword in message.lower():
        found=True
        print(message)
if not found:
    print("not found")   
       
