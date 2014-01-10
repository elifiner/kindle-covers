import glob
with open('index.html', 'w') as f:
    for filename in glob.glob('covers/*.jpg'):
        print >>f, '<img style="height:250px; width:165px" src="%s">' % filename
