'''
poop-map.py

another try at using Beautiful soup to get data
from the mobile 311 site
scrapting  it
but the idea here is shit

there is a lot of commentary about San Francisco poop maps, 
but I know, by using the app, andcause I read it in a 
Heather Kninght Chronicle Article in Ap;rilt early 2016
that DPW says the app doesn't distinguish between human poop and dod poop
but there the description field comes in

i
'''
'''
there is code about line 41 that is having no effect.   Im trying to use BeautifulSoup to 
do something like a jquery find, but its not working
Although people say BeautifulSoup is great, 
I'm struggling with it

'''
from bs4 import BeautifulSoup
import urllib2
import re
import string

def page_of_data(i):
	page_no =str(i)
	url_base = 'http://mobile311.sfgov.org/'
	url_ext = '?page='+page_no+'&service_id=518d5892601827e3880000c5' # street and sidewalk cleaning
	url= url_base+url_ext+'&status=open'
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),'lxml')
	#get report numbers
	reports = soup.table('span',"activity-timestamp")
	#get details from second page
	#should modify code to also get location information
	for line in reports:
		line=str(line)
		x=line.find("#")+1
		y=x+7
		z=line[x:y]
		#print z
		url_goal = url_base+"reports/"+z
		#print url_goal
		page2 = urllib2.urlopen(url_goal)
		real_soup = BeautifulSoup(page2.read())
		blockquote = real_soup('blockquote')
		for lne in blockquote:
			request_type = lne.find_next_sibling('p') 
			#print request_type
			if 'Human / Animal Waste'in str(request_type):
				print url_goal
				print blockquote
				pane = real_soup("div","tab-pane active")
				#kids = real_soup.findchildren("div","tab-pane active")
				for ln in pane:
					#kids = real_soup.findchildren("div","tab-pane active")	
					print ln	
					print "	kids**********************************"
				#for line in pane:
					



#end
for i in range(20):
	page_of_data(i)
