import random
count = 0

def word_list():
    words= open('eldrow_words.txt', 'r').read().splitlines()
    secret_word = random.choice(words)
    return(secret_word)

def main(count):
    if count < 6:
        guess = input('Enter guess: ')
        eval_guess(guess, secret_word, count)
    elif count == 6:
        print('sorry')
        print('The secret word was: ', secret_word)
        pass
        

def summary(eval_string):
    summ = []
    summ.append(eval_string)
    return(summ)

def eval_guess(guess, secret_word, count):
    in_word=[]
    out_of_place=[]
    not_in_word = []
    eval_string = ''
    let_pos = 0
    arr= []

    for letter in guess:
        if letter not in secret_word:
            eval_string+='X'
            not_in_word.append(letter.upper())

        else:
            if guess[let_pos] == secret_word[let_pos]:
                eval_string +='$'
                in_word.append(letter.upper())

            else:
                eval_string+='>'
                out_of_place.append(letter.upper())

        let_pos+=1
    if eval_string == 'X':
        not_in_word.append(letter)
    if guess != secret_word:

        i = 0
        while i < len(guess):
            print(guess[i].upper(), '', end = '')
            i+=1
        print()

        
        i = 0
        while i < len(eval_string):
            
            print(eval_string[i], '', end='')
            i+=1
        print()

        
        
        
     
        

        
        
        print('Correct:', *in_word)
        print('Out of place:', *out_of_place)
        print('Not in word:', *not_in_word)
        count+=1
        
        arr=summary(eval_string)
        main(count)
        print(arr)
        
    elif guess == secret_word:
        print('Good job')


secret_word = word_list()
main(count)
