import random

random_number = random.randint(1, 100)
#print(random_number)
attempts = 0

def guess_number():
    global attempts
    while True:
        print("--------------")
        User_Value = int(input(f"Enter a number: \n"))
        print("--------------")
        attempts += 1
        
        if User_Value < random_number:
            print("You entered a smaller number.")
        elif User_Value > random_number:
            print("You entered a larger number.")
        else:
            if attempts > 5:

                print("---------------------------------------------------------")
                print(f"Your guess is correct! It took you {attempts} attempts.😒😒")
                print("---------------------------------------------------------")
            else:
                print("---------------------------------------------------------")
                print(f"Your guess is correct! It took you {attempts} attempts..😊😊")
                print("---------------------------------------------------------")
            break  

guess_number()
