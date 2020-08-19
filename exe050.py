'''fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: ") : continue
    count = count + 1
x = line.find(':')
print(line)
sppos = line.find('.0' , x)  
print(sppos)
host = float(line[x: sppos])
media = host/count
print(media)'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    words = line.split()
    print(float(words[1]))
    total = (float(words[1]))
    media = total/count
print(total)  