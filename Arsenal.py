# import libraries
import requests
from bs4 import BeautifulSoup
import re
import datetime

def check_blank(foo):
    if (foo == None):
        print "Got nothing yet.."
        print "  -Arsenal FC\n"
        quit()
    return

# specify the url and get html to variable 'page'
url = 'https://m.livesoccertv.com/teams/england/arsenal/'
page = requests.get(url)

# parse the html using bs4 and store in variable 'soup'
soup = BeautifulSoup(page.text, 'lxml')

# finding link to page with required coverage information
foo = soup.find('div', attrs={'class':'-future'})
check_blank(foo)
url_anchor = foo.find('a', attrs={'class':'b_match_all-link'})
url = url_anchor.attrs['href']

# opening and parsing this page
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# print names of teams
print
foo = soup.find('div', attrs={'class':'b_match-top-section'})
check_blank(foo)
bar =  foo.text.strip().splitlines()
print bar[0], " vs ", bar[1]

# print name of competition
foo = soup.find('div', attrs={'class':'b_league'})
print foo.text.strip()
print

# print time and date in IST
foo = soup.find("div", attrs={"class":"b-match-top-section_score_time"})
bar = foo.attrs["data-timestamp"]
print datetime.datetime.fromtimestamp(int(bar)).strftime("%B %d, %A - %I:%M %p")
print

# India specific TV coverage
foo = soup.find(text=re.compile('India'))
check_blank(foo)
bar = foo.parent.parent.parent.text.strip().splitlines()
foobar = []
for b in bar:
    if (b != u'' and b != u'\xa0'):
        foobar.append(b)
print "\n".join(foobar[1:])
print
