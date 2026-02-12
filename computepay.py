def computepay(h, r):
    if h <= 40: 
        pay= h*r
        return pay
    else:
        overtime= h-40
        pay= 40*r+(overtime*(1.5*r))
        return pay 
hrs= float(input("Enter hours: "))
rate= float(input("Enter rate: "))
p= computepay(hrs, rate)
print("Pay", p)
