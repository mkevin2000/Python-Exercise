hrs= input("Enter Hours" )
rate= input("Enter rate" )
try:
    h= float(hrs)
    r= float(rate)
except: 
    print("Please Enter numeric input")
if h<=40:
    print(h*r)
else:
    print(40*r+(h-40)*r*1.5)         