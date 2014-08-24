The Python Natural Language ToolKit ([nltk](http://www.nltk.org/)) has a lot of functionality, including [stemming](http://en.wikipedia.org/wiki/Stemming). This also illustrates a common pattern of instantiating and then using objects in Python.

```Python
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("managers")
stemmer.stem("management")
# etc.
```
