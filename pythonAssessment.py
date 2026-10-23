import re
from collections import Counter
from pathlib import Path

FILE_PATH = Path("article.txt").parent / "article.txt"

def read_text_file(path):
    try:
        return path.read_text()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return ""

def count_specific_word(text: str, target_word: str) -> int:
    if not text or not target_word:
        return 0
    
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(target_word.lower())

def identify_most_common_word(text: str):
    if not text.strip():
        return None
    
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

def calculate_average_word_length(text: str) -> float:
    if not text.strip():
        return 0.0
    
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0.0
    
    total_letters = sum(len(word) for word in words)
    return total_letters / len(words)

def count_paragraphs(text: str) -> int:
    if not text.strip():
        return 1
    
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text: str) -> int:
    if not text.strip():
        return 1

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])+", text) if s.strip()]
    return len(sentences) if sentences else 1


def main():
    article_text = read_text_file(FILE_PATH)

    if not article_text:
        print("Warning: Article text is empty. Testing edge cases.")

    paragraphs = count_paragraphs(article_text)
    sentences = count_sentences(article_text)
    avg_length = calculate_average_word_length(article_text)
    common_word = identify_most_common_word(article_text)
    target = "the"
    specific_word_count = count_specific_word(article_text, target)

    print("--- Assessment Analysis Results ---")
    print(f"Paragraph Count:         {paragraphs}")
    print(f"Sentence Count:          {sentences}")
    print(f"Average Word Length:     {avg_length:.2f} characters")
    print(f"Most Common Word:        '{common_word}'")
    print(f"Count for word '{target}':  {specific_word_count}")


if __name__ == "__main__":
    main()