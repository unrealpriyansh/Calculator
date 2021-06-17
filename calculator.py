print("Enter type of arthimetic calculation you want :")
print("For addition type '+' ")
print("For subtraction type '-'")
print("For multiplication type '*' ")
print("For division type '/'")
opt=input("Enter here...")
i=int(input("Enter First number here ->"))
iii=int(input("Enter second number here ->"))
a,b,c,d="+","-","*","/"
if opt==a:
    print(i+iii)
elif opt==b:
    print(i-iii)
elif opt==c:
    print(i*iii)
elif opt==d:
    print(i/iii)
