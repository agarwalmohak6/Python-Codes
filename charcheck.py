c=input("Enter a character ")
if c>='a' and c<='z':
    print("LowerCase")
elif c>='A' and c<='Z':
    print("UpperCase")
elif c>='0' and c<='9':
    print("Digit")
else:
    print("Special character")
