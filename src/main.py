import random

def guess_the_number():
    print("Gambling simulator'!")
    number_to_guess = random.randint(1, 100000000000000)
    number_of_attempts = 0
    guess = None

    while guess != number_to_guess:
        guess = int(input("Try to guess a number between 1 to :100000000000000 "))
        number_of_attempts += 1
        
        if guess < number_to_guess:
            print("lOW Try again u low IQ.")
        elif guess > number_to_guess:
            print("HIGH Try again moron.")
    
    print(f"Wow you cheated in my game. you took  {number_to_guess} in {number_of_attempts} tries.")

if __name__ == "__main__":
    guess_the_number()
   
   
    