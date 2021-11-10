import webbrowser

f = open('helloworld.html','w')

message = """<html>
<head></head>
<body style="color:red"><h3>Hello World!</h3></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')