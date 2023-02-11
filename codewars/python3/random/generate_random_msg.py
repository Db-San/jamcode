import random

word_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
sentence = " ".join(random.sample(word_list, len(word_list)))
print(sentence.capitalize() + ".")
