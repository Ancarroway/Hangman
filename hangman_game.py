
import random

# ASCII Art for Hangman Stages (Visual representation of the game)
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Word categories - Each category contains a list of words
WORD_CATEGORIES = {
    "Animals": ["elephant", "giraffe", "kangaroo", "zebra", "dolphin"],
    "Fruits": ["apple", "banana", "strawberry", "watermelon", "pineapple"],
    "Countries": ["canada", "brazil", "france", "germany", "japan"],
    "Programming": ["python", "javascript", "algorithm", "developer", "variable"]
}

def choose_word():
    print("\nSelect a category:")
    for i, category in enumerate(WORD_CATEGORIES.keys(), 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("\nEnter the number of your category choice: "))
            if 1 <= choice <= len(WORD_CATEGORIES):
                category = list(WORD_CATEGORIES.keys())[choice - 1]
                return random.choice(WORD_CATEGORIES[category]), category
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    while True:
        word, category = choose_word()
        guessed_letters = set()
        attempts = 6
        hints_used = False
        score = 0

        print(f"\n🎮 Welcome to Hangman! (Category: {category})")
        print(HANGMAN_PICS[0])
        print(display_word(word, guessed_letters))

        while attempts > 0:
            print(f"\nRemaining attempts: {attempts}")
            guess = input("Guess a letter, type 'hint' for a hint, or type 'solve' to guess the full word: ").lower()

            if guess == "hint":
                if not hints_used:
                    hint_letter = random.choice([l for l in word if l not in guessed_letters])
                    print(f"💡 Hint: The word contains the letter '{hint_letter}'.")
                    guessed_letters.add(hint_letter)
                    hints_used = True
                else:
                    print("⚠️ You have already used your hint.")
                continue

            elif guess == "solve":
                solution = input("Enter your guess for the whole word: ").lower()
                if solution == word:
                    score = attempts * 10
                    print(f"🎉 Congratulations! You solved the word '{word}'! Your final score is: {score}")
                    break
                else:
                    print("❌ Incorrect guess! You lose all remaining attempts.")
                    attempts = 0
                    break

            if len(guess) != 1 or not guess.isalpha():
                print("⚠️ Invalid input. Enter a single letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("✅ Correct guess!")
            else:
                attempts -= 1
                print("❌ Wrong guess!")
                print(HANGMAN_PICS[6 - attempts])

            print(display_word(word, guessed_letters))

            if set(word) <= guessed_letters:
                score = attempts * 10
                print(f"\n🎉 Congratulations! You guessed the word '{word}'! Your final score is: {score}")
                break

        if attempts == 0:
            print(f"\n💀 Game Over! The word was '{word}'. Better luck next time!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    hangman()
