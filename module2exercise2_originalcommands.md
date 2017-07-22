# HIST 3814O
## July 20 2017
### Module 2 Exercise 2 command history

Followed [Ian Milligan's Automated Downloading with Wget tutorial @ The Programming Historian](http://www.programminghistorian.org/lessons/automated-downloading-with-wget).

    1  mkdir wget-activehistory
    2  cd wget-activehistory
    3  wget http://www.activehistory.ca/papers/
    4  wget -r -np -w 2 -limit-rate=20k http://activehistory.ca/papers/
    5  wget -r -np -w 2 --limit-rate=20k http://activehistory.ca/papers/
    6  history > module2exercise2_commands.md
