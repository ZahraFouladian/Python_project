from wordle.wordle import wordle
path = 'src/data/words_frequency.txt'
word_len = 5
limit = 1000
wordle = wordle(path,word_len,limit)
wordle.run()
