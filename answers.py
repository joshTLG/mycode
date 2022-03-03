answer = input("What is your favorite restaurant?")
print(answer)

age = int(input("Please enter your age: "))
if age >= 21:
    print("You can buy booze and lotto")
else:
    print("You're just a wee baby")

while True:
    ans = input("How many languages are writeen from right to left?: ")
    if ans == "12":
        name = True
        print("That's right!")
        break
    else:
        print("\nNope. Please take another guess.\n") 
