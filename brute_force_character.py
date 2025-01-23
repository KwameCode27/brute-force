import random
import pyautogui

character= "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

password = pyautogui.password()
guess = ""
while (guess != password):
    guess = random.choices(character_list, k=len(password))
    guess = "".join(guess)
    print(guess)

print(f"Your password is : {guess}")