def calculate_probability(text):
    words =text.lower().split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word,0)+1

    total_words =sum(frequencies.values())
    probabilities = {}
    for word, count in frequencies.items():
        probabilities[word] = count /total_words
    return probabilities , total_words

simple_text = "secret code secret money secret link win money "
word_porbs, total =calculate_probability(simple_text)

print(f"Total tokens in corpus: {total}\n")
print(f"{'Word':<12} | {'Count':<6} | {'Probability P(word)':<18}")
print("-" * 42)

words = simple_text.lower().split()
for word, porb in word_porbs.items():
    raw_count =word.count(word)
    print(f"{word:<12} | {raw_count:<6} | {porb:.4f}")
    print(f"\nProbability of missing word 'apple': {word_porbs.get('apple', 0.0)}")