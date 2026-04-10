Total = 0
Count = 0
while True:
    value = input("enter a number: ").strip()
    if value.lower() == "done":
        break
    try:
        num = float(value)
    except ValueError:
        print("Invalid input")
        continue
    Total = Total + num
    Count = Count + 1

print(Total)
print(Count)
Average = Total / Count if Count > 0 else 0
print(Total, Count, Average)
