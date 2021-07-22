largest = None
smallest = None

while True:
    input_num = input("Enter a number: ")
    if input_num == "done" : 
        break
    try:
        num = float(input_num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
        largest = num1
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

def done(largest,smallest):
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))

done(largest,smallest)