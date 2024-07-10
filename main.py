total = input("\n\nHello there, please enter the bill you will be paying\n")

percentage = input("\nPlease type the tip percentage you wish to pay.\n\n")

tips = (float(total) * int(percentage)) / 100

newTotal = float(total) + float(tips)

print(f"Your total amount is {total} and your tip is {tips}. Your new total amount is {round(newTotal, 2)}\n\nHave a Wonderful Day!")
