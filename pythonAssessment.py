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


def get_valid_filename():
    """
    Get a valid filename from the user using a while loop.
    Continues prompting until a valid file is provided or user skips.
    
    Returns:
        str: The filename or empty string to use sample text
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        filename = input("\nEnter the path to the news article file (or press Enter to use sample text): ").strip()
        
        # Conditional: Check if user wants to skip
        if not filename:
            print("Using sample news article text.")
            return ""
        
        # Conditional: Check if file exists and is readable
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Try to read a small portion to verify it's readable
                file.read(100)
            print(f"File '{filename}' found and is readable.")
            return filename
        except FileNotFoundError:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"File not found. You have {remaining} attempt(s) remaining.")
            else:
                print("Maximum attempts reached. Using sample text instead.")
                return ""
        except Exception as e:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Error reading file: {e}. You have {remaining} attempt(s) remaining.")
            else:
                print("Maximum attempts reached. Using sample text instead.")
                return ""
    
    return ""


def get_search_word():
    """
    Get a search word from the user with validation using a while loop.
    
    Returns:
        str: The search word (validated to contain only letters)
    """
    while True:
        search_word = input("\nEnter a word to count (letters only, or press Enter to use 'artificial'): ").strip()
        
        # Conditional: Check if user pressed Enter
        if not search_word:
            search_word = "artificial"
            print(f"Using default search word: '{search_word}'")
            return search_word
        
        # Conditional: Validate that the word contains only letters
        if re.match(r'^[a-zA-Z]+$', search_word):
            return search_word
        else:
            print("Invalid input. Please enter a word containing only letters.")


def display_analysis_results(text, search_word=None):
    """
    Perform all text analysis tasks and display the results.
    
    Args:
        text (str): The text to analyze
        search_word (str): Optional word to search for
    """
    print("\n" + "=" * 60)
    print("TEXT ANALYSIS RESULTS")
    print("=" * 60)
    
    # Task 1: Count specific word (with conditional)
    if search_word:
        word_count = count_specific_word(text, search_word)
        print(f"\n1. Count of '{search_word}': {word_count}")
        
        # Conditional: Provide feedback based on count
        if word_count == 0:
            print("   Note: The word was not found in the text.")
        elif word_count == 1:
            print("   Note: The word appears once in the text.")
        else:
            print(f"   Note: The word appears multiple times in the text.")
    else:
        print("\n1. No specific word provided for counting.")
    
    # Task 2: Most common word (with conditional)
    most_common = identify_most_common_word(text)
    if most_common:
        print(f"\n2. Most common word: '{most_common}'")
    else:
        print("\n2. Most common word: None (text is empty)")
    
    # Task 3: Average word length (with conditional)
    avg_length = calculate_average_word_length(text)
    print(f"\n3. Average word length: {avg_length:.2f} characters")
    
    # Conditional: Provide interpretation
    if avg_length == 0:
        print("   Note: No valid words found in the text.")
    elif avg_length < 4:
        print("   Note: Text uses relatively short words.")
    elif avg_length < 6:
        print("   Note: Text uses medium-length words.")
    else:
        print("   Note: Text uses relatively long words.")
    
    # Task 4: Paragraph count (with conditional)
    paragraph_count = count_paragraphs(text)
    print(f"\n4. Number of paragraphs: {paragraph_count}")
    
    # Conditional: Provide feedback
    if paragraph_count == 1:
        print("   Note: The text consists of a single paragraph.")
    else:
        print(f"   Note: The text is organized into {paragraph_count} paragraphs.")
    
    # Task 5: Sentence count (with conditional)
    sentence_count = count_sentences(text)
    print(f"\n5. Number of sentences: {sentence_count}")
    
    # Conditional: Provide feedback
    if sentence_count == 1:
        print("   Note: The text contains a single sentence.")
    elif sentence_count < 5:
        print("   Note: The text is relatively brief.")
    else:
        print(f"   Note: The text contains multiple sentences.")
    
    print("\n" + "=" * 60)


def main():
    """
    Main function to run the text analysis program.
    Uses while loop for menu-driven interaction.
    """
    print("=" * 60)
    print("NEWS ARTICLE TEXT ANALYSIS TOOL")
    print("=" * 60)
    
    # While loop for continuous operation
    continue_analysis = True
    
    while continue_analysis:
        print("\n" + "-" * 60)
        
        # Get filename with validation (uses while loop internally)
        filename = get_valid_filename()
        
        # Conditional: Determine whether to read from file or use sample text
        if filename:
            article_text = read_article_from_file(filename)
            # Conditional: Check if file reading was successful
            if not article_text:
                print("Unable to read file content. Using sample text instead.")
                filename = ""
        
        # Conditional: Use sample text if no valid file
        if not filename:
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
        
        # Get search word with validation (uses while loop internally)
        search_word = get_search_word()
        
        # Perform analysis and display results
        display_analysis_results(article_text, search_word)
        
        # While loop control: Ask if user wants to analyze another article
        while True:
            choice = input("\nWould you like to analyze another article? (yes/no): ").strip().lower()
            
            # Conditional: Validate user input
            if choice in ['yes', 'y']:
                continue_analysis = True
                break
            elif choice in ['no', 'n']:
                continue_analysis = False
                print("\nThank you for using the News Article Text Analysis Tool!")
                print("=" * 60)
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    

if __name__ == "__main__":
    main()