# A combinatoric intro to `ggplot`

You'll need `library(ggplot2)`. `ggplot` implements Leland Wilkinson's "grammar of graphics" for `R`. Documentation with examples is [available](http://docs.ggplot2.org/) as well.

---

For demonstration, this example data will be used:

    data(iris)

Take a look at the structure of the data. `Species` is a factor, everything else is numeric.

    str(iris)

---

Change the following with the pieces further below:

    ggplot(data = iris) + aes(x = Petal.Length) + geom_histogram()

Combine one `ggplot` call, one or more `aes` calls each with your choice of variable, probably one `geom` call, and so on!

`ggplot` call gets you started:

    ggplot(data = iris)

`aes`thetics attach data to dimensions:

    aes(x = Petal.Length)    # the x axis
    aes(y = Petal.Width)     # the y axis
    aes(color = Species)     # color (of outlines)
    aes(fill = Species)      # color (of interiors)
    aes(shape = Species)     # shape (of points)
    aes(size = Sepal.Length) # size (of points, usually)
    aes(alpha = Sepal.Width) # 'alpha' (transparency)
    aes(group = Species)     # may not be useful here

`geom` specifies what to draw. These ones require at least x:

    geom_histogram()
    geom_density()
    geom_dotplot()

Try these with a factor (like Species) on x and a numeric on y

    geom_boxplot()
    geom_violin()

These ones require at least x and y:

    geom_point()
    geom_bin2d()
    geom_hex()

This one's fairly flexible:

    geom_line()

Add these with other geoms, especially `point`:

    geom_smooth()
    geom_rug()
    geom_jitter()

small multiples, vertical or horizontal:

    facet_grid(Species ~ .)
    facet_grid(. ~ Species)

add some labels:

    ggtitle("Title of the Plot")
    xlab("x axis label")
    ylab("y axis label")

sometimes fun:

    coord_flip()

add a theme, if you want:
    theme_bw()
    theme_classic()

check the help for further customization:

    ?theme


You might like variants on this:

    scale_fill_manual(values=c("red","green","orange"))


Don't forget about all the documentation for ggplot2 [here](http://docs.ggplot2.org/):

    browseURL("http://docs.ggplot2.org/")
