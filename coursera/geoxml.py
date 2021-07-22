import urllib.request as urli
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

total_count = 0
sum = 0

print('Retrieving', url)
xml = urli.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_count += 1

print('Count:', total_count)
print('Sum:', sum)