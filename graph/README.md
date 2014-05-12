### Before

 * Read this post on [Graphs and their Representation](http://www.stoimen.com/blog/2012/08/31/computer-algorithms-graphs-and-their-representation/) to pick up some terms and the common methods for representating graphs.

Optional:

 * Read this brief [essay](https://www.python.org/doc/essays/graphs/) with a simple graph representation and algorithm implementations in Python.
 * Read [Graph-based Features for Supervised Link Prediction](http://www.kaggle.com/blobs/download/forum-message-attachment-files/183/supervised_link_prediction.pdf), a paper on extracting features from graphs for predictive modeling, for a particular example.


### Questions

 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Application presentation.

Question review.

[Slides](slides.pdf) on graphs.

Many things can be viewed as graphs even if they aren't obviously graphs to begin with. The transformation is in determining what a node is and what it means to be connected. A not uncommon way to do this is to use co-occurence of words. You could check out a [simple example](http://planspace.org/2013/01/30/visualize-co_occurrence/) using the `igraph` package in `R`.

In Python the go-to for graphs is [networkx](http://networkx.github.io/). They have a [tutorial](networkx.github.io/documentation/latest/tutorial/) to get you started.

Super-mini `networkx` demo:

```Python
import networkx as nx
g = nx.florentine_families_graph()
sorted(nx.eigenvector_centrality(g).items(), key=lambda x: x[1])
```

Graph visualization can be difficult in part because graphs don't have any terribly natural layout or orientation. [Gephi](https://gephi.org/) is a point-and-click application useful for working with graphs in an interactive manner. It describes itself as "Like Photoshop™ for graphs.".

An easy way to get a graph into Gephi is to create CSV files for the nodes and edges. It's easiest if you follow Gephi's conventions for the column names:

 * nodes file: `Id` and `label` will correspond to how nodes are referred to in the edges file and what is displayed in the visualization when labels are turned on. (Possibly the same thing.) Additional columns can be used to control visual properties of the nodes, as adjusted in the UI.
 * edges file: `source` and `target` refer to node IDs from the nodes file. They edges are directed unless there is a column `type` with values `undirected`. `weight` will be automatically used for edge weights. Additional columns can also be included.


### After

Optional:

 * For a very gentle and traditional introduction to graphs, check out this [chapter](http://www.mhhe.com/math/ltbmath/bennett_nelson/conceptual/netgraphs/graphs.htm) featuring [Pólya-style](http://en.wikipedia.org/wiki/How_to_Solve_It) exercises.
 * For a little more mathematics in connection with network graphs, see [The mathematics of networks](http://www-personal.umich.edu/~mejn/papers/palgrave.pdf).
 * Check out some of the things [Wolfram](http://www.wolframalpha.com/facebook/) does with Facebook data: [Data Science of the Facebook World](http://blog.stephenwolfram.com/2013/04/data-science-of-the-facebook-world/).
 * Read a Facebook/academic paper on [The Role of Social Networks in Information Diffusion](http://arxiv.org/abs/1201.4145).
 * A fairly interesting read showing how network data can become a story: [When Your Twitter Friend Turns Out To Be The Boston Bomber](http://digg.com/originals/dzhokhar-tsarnaev-twitter-map).
 * The [book](http://www.cambridge.org/us/academic/subjects/computer-science/algorithmics-complexity-computer-algebra-and-computational-g/networks-crowds-and-markets-reasoning-about-highly-connected-world) _Networks, Crowds, and Markets: Reasoning About a Highly Connected World_ is available [online](http://www.cs.cornell.edu/home/kleinber/networks-book/).
