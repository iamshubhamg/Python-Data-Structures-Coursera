
fname = raw_input("Enter file name: ")
fh = open(fname)
#fname  https://www.py4e.com/code3/words.txt

for fx in fh:
    fy = fx.rstrip()
    print(fy.upper())
