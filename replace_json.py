# code inspired by https://stackoverflow.com/questions/4746190/find-and-replace-within-a-text-file-using-python
n = 1
f1=open("input.json", "r")
f2=open("output.json", "w")
for line in f1:
  line = line.replace('"tweet"', '"tweet' + str(n) + '"')
  n = n+1
  f2.write(line)
f1.close()
f2.close()
