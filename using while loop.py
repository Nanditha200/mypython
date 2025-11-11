# Using a while loop
num = int(input("Enter an integer: "))
count = 0

# Handle zero case separately
if num == 0:
    count = 1
else:
    num = abs(num)  # To handle negative numbers
    while num > 0:
        num //= 10
        count += 1

print("Number of digits:", 
