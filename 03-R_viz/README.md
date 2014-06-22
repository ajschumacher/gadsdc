### Before

 * Read [That's Funny... A window on data can be a window on discovery](http://www.americanscientist.org/issues/pub/2009/4/thats-funny).
 * Read [The Gospel According to Tufte](http://www-personal.umich.edu/~jpboyd/eng403_chap2_tuftegospel.pdf), which is the best freely available summary of Tufte that I've been able to find.

Optional:

 * This [introduction to `ggplot`](http://www.ling.upenn.edu/~joseff/avml2012/) is fairly good, and follows nicely the theory about visualization from above.
 * Watch this presentation about [looking at your data](http://www.youtube.com/watch?v=coNDCIMH8bk).
 * Read this chapter from the Bad Data Handbook: "Is it just me, or does this data smell funny?"
 * These [slides](http://faculty.ucr.edu/~tgirke/HTML_Presentations/Manuals/Rgraphics/Rgraphics.pdf) include some good examples of the graphics functions we'll use, and more.
 * If you're interested in thinking about interactive/visualizations as a genre you might check out [Narrative Visualization: Telling Stories with Data
](http://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf).


### Questions

 * Some people think Tufte is too restrictive, or that he doesn't appreciate creative, eye-catching images. What do you think? What is your opinion of infographics?
 * Are there any visualizations that have particularly caught your interest? (Share a link or two if you can!) What was it about them that made them good/bad?
 * What tools have you previously used for producing images, statistical or otherwise? What are their strengths and weaknesses?
 * Does your application presentation topic connect in any way with ideas for your class project?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

Brief [slides](slides.pdf).

Summary statistics discussed:
 * mean (as one of the averages or measures of center)
 * variance (as covariance with self)
 * (Pearson's) correlation (as measure of varying together linearly)
 * (This leads into linear regression, which will be left until later.)

Slides at "Visualization as a medium":

Take a look at the Juice Labs [Chart Chooser](http://labs.juiceanalytics.com/chartchooser/) and gallery. Perhaps also [wtf-viz](http://wtfviz.net/).

Doing graphics with `R`:

`R` base graphics: `plot`, `plot(sort())`, (`abline`, `points`, `text`, ...), `hist`, `boxplot`, `barplot`, `dotchart`, (`image`, `contour`, `persp`), `pairs`, (`qqnorm`, `qqplot`), and `par`. (Use the help, and use the examples.)

Quantile plots can sometimes show more useful detail about data than a histogram. [[comparison example]](http://planspacedotorg.files.wordpress.com/2014/01/hist_vs_quantile.png) [[example from Washington Post]](http://apps.washingtonpost.com/g/page/national/715-new-exoplanets/841/)

The [mean-difference plot](http://en.wikipedia.org/wiki/Bland%E2%80%93Altman_plot) and the related percent-total plot are useful in analyzing agreement of measures or changes that are small - that is, when a scatterplot is not very helpful. For example: [scatterplots](http://planspace.org/2013/11/14/nyc-standardized-test-results-checking-out-the-number-of-students-tested-in-math-and-ela/) vs. [these alternatives](http://planspace.org/2013/11/15/nyc-standardized-test-results-checking-out-the-number-of-students-tested-in-math-and-ela-again/).

Introduce `knitr` and [RPubs](http://rpubs.com/):
 * `install.packages("knitr")`
 * Make a new `R Markdown` document in RStudio. Click `Knit HTML`. You're done!
 * [More introduction to `knitr` (with a video!)](http://yihui.name/knitr/)
 * [`knitr` chunk options](http://yihui.name/knitr/options)

Compare [three `R` graphics systems](three_systems.Rmd).

Experiment with the [combinatoric intro to `ggplot`](ggplot.md).

Write graphics to disk with `png()` and friends, followed by `dev.off()`.

Make a lot of visualizations of your data. Choose one. Post a `knitr` Rmarkdown document to RPubs. Post your viz and RPub on twitter, and call out @GA_DC.

Some presentations.


### After

Optional:

 * To keep practicing `R` and make sure you're confident with mean, covariance, and correlation, implement functions for these yourself and check that they give the same results as the ones in base `R`. (Does `R` give sample or population variance?) You can put a `name.R` file in the `03-R_viz` directory of the class repo.
 * You should really go to the source on Tufte, but that means you need to get his books. Start with [The Visual Display of Quantitative Information](http://www.amazon.com/The-Visual-Display-Quantitative-Information/dp/0961392142). I also especially like Tufte on PowerPoint, which you might even be able to find online.
 * On a similar level to Tufte, with more focus on scientific graphics, check out William Cleveland's books, e.g., [Visualizing Data](http://www.amazon.com/Visualizing-Data-William-S-Cleveland/dp/0963488406/).
 * If you've read Tufte and Cleveland, perhaps check out [Stephen Few](http://www.amazon.com/Stephen-Few/e/B001H6IQ5M).
 * This is a nice collection of [slope graphs](http://charliepark.org/slopegraphs/).
