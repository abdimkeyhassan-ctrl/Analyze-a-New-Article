"""
Text Analysis Script for News Articles
Performs various NLP tasks including word counting, statistics, and text structure analysis.
"""

import re
from collections import Counter


def count_specific_word(text, search_word):
    """
    Count the number of occurrences of a specific word in the text.
    
    Args:
        text (str): The text to search through
        search_word (str): The word to search for
    
    Returns:
        int: The count of occurrences (case-insensitive)
    
    Edge Cases:
        - Returns 0 if no matches are found
    """
    if not text or not search_word:
        return 0
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    search_word_lower = search_word.lower()
    
    # Use word boundaries to match whole words only
    pattern = r'\b' + re.escape(search_word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)
    
    return len(matches)


def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        str: The most common word (lowercase), or None if text is empty
    
    Edge Cases:
        - Returns None for empty string
    """
    if not text or not text.strip():
        return None
    
    # Extract words (alphanumeric sequences) and convert to lowercase
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    if not words:
        return None
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the most common word
    most_common = word_counts.most_common(1)[0][0]
    
    return most_common


def calculate_average_word_length(text):
    """
    Calculate the average length of words in the text.
    Excludes punctuation marks and special characters.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        float: The average word length
    
    Edge Cases:
        - Returns 0 for empty string
    """
    if not text or not text.strip():
        return 0.0
    
    # Extract words (only alphabetic characters)
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    if not words:
        return 0.0
    
    # Calculate total length and average
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    
    return average_length


def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    Paragraphs are defined by empty lines between blocks of text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: The number of paragraphs
    
    Edge Cases:
        - Returns 1 for empty string
    """
    if not text:
        return 1
    
    # Split by one or more empty lines (lines with only whitespace)
    paragraphs = re.split(r'\n\s*\n', text.strip())
    
    # Filter out empty paragraphs
    non_empty_paragraphs = [p for p in paragraphs if p.strip()]
    
    # Return at least 1 if text exists
    return max(1, len(non_empty_paragraphs))


def count_sentences(text):
    """
    Count the number of sentences in the text.
    Sentences are defined by punctuation marks: . ! ?
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: The number of sentences
    
    Edge Cases:
        - Returns 1 for empty string
    """
    if not text:
        return 1
    
    # Match sentence-ending punctuation (., !, ?)
    sentence_pattern = r'[.!?]+(?=\s|$)'
    sentences = re.split(sentence_pattern, text)
    
    # Filter out empty sentences
    non_empty_sentences = [s for s in sentences if s.strip()]
    
    # Return at least 1 if text exists
    return max(1, len(non_empty_sentences))


def read_article_from_file(filename):
    """
    Read the contents of a text file into a string.
    
    Args:
        filename (str): Path to the text file
    
    Returns:
        str: The contents of the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def display_analysis_results(text, search_word=None):
    """
    Perform all text analysis tasks and display the results.
    
    Args:
        text (str): The text to analyze
        search_word (str): Optional word to search for
    """
    print("=" * 60)
    print("TEXT ANALYSIS RESULTS")
    print("=" * 60)
    
    # Task 1: Count specific word
    if search_word:
        word_count = count_specific_word(text, search_word)
        print(f"\n1. Count of '{search_word}': {word_count}")
    else:
        print("\n1. No specific word provided for counting.")
    
    # Task 2: Most common word
    most_common = identify_most_common_word(text)
    print(f"\n2. Most common word: {most_common}")
    
    # Task 3: Average word length
    avg_length = calculate_average_word_length(text)
    print(f"\n3. Average word length: {avg_length:.2f} characters")
    
    # Task 4: Paragraph count
    paragraph_count = count_paragraphs(text)
    print(f"\n4. Number of paragraphs: {paragraph_count}")
    
    # Task 5: Sentence count
    sentence_count = count_sentences(text)
    print(f"\n5. Number of sentences: {sentence_count}")
    
    print("\n" + "=" * 60)


def main():
    """
    Main function to run the text analysis program.
    """
    print("News Article Text Analysis Tool")
    print("=" * 60)
    
    # Read from a file
    filename = input("\nEnter the path to the news article file (or press Enter to use sample text): ").strip()
    
    if filename:
        article_text = read_article_from_file(filename)
        if not article_text:
            print("Unable to read file. Exiting.")
            return
    else:
        # Sample news article for demonstration
        article_text = """
The impact of artificial intelligence on modern society continues to grow. 
Artificial intelligence is transforming industries across the globe!

Technology companies are investing billions in AI research. The development of 
AI has accelerated rapidly in recent years. Many experts believe artificial 
intelligence will revolutionize healthcare, education, and transportation.

However, concerns about AI ethics and job displacement remain significant. 
Policymakers are working to establish regulations. The future of AI depends 
on responsible development and implementation.

What will the next decade bring? Only time will tell. The AI revolution is 
just beginning!
"""
        print("\nUsing sample news article text.")
    
    # Get word to search for
    search_word = input("\nEnter a word to count (or press Enter to skip): ").strip()
    if not search_word:
        search_word = "artificial"  # Default for demonstration
        print(f"Using default search word: '{search_word}'")
    
    # Perform analysis and display results
    display_analysis_results(article_text, search_word)


if __name__ == "__main__":
    main()