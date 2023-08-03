print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count occurrences of letters in "true" and "love"
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

    # Combine the counts to make a 2-digit number
    love_score = int(str(true_count) + str(love_count))

    return love_score

def display_love_message(love_score):
    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")

if __name__ == "__main__":
    love_score = calculate_love_score(name1, name2)
    display_love_message(love_score)
