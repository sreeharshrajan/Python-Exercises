import json

input = '''
[
    {
        "id" : "001",
        "x"  : "2",
        "name" : "chuck"
    } ,
    {
        "id" : "003",
        "x"  : "6",
        "name" : "dump"
    }
]'''

info = json.loads(input)
print('User Counts: ',len(info))

for item in info:
    print("Name: ", item['name'])
    print("ID: ", item['id'])
    print("Attribute: ", item['x'])