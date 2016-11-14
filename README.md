# Web Scraping with Python

## What is web scraping? (5 mins)
Web scraping is a technique for extracting large amounts of data from websites' source code (HTML). This data can be saved to a locally or to a database in table format.

1. Retrieve HTML data from a domain name
2. Parse the data for specific information
3. Store the target information

#### Data on the web

- A lot of sites don't have APIs, but the internet is the best place for information.
- Legal issues:
    - www.facebook.com/robots.txt
    - www.nytimes.com/robots.txt
    - www.generalassemb.ly/robots.txt

## Intro to Python (30 mins)
[Python 2x Documentation](https://docs.python.org/2/)

Q: Why is Python the language of choice for data scientists?
- Python is an interpreted, dynamically-typed language with a precise and efficient syntax.
- Python has a good REPL and new modules can be explored from the REPL with dir() and docstrings.
- Strong, core libraries (ie. NumPy, SciPy, pandas, matplotlib, IPython)
- Data analysis and modeling, and data manipulation

[Source: Quora](https://www.quora.com/Why-is-Python-a-language-of-choice-for-data-scientists)

## Installing Python
The latest version of Mac OS X, El Capitan, comes with Python 2.7 installed already.

#### Installing with Homebrew
Installing Python 2.7:
```
$ brew install python
```

```
$ python -V
-> Python 2.7.10
```

#### pip
Homebrew installs Setuptools and pip for you.
pip is a package management system for easily installing and managing Python packages

#### urllib module

[urllib Documentation](https://docs.python.org/2/library/urllib.html)

#### Beautiful Soup Library
Beautiful Soup is a Python library for pulling data out of HTML and XML files.

```
$ pip install beautifulsoup4
-> Successfully installed beautifulsoup4-4.5.1
```

[BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Python Data Structures:
Run `python` in terminal for python REPL

#### Lists

```
my_list = [1, 2, 3, 4, 5, "a"]
```

#### Tuples
Tuples are faster and consume less memory than lists.
```
t = (1, 2, 3, 4, 5, "a")
```

#### Dictionaries
```
dict = {"a":1, "b":2, "c":3}
```

#### Strings
```
favorite_food = "tacos"
```

#### Set + Frozen Set
```
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
a | b # Union
-> {1, 2, 3, 4, 5, 6}
```

### List Manipulations
```
galaxies = ["andromeda", "triangulum", "centaurus A", "bode's"]
```
#### accessing and slicing
```
galaxies[0]         # returns "andromeda"
galaxies[1:3]       # returns ['triangulum', 'centaurus A']
galaxies[2:]        # returns ['centaurus A', "bode's"]
galaxies[:2]        # returns ['andromeda', 'triangulum']
galaxies[2:-1]      # returns ['centaurus A']
```

#### length
```
len(galaxies)       # returns 4
```

#### Python functions
** Indentation and syntax MATTER! **
```
def say_hello(name):
    print "Hello " + name

# invoke the function:
say_hello("Mr. Robot")
```


#### for loops
```
junk_drawer = ['expired coupon', 'loose change', 'rubber band', 'lint']
for x in junk_drawer:
    print x

```

#### if statements

```
numbers = [1,2,3,4,5,6]
for number in numbers:
    if number % 2 == 0:
        print number
    else:
        print "odd!"

```

### Let's do some web scraping! (1 hr)

GA PROFILES EXERCISE:

- Find the first project in New York City
- Find all project titles in New York City
- Which are all the unique locations that projects have come from?
- How many are from each location?

```
from bs4 import BeautifulSoup
from urllib import urlopen

url = 'https://gallery.generalassemb.ly'
page_source = urlopen(url).read()
soup = BeautifulSoup(page_source, "html.parser")
soup
```

### Navigating soup
```
soup.title
-> <title>GA Gallery</title>

soup.title.string
-> u'GA Gallery'

soup.p
-> <p>ite-sized learning for all</p>

soup.find_all('a')
-> [<a href="/"><h2 class="brand">,
<a href="/login">Login</a>,
<a class="button small secondary href="/auth/generassembly">Login</a",
...]
```
