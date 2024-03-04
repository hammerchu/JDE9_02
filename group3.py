def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word and join them back
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Example usage:
input_sentence = "I am a boy"
reversed_result = reverse_words(input_sentence)
print(f"Reversed sentence: {reversed_result}")

   
    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
