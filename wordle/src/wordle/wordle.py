from utilse import print_green,print_yellow,print_red
#-----------------------------------------------------------------------------------
class wordle():
    def __init__(self,path,word_len,limit):
        self.word_len = word_len
        self.limit = limit
        self.words =self.generate_word(path,word_len,limit)
        
# generate word 
#------------------------------------------------------------------------------------
    def generate_word(self,path,word_len,limit):
        words = []
        with open(path) as f:
            for line in f:
                line.strip()
                word, frequency = line.split(',')
                words.append((word, int(frequency)))        
#filter
        words = list(filter(lambda s : len(s[0])==word_len, words))
        words = sorted(words,key=lambda s: s[1], reverse=True)
#limit
        words = words[:limit]
                                                                                                                                                                                                                                                                                      #drop 
        words = [i[0] for i in words]
        return words
#------------------------------------------------------------------------------------    
    def run(self):
        word_set = set(self.words)
        import random
        word = random.choice(self.words)
        num_try = 1
        while True:
            guss_word = (input('please enter your word(or enter exit to cancel) =')).strip()
            guss_word = guss_word.lower()
            if guss_word == 'exit':
                break
            if len(guss_word) != self.word_len :
                print('your word must be have 5 letter')
                continue 
            
            for select_letter,guss_letter in zip(word,guss_word):
                if select_letter == guss_letter:
                    print_green(f' {guss_letter} ', end='')
                    print(' ',end='')
                elif guss_letter in word:
                    print_yellow(f' {guss_letter} ', end='')
                    print(' ', end='')
                else:
                    print_red(f' {guss_letter} ', end='')
                    print(' ', end='')
                    
                    
                    
            if guss_word == word:
                print('')
                print_green('*********congratulations***********')
                break
            else:
                chance = 5 - num_try
                num_try += 1 
                if num_try > 5:
                    print('')
                    print_red(f'*********sorry you can not guess********** \n************ the word is = {word}**********')
                    break
                else :
                    print('')
                    print_yellow(f'\n ********** You have {chance} chances to guess**********')
            