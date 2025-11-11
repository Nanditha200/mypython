# even/odd and positive/negative combined

number = int(input("enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("even and positive")
    else:
        print("odd and positive")
elif num < 0:
    if num % 2 == 0:
        print("even and negative")
    else:
        print("odd and negative")
else:
    print("zero(neither positivr nor negative)")
         
