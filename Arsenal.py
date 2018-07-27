import urllib2
from bs4 import BeautifulSoup
import re
import datetime

# url to goal's team page
url = 'http://www.goal.com/en-in/teams'
page = urllib2.urlopen(url)

# parse the html using bs4 and store in variable 'soup'
soup = BeautifulSoup(page, 'lxml')

# finding link to football club's page 
foo = soup.find('div', attrs={'class':'main-content'})
bar = foo.find(text=re.compile('Arsenal'))
url = bar.parent.parent.attrs['href']

# opening football club's fixture page directly
url = "http://www.goal.com" + url
url = url.split('/')
url_foo =  '/'.join(url[:6])
url_bar = ''.join(url[6:]) 
url = url_foo + '/fixtures-results/' + url_bar
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'lxml')

# printing required data
print
foo = soup.find('div', attrs={'class':'status-fix'})
# time data
bar = foo.attrs['data-timestamp']
bar =  bar[:-3]
bar = int(bar) - 19800
print datetime.datetime.fromtimestamp(int(bar)).strftime("%B %d, %A - %I:%M %p").center(80)
print
# team names
bar = foo.find('div', attrs={'class':'team-home'})
print bar.find('span', attrs={'class':'team-name'}).text.center(40)
bar = foo.find('div', attrs={'class':'team-away'})
print 'vs'.center(80)
print bar.find('span', attrs={'class':'team-name'}).text.center(120)
# score
bar = foo.find('div', attrs={'class':'team-home'})
print bar.find('span', attrs={'class':'goals'}).text.center(40) 
bar = foo.find('div', attrs={'class':'team-away'})
print bar.find('span', attrs={'class':'goals'}).text.center(120) 
# match type
bar = foo.find('div', attrs={'class':'match-additional-data'})
print bar.text.center(80)
print
###############################################################################################
###############################################################################################
###############################################################################################
# printing previous match details
#print 'Previously'.center(80)
#foo = foo.find_previous_sibling('div') 
###############################################################################################
# time data
#bar = foo.attrs['data-timestamp']
#bar =  bar[:-3]
#bar = int(bar) - 19800
#print datetime.datetime.fromtimestamp(int(bar)).strftime("%B %d, %A - %I:%M %p").center(80)
#print
###############################################################################################
# team names
#bar = foo.find('div', attrs={'class':'team-home'})
#print bar.find('span', attrs={'class':'team-name'}).text.center(40)
#bar = foo.find('div', attrs={'class':'team-away'})
#print 'vs'.center(80)
#print bar.find('span', attrs={'class':'team-name'}).text.center(120)
###############################################################################################
# score
#bar = foo.find('div', attrs={'class':'team-home'})
#print bar.find('span', attrs={'class':'goals'}).text.center(40) 
#bar = foo.find('div', attrs={'class':'team-away'})
#print bar.find('span', attrs={'class':'goals'}).text.center(120) 
###############################################################################################
# match type
#bar = foo.find('div', attrs={'class':'match-additional-data'})
#print bar.text.center(80)
#print
###############################################################################################
