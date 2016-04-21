'''
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
import pickle
import os

thefile = open('reportsencampment_url.txt', 'w')


def page_of_data(i): # normally the web-page with ten reports on it.
	page_no =str(i)
	url_base = 'http://mobile311.sfgov.org/'
	#url_ext = '?page='+page_no+'&service_id=518d5892601827e3880000c5' # street and sidewalk cleaning
	url_ext = '?page='+page_no+'&service_id=55e8409a45ff461f92000006' # homeless concerns
	# change this line for other type of service reports
	url= url_base+url_ext+'&status=open' #status closed is possible
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),'lxml')
	#get report numbers from first page
	reports = soup.table('span',"activity-timestamp") # using find_all => gives [ ]


	#get details from second page
	#should modify code to also get location information
	for line in reports:
		line=str(line)
		x=line.find("#")+1
		y=x+7
		z=line[x:y]
		
		#print z - the active report number
		url_goal = url_base+"reports/"+z
		#print url_goal

		page2 = urllib2.urlopen(url_goal)
		real_soup = BeautifulSoup(page2.read())
		#print real_soup # for debugging
		
		

		blockquote = real_soup('blockquote')
		for lne in blockquote:
			request_type = lne.find_next_sibling('p') 
			#print request_type
			if 'Encampment' in str(request_type):
				print url_goal
				#print blockquote
				#thefile.write("%s\n" % url_goal)
				with open("url_list.txt","a") as thefile:
					thefile.write("%s\n" % url_goal)


		#pane = real_soup("div","tab-pane active")
		#for ln in pane:
					
		#	script = ('script')
		#	print script
		
for i in range(20):
	page_of_data(i)
