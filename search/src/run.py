from pathlib import Path
from nlp.text_process import (ConvertCase,RemoveDigit,RemovePunkt,RemoveSpace,TextPipeline) 
class search():
    def __init__(self, path_doc,stop_word=None):
        self.data = self.crawling(path_doc)
        self.pipe = TextPipeline(ConvertCase(), RemoveDigit(), RemovePunkt(), RemoveSpace())
        if stop_word == None:
            with open('src/data/stop_words.txt') as g:
                stop_word = set(g.read().split('\n'))
                stop_word = list(map(self.pipe.transform ,stop_word))     
        self.stop_word = stop_word
        self.index = self.index_data()



    def crawling(self,path_doc):
        data = {}
        for doc_path in Path(path_doc).iterdir():
            if doc_path.suffix != '.txt':
                continue
            with open(doc_path) as f:
                doc_name = doc_path.stem.replace('-','').title()
                data[doc_name] = f.read()
        return data  


    def index_data(self):
        index = {}
        for doc_name, doc_content in self.data.items():
            words = doc_content.split()
            for word in words:
                word = self.pipe.transform(word)
                if word in self.stop_word:
                    continue
                elif word in index:
                    index[word].add(doc_name)
                else:
                    index[word] = {doc_name}     
        return index


    def search_data(self, query):
        docs = []
        query = self.pipe.transform(query)
        search_tokens = query.split()
        for word in search_tokens:
            docs.extend(self.index.get(word,[]))
        return docs


if __name__ == '__main__':
    searcher = search('src/data/documents')   
    while True:
        search_input = input('enter your search (enter exit for exit)=')  
        if search_input == 'exit':
            break
        print(searcher.search_data(search_input))
        