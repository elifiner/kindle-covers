import os
import pprint
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from BeautifulSoup import BeautifulSoup

password = getpass.getpass('Kindle Password:')

d = webdriver.Chrome()
os.system("""osascript -e 'tell app "Google Chrome" to activate window 2'""")

d.get('http://kindle.amazon.com')
d.find_element_by_css_selector('[href*="login"]').click()
d.find_element_by_name('email').send_keys('eli.finer@gmail.com')
d.find_element_by_name('password').clear()
d.find_element_by_name('password').send_keys('kupil2litra')
d.find_element_by_name('signIn').submit()
d.save_screenshot('s.png')
d.find_element_by_css_selector('[href*="your_reading"]').click()
books = []

while True:
    soup = BeautifulSoup(d.page_source)
    for tr in soup.find('table', id='yourReadingList').findAll('tr'):
        title = tr.a.string
        author = tr.span.string
        image = None
        if tr.img:
            image = tr.img.get('src')

        if title and author and image:
            books.append(dict(
                title=title.strip(),
                author=author.strip(),
                image=image.strip()
            ))
    try:
        d.find_element_by_partial_link_text('Next').click()
    except NoSuchElementException:
        break

with open('books.dict.py', 'w') as f:
    f.write(pprint.pformat(books))
