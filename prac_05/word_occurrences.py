"""
Word Occurrences
Estimate: 20 minutes
Actual:   11 minutes
"""

words = list(input("Text: ").split())
word_to_count = {}
for word in sorted(words):
    word_to_count[word] = word_to_count.get(word, 0) + 1
longest_word_length = max(len(word) for word in word_to_count.keys())
for word, count in word_to_count.items():
    print(f"{word:{longest_word_length}} : {count}")
