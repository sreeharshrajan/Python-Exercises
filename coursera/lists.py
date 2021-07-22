x = list(range(5))
print(x)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(*c)
print("printing lists separated by commas")
  
print(*c, sep = ", ") 
print(len(c))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])