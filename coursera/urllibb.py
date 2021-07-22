import urllib.request, urllib.parse, urllib.error
#from urllib.request import Request, urlopen

#fhandle = Request('http://data.pr4.org/romeo.txt', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(fhandle).read()

fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page-1.htm')
counts = dict()
for line in fhandle:
    print(line.decode().strip())
    words = line.decode().strip()
    for word in words:
        counts[words] = counts.get(word,0) + 1
print(counts)