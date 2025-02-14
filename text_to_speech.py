from gtts import gTTS
from newspaper import Article as newsA


class ArticleHandler:
    def __init__(self, article_url):
        self.article_url = article_url
        self.chosen_article = ''

    def articleInit(self):
        self.chosen_article = newsA(self.article_url)
        self.chosen_article.download()
        self.chosen_article.parse()
        
    def convert_to_audio(self):
        content_to_convert = self.chosen_article.title + self.chosen_article.text
        article_to_audio = gTTS(content_to_convert, lang='en')
        article_to_audio.save(f'article_to_audio.mp3')

article_1 = ArticleHandler('https://abcnews.go.com/International/trump-putin-prepare-begin-ukraine-peace-talks-europe/story?id=118771634')
article_1.articleInit()
article_1.convert_to_audio()


