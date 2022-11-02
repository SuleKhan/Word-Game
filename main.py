# 23/01/2022
import random
import time
import os


def choose_keys(num_vowels, num_letters):
    vowels = "aeiou"
    alpha = "bcdfghjklmnpqrstvwxyz"
    choices = []
    for i in range(num_vowels):
        choices.append(vowels[random.randint(0, 4)])

    for i in range(num_letters):
        choices.append(alpha[random.randint(0, 20)])

    random.shuffle(choices)
    return choices


def check_word_is_real(word):
    with open("Dictionary.txt", "r") as file:
        data = file.read()
    data.split("\n")
    if word in data: return True, True

    return False, "Word Does Not Exist!"


def check_ans_is_valid(ans, new_keys):
    new_keys = keys[:]
    if len(ans) < 2:
        return False, "Word Too Small!"
    if " " in ans:
        return False, "No Spaces Allowed!"
    else:
        for i in ans:
            if i not in new_keys:
                return False, "Invalid Answer!"
            new_keys.remove(i)

    return True, True


def check_guess(guess):
    with open("guesses.txt", "r") as file:
        data = file.readlines()

    if guess + "\n" in data:
        return False, "Already Guessed!"
    return True, True


def print_keys(keys):
    design = (f"         {keys[0]}         \n\n"
          f"    {keys[1]}         {keys[2]}\n\n"
          f"      {keys[3]}      {keys[4]}\n\n")
    return design


def print_guesses():
    with open("guesses.txt", "r") as file:
        data = file.read()
    return data


lives = 3
keys = choose_keys(2, 3)
score = 0
with open("guesses.txt", "w"):
    pass

while lives > 0:
    os.system("cls")

    if lives == 3:
        print("Lives: ♥♥♥" + f"          Score: {score}" + "\n")
    if lives == 2:
        print("Lives: ♥♥" + f"           Score: {score}" + "\n")
    if lives == 1:
        print("Lives: ♥" + f"            Score: {score}" + "\n")

    print(print_keys(keys))
    print("Guesses:")
    print(print_guesses())
    answer = input("Input Answer: ").lower()

    valid, invalid_error = check_ans_is_valid(answer, keys)
    real, fake_error = check_word_is_real(answer)
    not_guessed, guessed_error = check_guess(answer)

    if valid and real and not_guessed:
        with open("guesses.txt", "a") as file:
            file.write(answer)
            file.write("\n")
        score += 1
        print("\nCorrect Answer!")
    elif not valid:
        lives -= 1
        print(invalid_error)
        print("\nLife Lost!")
    elif not real:
        lives -= 1
        print(fake_error)
        print("\nLife Lost!")
    elif not not_guessed:
        lives -= 1
        print(guessed_error)
        print("\nLife Lost!")

    time.sleep(2)

os.system("cls")
print(f"      YOUR SCORE: {score}")
