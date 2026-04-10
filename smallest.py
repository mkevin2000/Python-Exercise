smallest=None
print("Before",smallest)
for num in [23, 45, 7, 89,123, 1, 78]:
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
        print(smallest,num)
print("after", smallest)
