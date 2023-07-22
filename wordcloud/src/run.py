file_path = 'src/data/movies.txt'
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
class wordcloudgenerator():
    def __init__(self, file_path):
        with open(file_path) as f:
            self.text = f.read()
    def run(self, output_path):
        wordcloud = WordCloud( 
        background_color='white',max_words=100).generate(self.text)  
        plt.imshow(wordcloud)
        plt.axis('on') 
        plt.show()
        wordcloud.to_file(output_path)        
if __name__ == '__main__':
    c =wordcloudgenerator(file_path)
    c.run('./output.png')        