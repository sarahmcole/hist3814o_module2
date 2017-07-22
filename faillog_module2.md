# HIST3814O Fail log: module 2

## EXERCISE 1: THE DREAM CASE

+ I tried to search The Epigraphic Database for a few words before realizing I didn't know enough Latin to understand the epigraphs themselves, so I had better pick one keyword to look at and compare dates/locations.
+ Following Dr. Graham's advice, I searched for the one profession I know the Romans couldn't do without: "orator," or politician.
+ Initially I limited the search to the time period of the Roman Empire, but since I have trouble reading the Latin to do text-based analysis, I realized it might be interesting to compare the number of mentions of "orator" across a wider time period, so I removed that restriction.
+ FAIL? I uploaded the csv file to WTFcsv and got a bit of a [jumbled mess](https://databasic.io/en/wtfcsv/results/59709c157088b476a4c56c4e). I definitely don't know how to interpret these visualizations.
  + next steps: I will upload the results to the slack group to see if my classmates have any advice for using data from the Epigraphic Database.
+ I created a text file using nano called module2exercise1.txt documenting my search, the results, and where I am storing those results (github.com/sarahmcole/hit3814o_module2).
+ forgot AGAIN to export my command history before signing off.
  + next steps: I need to make a point to always save my command history.
  + question: could I (theoretically) write a program that prompts me to save my command history? perhaps not one that could run in DHbox, but if I created my own workspace, could I add a sort of semiautomated save or at least a reminder to save?

## EXERCISE 2: WGET

+ I followed [Ian Milligan's Automated Downloading with Wget tutorial at The Programming Historian](https://programminghistorian.org/lessons/automated-downloading-with-wget).
+ I managed to complete the tutorial AND remember to save my history as module2exercise2_commands.md!
+ Fail: I tried to lodge module2exercise2_commands.md in my hist3814o_module2 depository (which I added as a remote called `module2`) with this command: `git push module2 module2exercise2_commands.md`. This did not work.
  + Workaround attempt: I tried to make a git repository on my machine to then push to the remote on github. It didn't work; I think because I hadn't initialized a repo on my machine, so there were no tracked changes (such as the addition of a file) to "push." So, I created a new directory called `hist3814o_module2` and initialized it. Then I cd'd into the folder containing module2exercise2_commands.md and tried to move the .md file into /hist3814o_module2/ with this command:
`mv module2exercise2_commands.md hist3814o_module2`
I wound up renaming the file to hist3814o_module2! So I changed the name back, made an updated commands history, downloaded both and uploaded them to github through my browser. Follow the epic saga on the updated commands history.
+ I tried this command:`wget -r -np  -w 2 --limit-rate=20k -nd -A .txt http://collections.banq.qc.ca:8008/jrn03/equity/src/`
  + FAIL: I DID EXACTLY WHAT DR GRAHAM SAID NOT TO DO AND STARTED DOWNLOADING ALL OF IT... but nothing downloaded, because the .html files it tried to download first were rejected by my command. Phew.
+ I used the command `wget -r --no-parent -w 2 --limit-rate=20k -nd -A .txt http://collections.banq.qc.ca:8008/jrn03/equity/src/189*/`, changing the year 10 times to download all issues from the 1890s.
+ lost my internet connection again and was unable to export my history this time. sigh.

## EXERCISE 3: TEI
+ Followed exercise 3 to learn about the [Text Encoding Initiative](http://www.tei-c.org/index.xml).
+ I already had Notepad++ installed. Yay!
+ I transcribed page 93 of *Negro Slavery* by Zachary Macauley from [Recovered Histories](http://www.recoveredhistories.org/).
+ I used the [guidelines from TEI](http://www.tei-c.org/release/doc/tei-p5-doc/en/Guidelines.pdf) to encode italic emphasis
+ tried to open the xml file in firefox - FAIL! "XML Parsing Error: not well-formed"
  + error message says Number 56, so I know it's in line 56.
   + AHA: `<interp key="Until 1823, legal protections for slaves gained by the British anti-slavery movement were negligible." n="Morgan, Kenneth. Slavery in the British Empire: From Africa to America. New York: Oxford University Press, 2007. 170." cert="med" ref="http://lib.myilibrary.com/Open.aspx?id=134183">but they have been generally inefficient to their professed object, whatever other purpose they may have served.<interp>` I forgot the backslash to close my `<interp>` tag.
+ I LOVE THE FORMATTED TEXT OH MY GOD.

## EXERCISE 4: JSON
+ Following the instructions for exercise 4, I created a shell program canadiana.sh.
  + I changed the dates searched from 1914 to 1918 (`&df=1914&dt=1918`) to 1880 to 1885 (`&df=1880&dt=1885`).
+ I ran the program and downloaded output.txt to my machine.
+ I saved my commands history as module2exercise4_commands.md.
+ I lodged output.txt and module2exercise4_commands.md into my /hist3814o_module2/ repo.
 + ERROR: output.txt is too big for github's 25mb limit. Will consult with my classmates on slack.
 + My filesize was okay'd by Dr. Graham.


## EXERCISE 5: TWARC
+ error: could not install TWARC: `sudo: pip: command not found`
  + I posted on Slack asking about this error.
  + response from Dr. Graham got it fixed: running `pip install twarc` worked. I annotated the instructions to let my classmates know.
+ I love reading and this class is making me think about diversity and community and technology, so I searched JSON for `ownvoices` (a community campaign led by readers and authors promoting books written by minority characters written by minorities)
+ got error message when trying to convert using json2csv. It seems to have to do with a formatting error in the json file. I screencapped the error message and uploaded it to /hist3814o_module2/ as module2exercise5errormsg.png.
  + I posted in Slack asking about this error.
+ (copied from slack group) found error: the json file produced by twarc treats each tweet as its own array, without an initial array connecting them all into one file, like this: `{"data": "value"...} {"data": "value"...} {"data": "value"...}`. I was able to use notepad++'s replace function and some regex to separate them out into something like this:
`{ "tweet": {"data": "value"...}, "tweet": {"data": "value"...}, "tweet": {"data": "value"...} }`
but now I have a bunch of objects all called "tweet", and if I want to make a valid json out of them I'd have to go and manually add "tweet1", "tweet2", "tweet3" to each one... is there a python program to help me with this? I feel like this should be doable, but I don't know how to write it myself.
+ to replace, I used Notepad++'s extended replace function: replaced  `{"in_reply_to_status_id":` with `\n "tweet": {"in_reply_to_status_id":`.
  + fail: this resulted in 1000+ objects in the initial array called "tweet"
  + solution: I [wrote a Python program](http://github.com/sarahmcole/hist3814o_module2/replace_json.py) that replaced "tweet" with "tweet1", "tweet2", "tweet3", etc. Then it was valid JSON!
  + future steps: if python supports regex, then this program could be modified to convert directly from `{"in_reply_to_status_id":` to `"tweet + str(n) + ": {"in_reply_to_status_id":`, with n going up by 1 with each object.
   + I added documentation and the program now uses the initial .json output from twarc; no need to add `"tweet": {`
+ json2csv accepted my new .json and converted it to csv, which I saved to my own machine as "search_output.csv" and deleted from DHBox (as it was over 5MB).

## EXERCISE 6: TESSERACT OCR
+ downloaded tesseract, imagemagick and pdftk.
+ fail: downloaded index.html because I forgot the -r command in wget. duh.
+ polite fail: took 16 minutes to download the .pdf because I included `--limit-rate=20k`. Took a youtube break in the meantime.
+ fail: I forgot to -nd, so my file wound up in ocr-test/collections.banq.qc.ca:8008/jrn03/equity/src/1957/07/04
+ I moved the file back to /ocr-test/ then completed the tutorial.
+ possible fail: the OCR is completely unreadable!
  + I'll upload it to github and consult with my classmates on Slack.
+ uploaded output_exercise6.txt (renamed from output.txt.txt), pg_0001.pdf, and module2exercise6_commands.md to github.
