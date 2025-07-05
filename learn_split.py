def split_by_comma():
    input_str = '1,2,3,4,5'
    split_results = input_str.split(',')
    print(split_results)



def sentence_reverser():
    input_sentence = input('Enter a sentence: ')
    split_input = input_sentence.split()
    list_ending_value_index = len(split_input) - 1
    for i in range(len(split_input) - 1, -1, -1):
        print(split_input[i], end=' ')


def repeating_word_finder():
    jack_counter = 0
    input_story = 'Jack was a curious boy who loved robots. One day, Jack found a dusty toolbox in his attic. Jack used it to build a tiny robot friend named Spark. Every night, Jack and Spark would stargaze and dream of space adventures. Jack knew one day, he and Spark would fly to the stars.'.lower()
    split_input = input_story.split()
    for i in range(len(split_input)):
        if split_input[i] == 'jack':
            jack_counter = jack_counter + 1
    print(jack_counter)

def repeating_word_finder_advanced():
    jack_counter = 0
    input_story = input('Enter a story (3-4 lines) ').lower()
    word_to_find = input('What word would you like to find in your story? ').lower()
    word_is_valid = word_to_find.split()
    
    if len(word_is_valid) == 1: 
        split_input = input_story.split()
        for i in range(len(split_input)):
            if split_input[i] == word_to_find:
                jack_counter = jack_counter + 1
        print(jack_counter)
    else:
        print('You can only find one word!')
    
repeating_word_finder_advanced()








 