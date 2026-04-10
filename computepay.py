deal=0
no_responses=0
while True:
    line=input("Enter result(Deal/No/Skip/Done) ").strip().lower()
    if line=="skip":
        continue
    elif line=="deal":
        deal=deal+1
    elif line=="no":
        no_responses=no_responses+1
    elif line=="done":
        break       
    else:
        print("Invalid Input")
Total =deal+no_responses         
print("Total Attempts: ", Total)
print("Deals: ", deal)
print("No responses:", no_responses)
print("Deal rate: ", deal/(deal+no_responses)*100,"%")
if Total==0:
      print("Deal rate: 0")
else:
    print("Deal rate:", (deal / Total) * 100, "%")     
         