s = "We work hard because hard work pays."

tokens = s.split(" ")
d = {}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1

print(d)