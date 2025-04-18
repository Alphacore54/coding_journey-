import random
from colorama import init, Fore

init(autoreset=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def guess_if_u_can():
    secret = random.randint(1, 100)
 #   print(secret)
    attempts = 0

    print(Fore.CYAN + "="*40)
    print(Fore.MAGENTA + "     WELCOME TO 'GUESS IF U CAN'")
    print(Fore.CYAN + "="*40)

    while True:
        try:
            guess = int(input(Fore.GREEN + "\nGuess the number (1-100): "))
            attempts += 1
            if guess == secret and attempts <= 3:
                print(Fore.GREEN + f"holy cow u guessed this shit at freaking less that 3 attempt ur something else ur einstien")
                break

            if guess == secret:
                print(Fore.GREEN + f"he he hee u guess it in {attempts} i dare u can't do that in less that three attempts ")
                break
            elif guess < secret:
                print(Fore.RED + "open ur brain bro why are u thinking too low go outside touch some grass man think beyond the 6th floor .")
            else:
                print(Fore.RED + "okay ur thing too high thinking of a goal which is beyond ur reach is not good but it's risky")
            if attempts == 8 :
                 print(Fore.RED+"somtime i wonder if i can be cloud just go with flow without worring about future wht u are taking more that 8 attempts to guess a freaking number such noob haha ")
            # Even/Odd Hint
            if attempts == 3:
                if secret % 2 == 0:
                    print(Fore.RED + "Hint:"+Fore.YELLOW+" now u need a hint huh do u know bwm m4 can hit 1 - 100 in just freaking 3 sec that something sick with 550 nm torque oooo u need hints the number u want is if u divide it with 2 u will get 0 ")
                else:
                    print(Fore.RED + "Hint:"+Fore.YELLOW+" huh u can't even guess a number in 3 attempts think about a rock okay now hummer that thing untill u got salt of that rock then mix that thing in water what will u get nothing right now think of a number if we divide that with 2 it will not give 0 ")

            if is_prime(secret) and attempts == 3:
                print(Fore.RED + "Hint :"+Fore.YELLOW+" it's prime yeah it's prime not the number it's from transformer i big truck optims prime not the number ok ")
            elif secret != 1 and attempts == 3:
                print(Fore.RED + "Hint:"+Fore.YELLOW+" i misss prime (╥﹏╥) but he is not here and it's not prime number too")       

        except ValueError:
            print(Fore.RED + "hey u stop messing with my code ask ur math teach what number is ")

# Run it
guess_if_u_can()