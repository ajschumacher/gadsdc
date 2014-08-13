### Before

 * Read the Python Guide on [HTML Scraping](http://docs.python-guide.org/en/latest/scenarios/scrape/).
 * Read Scott Murray's [tutorial on D3](http://alignedleft.com/tutorials/d3/).

Optional:

 * Install a JSON viewer for your browser, such as [JSONview](http://jsonview.com/).
 * Read this chapter from the Bad Data Handbook: "Data intended for human consumption, not machine consumption"


### Questions

 * What data formats have you worked with? What are their strengths and weaknesses?
 * How can you get data? What data would you like to get for your final project? Where could you get it? Where have you looked?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.


#### Web Scraping

Play with basic [web scraping](scrape.py) using [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).

```bash
pip install beautifulsoup
pip install lxml
pip install cssselect
```


#### Web APIs

[Slides](slides.pdf) on data and formats.

[API lab](lab_API.md) on getting data from the web.

Exercise:

 * Pull some Sunlight API data into Python using `requests`.
 * Use the `json` library to `json.loads()` the Sunlight data into a Python data structure.
 * Re-structure the data into a list of lists or a `pandas` `DataFrame`.

One popular web API requiring OAuth is Twitter. You have to "create an application" through [dev.twitter.com](https://dev.twitter.com/) to get the required keys and tokens. Then after `pip install TwitterAPI` it's easy to access Twitter data through Python:

```Python
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret,
                 access_token_key, access_token_secret)
r = api.request('statuses/user_timeline',
                {'screen_name':'planarrowspace'})
tweets = [tweet for tweet in r]
for tweet in tweets:
    print tweet['text']
# etc.
```


#### Web visualization with D3

[D3](http://d3js.org/) is a much-loved JavaScript library for web-stack data visualization: Data Driven Documents. The library gives you a lot of control. D3 creator Mike Bostock's [Let's Make a Bar Chart](http://bost.ocks.org/mike/bar/) currently runs to three parts and is not yet complete. To fully take advantage of all the functionality of D3 requires some considerable familiarity with HTML, CSS, and JavaScript - but there are also a lot of examples that you can start from and modify!

Use the [d3.js bar chart generator](http://d3-generator.com/) to quickly get a bar chart made from some CSV data such as [lab_API-deficit.csv](lab_API-deficit.csv). This quickly gets you code that you can tweak in the browser.

Save the generated HTML to your computer and take advantage of Python's built-in web server:

```bash
python -m SimpleHTTPServer
```

View the page as served by Python.

Exercise:

 * Add an H1 header to the page.
 * Change the font face of the value labels with CSS.
 * Add commas to the axis labels.
 * Extract the CSV data to a separate file.
 * Extract the JavaScript to a separate file.
 * Add an animation ("transition").
 * Switch the chart from horizontal to vertical.


### After

Optional:

 * Read Tom Levine's scraping wisdom:
     * [Websites to data tables](http://dada.pink/dada/web-sites-to-data-tables/)
	 * [Websites to data tables, in depth](http://dada.pink/dada/web-sites-to-data-tables-in-depth/)
 * `scrapy` is a Python package for doing web scraping with a little bit bigger framework. Check out their [tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).
 * Check out [Crossfilter](http://square.github.io/crossfilter/), a
   fairly spectacular JavaScript library that lets you work with a lot
   of data in the browser and achieve neat interactive displays with
   scrubbing and so on. There's a nice
   [tutorial](http://blog.rusty.io/2012/09/17/crossfilter-tutorial/)
   that you might start with.
 * For more coding practice, you might check out one of [many coding competition sites/platforms](http://codecondo.com/coding-challenges).
