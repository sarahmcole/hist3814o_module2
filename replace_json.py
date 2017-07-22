# code inspired by https://stackoverflow.com/questions/4746190/find-and-replace-within-a-text-file-using-python
# This program will add an initial array with each tweet numbered (eg "tweet1", "tweet2", "tweet3") to an output file from twarc that is missing an initial array.
# Rename output file from twarc to input.json. Create an empty file named output.json. Keep these in the same folder as this .py file.

n = 1
f1=open("input.json", "r")
f2=open("output.json", "w")

for line in f1:
  # '{"in_reply_to_status_id":' is the first element of each new tweet
  line = line.replace('{"in_reply_to_status_id":', '\n"tweet' + str(n) + '": {"in_reply_to_status_id":')
  n = n+1
  f2.write(line)
f1.close()
f2.close()
