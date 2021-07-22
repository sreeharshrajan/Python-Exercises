fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except:
    print("File Cannot Be Opened: ", fname)
    quit()

count = 0
for line in fhand:
    count = count + 1
print(count)
inp = fhand.read()
print(len(inp))
print(inp[:20])
print(fname)

