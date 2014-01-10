import re
import grequests

books = eval(open('books.dict.py').read())
books.sort(key=lambda v: (v['author'], v['title']))
for b in books:
    b['image'] = re.sub('SX\d+_SY\d+', 'SX1000_SY1000', b['image'])

rs = grequests.map(grequests.get(b['image']) for b in books)

for i, r in enumerate(rs):
    filename = 'covers/cover-%03d.jpg' % (i+1) 
    print '%s -> %s' % (r.url, filename)
    with open(filename, 'w') as f:
        f.write(r.content)
