# Web Scraping with Python

+![python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)


## Lesson Objectives
- Learn about Python as a programming language
- Practice writing Python code (data types)
- Understand the process of web scraping
- Use BeautifulSoup library to scrape GA Profiles
- Stretch: Scrape weather info + plot a graph


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

Q: Why Python?
- Python was implemented in 1989 in the Netherlands with the core philosophy that:
  - Beautiful is better than ugly
  - Explicit is better than implicit
  - Simple is better than complex
  - Complex is better than complicated
  - Readability counts
- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
- Python is whitespace deliminated.
- Python is an accessible language for new programmers, with easy to learn syntax
- Open source modules and big libraries hook very easily into the C language. Python is a layer on top of C.
- As a multipurpose language, it can be used for small, big, online, offline projects, and are largely used in web development, simple scripting, and data analysis
- So, Python is *less verbose* and allows for *faster development cycles*

[Python + Data: Quora](https://www.quora.com/Why-is-Python-a-language-of-choice-for-data-scientists)

## Installing Python
The latest version of Mac OS X, El Capitan, comes with Python 2.7 installed already.
The newest version of Python is Python3, but we will use Python 2.x.

#### Installing with Homebrew
We will be installing our own version of Python 2.7:
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

Beautiful Soup transforms a complex HTML document into a complex tree of Python objects:
- Tag
- NavigableString
- BeautifulSoup
- Comment

```
$ pip install beautifulsoup4
-> Successfully installed beautifulsoup4-4.5.1
```

[BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Python Data Types:
Run `python` in terminal for python shell

#### Variables + Multiple Assignments
Python variables do not need explicit declaration. You can simple assign a value to a variable:

```
x = 1
x = "Yams"
x = [1,2,3]

a = b = c = 1
```

Python has 5 standard data types:

#### Numbers (int, long, float, complex)
```
int_num = -9888
long_num = 0xDEFABCECBDAECBFBAEl
float_num = 0.0
complex_num = .876j
```

#### Lists

```
my_list = [1, 2, 3, 4, 5, "a"]
```

#### Tuples
Tuples are faster and consume less memory than lists.
Tuples are immutable (think: "Read Only")

```
t = (1, 2, 3, 4, 5, "a")
```

#### Dictionaries
```
dict = {}
dict['pie'] = "apple"
dict[2] = "two"

my_dict = {"a":1, "b":2, "c":3}

dict.keys()     # prints all keys
dict.values()   # prints all values
```

#### Strings
```
favorite_food = "tacos"
print favorite_food         # returns "tacos"
print favorite_food[0]      # returns "t"
print favorite_food[2:5]    # returns "cos"
print favorite_food * 2     # returns "tacostacos"
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

### :neckbeard: You Do!

```
fresh_prince = ["Will Smith", "Philip", "Carlton", "Hilary", "Jazz", "Geoffrey"]
```

Using the `fresh_prince` list, access:

1. "Philip"
2. ["Hilary", "Jazz", "Geoffrey"]
3. ["Will Smith", "Philip", "Carlton"]
4. ["Philip", "Carlton", "Hilary", "Jazz", "Geoffrey"]
5. Remove "Geoffrey" (hint: `.pop()`?)
6. Add "Nicky" to the end (hint: `.append()`?)


#### length
```
len(fresh_prince)       # returns 6
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

### :neckbeard: You Do!

Exercise 2: Create a calculator function:

1. `bad_calc` will take 2 arguments, `num1` and `num2`
2. If they're both even, print the product (multiply them)
3. If they're both odd, print the sum (add them)
4. If they're neither, print the numbers

Exercise 3: Zpelling
```
zpecial = ["zoup", "soccer", "zkillz", "zelf", "javascript"]
```

1. Write a for loop to loop through `zpecial`.
2. If the word contains a 'z', print the new word.
3. If there are no 'z's, print "not zpecial".



### Let's do some web scraping! (1 hr)

GA PROFILES EXERCISE:

- Find the first project in New York City
- Find all project titles in New York City
- Which are all the unique locations that projects have come from?
- How many are from each location?

#### Starter Code:

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

### More BeautifulSoup navigation methods
- `.children`
- `.contents`
- `.descendants`
- `.string`
- `.parent` / `.parents`
- `.next_sibling` / `.previous_sibling`

### Filters

#### String
```
soup.find_all('b')
# finds all the <b> tags in the document
```

#### Regular Expression
```
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b
```

#### Function
#### List
#### Keyword Arguments
```
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

#### CSS Class
```
soup.find_all("a", class_="sister")
```
