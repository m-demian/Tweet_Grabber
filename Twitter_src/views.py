from django.shortcuts import render
from django.http import HttpResponse

import requests

from bs4 import BeautifulSoup


# Create your views here.


def index(request):
	if request.GET.get('username'):
		username = request.GET.get('username')
		URL = 'http://twitter.com/' + username 

		html_doc = requests.get(URL).text

		soup = BeautifulSoup(html_doc, 'html.parser')

		# Check if User is found
		try:
			tweets = soup.find_all('p')[2:7]
		except:
			tweets_list = ['User not found']
		else:
			tweets_list = [tweet.text for tweet in tweets]

	context = { 'content': tweets_list}

	return render(request, 'main/welcome.html',context)

