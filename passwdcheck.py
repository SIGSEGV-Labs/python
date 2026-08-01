SPECIALCHARS = """*"':;!?/)(+.,-&_$#@%[]}{\=°^¥€¢£~`|•√π÷×§∆©®<>"""
STRENGTH = 0

passwd = input("Enter the password: ")

# length check:
if len(passwd) > 8:
    STRENGTH += 2
    
# alphanumeric check:    
has_alpha = any(char.isalpha() for char in passwd)
has_digit = any(char.isdigit() for char in passwd)

if all([has_alpha, has_digit]):
    STRENGTH += 2

# special characters check:
for char in passwd:
    if char in SPECIALCHARS:
        STRENGTH += 1
        break
        
        
if STRENGTH == 0:
    print("The password is Very Weak.")
    
elif STRENGTH == 1:
    print("The password is Weak.")

elif STRENGTH == 2:
    print("The password is Medium.")
    
elif 3 <= STRENGTH <= 4:
    print("The password is Strong.")

else:
    print("The password is Very Strong.")       
