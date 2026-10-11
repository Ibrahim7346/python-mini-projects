target_password = "zzz"

characters = "abcdefghijklmnopqrstuvwxyz"

attempts = 0

for first in characters:
    for second in characters:
        for third in characters:

            guess = first + second + third
            attempts += 1

            print("Tryng:", guess)

            if guess == target_password:
                print("\nPassword Found")
                print("Password:", guess)
                print("Attempt:", attempts)
                exit()