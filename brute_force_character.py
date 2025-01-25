import random
import pyautogui


character= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
character_list = list(character)

password = input("Enter your password:")
guess= ""
while (guess != password):
    # checking random alphanumeric
    guess = random.choices(character_list, k=len(password))
    guess = "".join(guess)
    print(guess)

print(f"Your password is : {guess}")