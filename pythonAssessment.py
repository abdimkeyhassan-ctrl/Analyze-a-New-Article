# pythonAssessment.py
# Beginner Friendly Text Analysis Program

import string
from collections import Counter


# -----------------------------
# Read File Function
# -----------------------------
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return ""


# -----------------------------
# 1. Count Specific Word
# -----------------------------
def count_specific_word(text, search_word):
    if not text:
        return 0

    text = text.lower()
    search_word = search_word.lower()

    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    return words.count(search_word)


# -----------------------------
# 2. Identify Most Common Word
# -----------------------------
def identify_most_common_word(text):
    if not text.strip():
        return None

    words = text.lower().translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    if not words:
        return None

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


# -----------------------------
# 3. Calculate Average Word Length
# -----------------------------
def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = text.translate(
        str.maketrans("", "", string.punctuation)
    ).split()

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


# -----------------------------
# 4. Count Paragraphs
# -----------------------------
def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


# -----------------------------
# 5. Count Sentences
# -----------------------------
def count_sentences(text):
    if not text.strip():
        return 1

    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count


# -----------------------------
# Main Program (WITH WHILE LOOP)
# -----------------------------
def main():

    print("=== NEWS ARTICLE TEXT ANALYSIS ===")

    file_path = input("Enter the path to the news article file: ")
    text = read_file(file_path)

    # Conditional check
    if not text:
        print("No text loaded. Program will exit.")
        return
    else:
        print("File loaded successfully!\n")

    # WHILE LOOP to allow repeated analysis
    while True:

        print("\nChoose an option:")
        print("1 - Count Specific Word")
        print("2 - Identify Most Common Word")
        print("3 - Calculate Average Word Length")
        print("4 - Count Paragraphs")
        print("5 - Count Sentences")
        print("6 - Exit")

        choice = input("Enter your choice (1-6): ")

        # Conditional statements
        if choice == "1":
            search_word = input("Enter word to search: ")
            result = count_specific_word(text, search_word)
            print(f"The word '{search_word}' appears {result} times.")

        elif choice == "2":
            result = identify_most_common_word(text)
            print(f"Most common word: {result}")

        elif choice == "3":
            result = calculate_average_word_length(text)
            print(f"Average word length: {result:.2f}")

        elif choice == "4":
            result = count_paragraphs(text)
            print(f"Number of paragraphs: {result}")

        elif choice == "5":
            result = count_sentences(text)
            print(f"Number of sentences: {result}")

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Run program
if __name__ == "__main__":
    main()