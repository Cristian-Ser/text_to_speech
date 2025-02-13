from gtts import gTTS
from newspaper import Article

def text_to_speech():
    # asking for the url of the article
    url = input('Introduce the URL of the article you want to turn into a speech')

    # initializing the article by itself with newspaper3k
    article = Article(url=url)
    
    # parsing the article (for that we have to download it first)
    article.download()
    article.parse()

    # now we select the content we are interested in. In this case: title and text
    title = article.title
    text = article.text

    


