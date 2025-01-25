import random
# import string
import time
# from itertools import product


# class Brute_force_crack:

#     def brute_force_passsword(target, charset):
#         start_time = time.time()

#         for guess in map(''.join, product(charset, repeat=len(target))):
#             if guess == target:
#                 return time.time() - start_time
            
    
#     def generate_random_password(length, charset):
#         return ''.join(random.choice(charset) for _ in range(length))
    

# attack = Brute_force_crack()

# attack.brute_force_passsword()
     

# number = int(input("Enter your password: "))
# guess =0
# while(guess != number):
#     guess = random.randint(0,99999)
#     print(guess)


# print(f"Your guess number: {str(number)}")


def test_brute_force(numberOfTest):
  times = []
  for i in range(numberOfTest):
    target_pin = int(random.randint(1000, 9999))
    start_time = time.time()
    test_brute_force(target_pin)
    end_time = time.time()
    time.append(end_time - start_time)
  return time