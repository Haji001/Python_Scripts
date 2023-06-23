import random
import string


noun_str = ['ball', 'house', 'cat',
            'elephan', 'dog', 'tree', 
            'chicken', 'car', 'ball']

adjectives_str = ['Big', 'tall', 'ugly',
                  'small', 'old', 'new',
                  'beautiful', 'unique', 'smart']


noun = random.choice(noun_str)
adjective = random.choice(adjectives_str)

number = random.randrange(0, 100)
spring_punctuation = random.choice(string.punctuation)

password = noun + adjective + str(number) + spring_punctuation
print(password)



while True:
    noun_str = ['ball', 'house', 'cat',
            'elephan', 'dog', 'tree', 
            'chicken', 'car', 'ball']

    adjectives_str = ['Big', 'tall', 'ugly',
                    'small', 'old', 'new',
                    'beautiful', 'unique', 'smart']


    noun = random.choice(noun_str)
    adjective = random.choice(adjectives_str)

    number = random.randrange(0, 100)
    spring_punctuation = random.choice(string.punctuation)

    password = noun + adjective + str(number) + spring_punctuation
    print(password)

    res = input("Want another password? Type Y or N\n")
    if res == 'N':
        break
    else:
        continue



