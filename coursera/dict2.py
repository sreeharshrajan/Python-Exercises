fname = input('Enter File Name:')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wrds =  lin.split()
    #print(wrds)
    for w in wrds:
        #idiom: retrive/create/update counter
        di[w] = di.get(w,0) + 1

        #print('**',w,di.get(w,-99))
        #oldcount = di.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount + 1 
        #di[w] = newcount
       # if w in di :
         #   di[w] = di[w] + 1
       # else:
         #   di[w] = 1
       # print(w,di[w])

#print(di)

#finding most common word
k=0
v=0
largest = -1
theWord = 1

for k,v in di.items():
    print (k,v)
    if v > largest:
        largest = v
        theWord = w #Capturing the largest word

print("The Most Common Word is", theWord)
print("It appears",largest)