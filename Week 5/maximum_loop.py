fname = input("Enter file name: ")
counts = dict()
handle = open(fname)
for line in handle:
   line=line.rstrip()
   if line.startswith('From '):
       words=line.split()
       counts[words[1]]=counts.get(words[1],0)+1
bigcount=0
for word,count in counts.items():
   if bigcount == 0 or count>bigcount:
       bigword=word
       bigcount=count

print(bigword,bigcount)
