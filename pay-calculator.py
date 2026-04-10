# a program that keeps asking the user to enter numbers,
#  and when the user types done, it prints the largest number entered.
largest=None
while True:
    value=input("Enter a number (or 'done' to finish): ").strip().lower()
    if value=="done":
        break
    try:
        num=float(value)
        if largest is None or num>largest:
            largest=num
    except ValueError:
        print("Invalid input")
print(" The largest number is:", largest)       