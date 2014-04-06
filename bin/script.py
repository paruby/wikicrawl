import urllib2
import sys

def check_p(i,source):
	if(source[i]=='<' and source[i+1]=='p' and source[i+2]=='>'):
		return 1
	else:
		return 0
		
def check_a(i,source):
	if(source[i]=='<' and source[i+1]=='a'):
		return 1
	else:
		return 0


def find_next_url(url):
	
	document = urllib2.urlopen(url)
	page_source = document.read()
	
	i=0
	
	while(check_p(i,page_source)==0):
		i+=1
	

	# now we've got to here we know that we've got to the first paragraph of
	# actual text

	bracket_stack = 0
	square_stack = 0

	while(check_a(i,page_source)==0):
		i+=1
		if(page_source[i]=='('):
			bracket_stack+=1
			while(bracket_stack!=0):
				i+=1
				if(page_source[i]=='('):
					bracket_stack+=1
				if(page_source[i]==')'):
					bracket_stack-=1
		if(page_source[i]=='['):
			square_stack+=1
			while(square_stack!=0):
				i+=1
				if(square_source[i]=='['):
					square_stack+=1
				if(page_source[i]==']'):
					square_stack-=1
		if(page_source[i:i+4]=='<sup'):
			while(page_source[i:i+6]!='</sup>'):
				i+=1
				
	while(page_source[i]!='"'):
		i+=1
	
	LINK = ''
	i+=1
	while(page_source[i]!='"'):
		LINK = LINK + page_source[i]
		i+=1

	return BASE+LINK


BASE = "http://en.wikipedia.org"
NUMBER_OF_TRIALS = 50
ouput=''

output.append(next_url)

reached_philosophy=0
reached_information=0
k=0;
for k in range(0,NUMBER_OF_TRIALS):
	try:
		next_url = "http://en.wikipedia.org/wiki/Special:Random"
		j=0;
		while(next_url!='http://en.wikipedia.org/wiki/Philosophy' and\
next_url!='http://en.wikipedia.org/wiki/Information' and j<MAX):
			next_url = find_next_url(next_url)
			ouput.append(next_url)
			if (("File:" in next_url) or ("//upload.wikimedia" in next_url) \
or ("w/index" in next_url)):
				ouput.append("Error! We've gone to a picture. Starting again \n")
				break
			j+=1
		if next_url=='http://en.wikipedia.org/wiki/Philosophy':
			reached_philosophy+=1
			output.append("\n Getting random page... \n")
		if next_url=='http://en.wikipedia.org/wiki/Information':
			reached_information+=1
			output.append("\n Getting random page... \n")
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		output.append("Error! Starting again \n")

output.append("\n\n\n")
output.append("Proportion to reach Philosophy is:" + \
str(float(reached_philosophy)/float(NUMBER_OF_TRIALS)))
output.append("\n Proportion to reach Information: " + \
str(float(reached_information)/float(NUMBER_OF_TRIALS)))	
	
	
	
	
	