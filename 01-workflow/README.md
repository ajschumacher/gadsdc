### Before

Optional:

* Read this paper. It was one of the best from [KDD](http://www.kdd.org/) 2013. "[Amplifying the Voice of Youth in Africa via Text Analytics](http://www.prem-melville.com/publications/unicef-kdd2013.pdf)" You don't have to follow everything in the paper, but it does give a nice overview of a complete "data science" process, including data architecture, modeling, evaluation, and application.


### Questions

 * How do you relate to Conway's [data science Venn diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)? What related skills and training do you have? What fields/topics do you know? What are you interested in learning more about?
 * How do you currently organize your work? Do you use any systems, conventions, or organizational tools? What is useful to you? Have you used any version control systems?
 * What ideas or thoughts do you have about your class project? Have you started thinking about it yet?
 * What other thoughts, comments, concerns, and questions do you have? What's on your mind?


### During

Email instructors.

An example of an analysis using version control data
 * "Collaboration in the open-source arena: The WebKit case" [[arXiv]](http://arxiv.org/abs/1401.5996) [[PDF]](http://arxiv.org/pdf/1401.5996v1.pdf) [[more]](http://users.utu.fi/joante/WebKitSNA/)

Application Presentations assigned and scheduled.

Setting up a machine on [AWS EC2](http://aws.amazon.com/ec2/) and getting set up with [git](http://git-scm.com/) and [github](https://github.com/). These blog posts describe much of the process demonstrated in class:

 * [Easy AWS EC2 Ubuntu Quick Start](http://planspace.org/2014/01/25/easy-aws-ec2-ubuntu-quick-start/)
 * [A shared playground on Ubuntu](http://planspace.org/2014/02/15/a-shared-playground-on-ubuntu/)
 * [Set up git/hub on Ubuntu](http://planspace.org/2014/02/16/set-up-github-on-ubuntu/)

Please never put spaces in filenames.

Please always end files with a newline.

You should know these: `pwd`, `ls`, `cd`, `cp`, `mv`, `rm`, `hostname`, `whoami`, `passwd`, `ssh`, `env`, `export`.

On Ubuntu, `apt-get install` things you want.

Learn some `readline`/`emacs` [keyboard navigation shortcuts](http://www.catonmat.net/download/readline-emacs-editing-mode-cheat-sheet.pdf).

You should know at least one command-line text editor. When in doubt, you can usually fall back on `nano`. In some cases `vi` is the only thing available, so at least know how to get out by hitting `esc` and then entering `q!`. People generally develop proficiency in at least one of `vim` or `emacs`. There's nothing wrong with using a GUI editor such as [Sublime Text](http://www.sublimetext.com/), [TextWrangler](http://www.barebones.com/products/textwrangler/), [TextMate](http://macromates.com/), or [Notepad++](http://notepad-plus-plus.org/) as well.

For `git`: `git init`, `git status`, `git add`, `git commit`, `git push`, `git clone`, `git pull`, `git log`, etc.

On github, be able to fork and submit pull requests.

More command-line tools: `man`, `time`, `wget`, `curl`, [`tmux`](http://robots.thoughtbot.com/a-tmux-crash-course), `echo`, `cat`, `diff`, `tr`, `sort`, `wc`, `more`, `less`, `head`, `tail`, `cut`, `uniq`, `join`, `grep`, `bc`.

[Command-Line Data Manipulation](http://planspace.org/2013/05/21/command-line-data-manipulation/)

Just enough `sed` and regular expressions to know what they are:

    cat file.txt | sed 's/^/ * /'

You'll need to know some [markdown](https://daringfireball.net/projects/markdown/syntax), and [github-flavored markdown](https://help.github.com/articles/github-flavored-markdown) is often handy too. This [live markdown editor](http://jrmoran.com/playground/markdown-live-editor/) can be useful.

Play with git logs to do a simple analysis of open source projects.


### After

 * If you don't have them already, make a [twitter](https://twitter.com/) account and a [blog](http://sixrevisions.com/tools/top-free-online-blogging/). Communication is a good thing!
 * In your fork of the class repository, in the `01-workflow` directory, make a file named `yourname.md` containing links to your twitter account and blog. Commit, push to github, and submit a pull request to get your file in the class repository.

Optional:
 * Make your own EC2 micro Ubuntu instance and set it up a little.
 * Do the `emacs` tutorial. In `emacs`, press `control` and `h`, then press `t`.
 * Learn more about `sed` and `awk`.
 * Read this chapter from the Bad Data Handbook: "Myths of cloud computing"
