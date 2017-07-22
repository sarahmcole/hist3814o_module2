# HIST3814O MODULE 2 EXERCISE 2
## July 20 2017

Here are the commands I made while following [Ian Milligan's Automated Downloading with Wget tutorial @ The Programming Historian](http://www.theprogramminghistorian.org/lessons/automated-downloading-with-wget).

    1  mkdir wget-activehistory
    2  cd wget-activehistory
    3  wget http://www.activehistory.ca/papers/
    4  wget -r -np -w 2 -limit-rate=20k http://activehistory.ca/papers/
    5  wget -r -np -w 2 --limit-rate=20k http://activehistory.ca/papers/
    6  history > module2exercise2_commands.md
    7  nano module2exercise2_commands.md

Here is where I fly too close to the sun in trying to push module2exercise2_commands.md to a github repo, /hist3814o_module2/.

    8  git remote add module2 http://github.com/sarahmcole/hist3814o_module2/
    9  git push module2 module2exercise2_commands.md
   10  cd hist3814o_module2
   11  cd origin
   12  cd sarahmcole
   13  cd
   14  mkdir hist3814o_module2
   15  cd hist3814o_module2
   16  cd wget_activehistory
   17  cd wget-activehistory
   18  cd/
   19  cd
   20  cd wget-activehistory

Here is me thinking the mv command is actually move:

   21  move hist3814o_module2 module2exercise2_commands.md
   22  move mo
   23  move
   24  move module2exercise2_commands.md hist3814o_module2
   25  cd hist3814o_module2
   26  cd
   27  cd hist3814o_module2
   28  gi
   29  git init
   30  cd
   31  cd wget-activehistory

here is me getting the mv command right, but not realizing that it just renamed module2exercise2_commands.md to hist3814o_module2:

   32  mv module2exercise2_commands.md hist3814o_module2
   33  cd
   34  cd modu
   35  cd hist3814o_module2
   36  ls
   37  cdcd
   38  cd
   39  cd wget-activehistory
   40  ls

here is where I thought I had lost module2exercise2_commands.md and make a new history file:

   41  history
   42  history > module2exercise2_commands.md
   43  nano module2exercise2_commands.md

here is where I realize the original module2exercise2_commands.md was never lost after all, so I rename it to module2exercise2_originalcommands.md and make this new command history.

   44  nano hist3814o_module2
   45  mv hist3814o_module2 module2exercise2_originalcommands.md
   46  history > module2exercise2_newcommands.md
