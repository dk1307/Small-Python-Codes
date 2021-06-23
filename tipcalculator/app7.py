#Custom Tip calculator
# (10%, 15% and 20%)
print("\nWelcome to My custom Tip Calculator\n")
while True:
    try:
        user_input = input("What is the total of your pay amount? Rupees: ")
        total_check = float(user_input)
        break 
    except ValueError:
        print("Heyy I'm sorry, It's looks like you typed something incorrect words. try typing in a number! Thank u :)")

while True:
    tip_choice = input("For Tip: Type 'a' for 10%, 'b' for 15%, or 'c' for 20% : ")
    if tip_choice not in ('a', 'b', 'c'):
        print("Heyy I'm sorry, It's looks like you typed something incorrect words. Please read the instructions and try again! thank u :)")
    else:
        if tip_choice == "a":
            result = 0.10 * total_check + total_check
        elif tip_choice == "b":
            result = 0.15 * total_check + total_check
        elif tip_choice == "c":
            result = 0.20 * total_check + total_check
        
        print("\nHeyy You should total leave Rupees: %.3f " % (result))
        break