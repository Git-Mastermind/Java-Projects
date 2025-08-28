def cel_to_far():
    temp_c = [0,20,7,14,12]
    temp_f = list(map(lambda cel: (cel * 9/5) + 32, temp_c))
    print(temp_f)

def find_evens():
    nums = [0,1,2,3,4,5,6,7,8,9]
    evens = list(filter(lambda even: even % 2 == 0, nums))
    print(*evens)

def find_long_words():
    words = ['hi', 'hello', 'wazzup', 'hey', 'howyadoin']
    long_words = list(filter(lambda word: len(word) >= 4, words))
    print(*long_words)

