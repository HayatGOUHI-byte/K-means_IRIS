def my_bag_of_words(text, words_to_index, dict_size):
"""
    text: a string
    dict_size: size of the dictionary

    return a vector which is a bag-of-words representation of 'text'
"""


 Let say we have N = 4 and the list of the most popular words is 

['hi', 'you', 'me', 'are']

Then we need to numerate them, for example, like this: 

{'hi': 0, 'you': 1, 'me': 2, 'are': 3}

And we have the text, which we want to transform to the vector:
'hi how are you'

For this text we create a corresponding zero vector 
[0, 0, 0, 0]

And iterate over all words, and if the word is in the dictionary, we increase the value of the corresponding position in the vector:
'hi':  [1, 0, 0, 0]
'how': [1, 0, 0, 0] # word 'how' is not in our dictionary
'are': [1, 0, 0, 1]
'you': [1, 1, 0, 1]

The resulting vector will be 
[1, 1, 0, 1]