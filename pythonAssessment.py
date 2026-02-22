# pythonAssessment.py
# Text Analysis Program for News Articles


import string
from collections import Counter


# -----------------------------
# Read File Function
# -----------------------------
def read_file(file_path):
    """
    Reads the contents of a text file and returns it as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""


# -----------------------------
# 1. Count Specific Word
# -----------------------------
def count_specific_word(text, search_word):
    """
    Counts how many times a specific word appears in the text.
    Returns an integer.
    """
    if not text:
        return 0

    # Remove punctuation and convert to lowercase
    text = text.lower()
    search_word = search_word.lower()

    words = text.translate(str.maketrans("", "", string.punctuation)).split()

    return words.count(search_word)


# -----------------------------
# 2. Identify Most Common Word
# -----------------------------
def identify_most_common_word(text):
    """
    Returns the most common word in the text.
    Returns None if text is empty.
    """
    if not text.strip():
        return None

    text = text.lower()
    words = text.translate(str.maketrans("", "", string.punctuation)).split()

    if not words:
        return None

    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]

    return most_common_word


# -----------------------------
# 3. Calculate Average Word Length
# -----------------------------
def calculate_average_word_length(text):
    """
    Calculates the average word length.
    Returns a float.
    Returns 0 if text is empty.
    """
    if not text.strip():
        return 0

    words = text.translate(str.maketrans("", "", string.punctuation)).split()

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    average = total_length / len(words)

    return average


# -----------------------------
# 4. Count Paragraphs
# -----------------------------
def count_paragraphs(text):
    """
    Counts the number of paragraphs.
    Paragraphs are separated by empty lines.
    Returns an integer.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


# -----------------------------
# 5. Count Sentences
# -----------------------------
def count_sentences(text):
    """
    Counts the number of sentences.
    Sentences end with ., !, or ?
    Returns an integer.
    Returns 1 if text is empty.
    """
    if not text.strip():
        return 1

    sentence_count = 0
    for char in text:
        if char in ".!?":
            sentence_count += 1

    return sentence_count


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("=== NEWS ARTICLE TEXT ANALYSIS ===")

    file_path = input("Enter the path to the news article file: ")

    text = read_file(file_path)

    if not text:
        print("No text to analyze.")
        return

    # Count specific word
    search_word = input("Enter the word you want to count: ")
    word_count = count_specific_word(text, search_word)
    print(f"\nThe word '{search_word}' appears {word_count} times.")

    # Most common word
    common_word = identify_most_common_word(text)
    print(f"The most common word is: {common_word}")

    # Average word length
    avg_length = calculate_average_word_length(text)
    print(f"The average word length is: {avg_length:.2f}")

    # Paragraph count
    paragraph_count = count_paragraphs(text)
    print(f"The number of paragraphs is: {paragraph_count}")

    # Sentence count
    sentence_count = count_sentences(text)
    print(f"The number of sentences is: {sentence_count}")


# Run the program
if __name__ == "__main__":
    main()