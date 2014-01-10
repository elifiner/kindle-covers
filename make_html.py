import glob
with open('index.html', 'w') as f:
    for filename in glob.glob('covers/*.jpg'):
        print >>f, '<img style="height:320px; width:215px" src="%s">' % filename
