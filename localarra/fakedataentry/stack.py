import requests
from bs4 import BeautifulSoup
import time
from questions.models import Posts
from django.shortcuts import render
from random import randint

def index(request):
	# loop init
	c = int(45475)
	a = 10
	mylist = {}
	i = int(1)
	#start loop for get data from desire website
	for a in range(100):
		#urls defining
		url = 'https://stackoverflow.com/questions/'+str(c)
		c = int(c) + 786
	
		#temp stop for check everything worksfine
		# time.sleep(5)
		
		#finding the taret and store for future process
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html, "html.parser")
		question_name = soup.find('a', attrs={'class': 'question-hyperlink'})
		question_details = soup.find('div', attrs={'class': 'post-text'})
		question_taglist = soup.find('div', attrs={'class': 'post-taglist'})
		question_accepted_answer_tmp = soup.find('div', attrs={'class': 'accepted-answer'})
		
		#init for database
		if question_name != None and question_details != None and question_taglist != None and question_accepted_answer_tmp != None:
			question_accepted_answer = question_accepted_answer_tmp.find('div', attrs={'class': 'post-text'})
			question_name_final = question_name.text
			question_details_final = question_details.text
			question_taglist_final = question_taglist.text
			question_accepted_answer_final = question_accepted_answer.text
			print(question_taglist_final)
		else:
			continue	

		#printing process
		# print('-------------------------------------------------------------------------------------')
		# print(url)
		# print(c)
		# print('q_title=',question_name_final,'\nq_details=',question_details_final,'\nq_answer=',question_accepted_answer_final)
		# print('-------------------------------------------------------------------------------------')
		# print('######################################################################################')

		#making list for output
		i += 1
		mylist.update({i :{ 'question_name': question_name_final,'questionn_details': question_details_final,'question_tag': question_taglist_final,'question_answer': question_accepted_answer_final }})

		#entry in database
		q = Posts.objects.create(PostTypeId_id=1,Score=randint(1, 100),Body=question_details_final,OwnerUserId=1,OwnerDisplayName='Localarra',Title=question_name_final,Tags=question_taglist_final,AnswerCount=1)
		q.save()
		q.id
		a = Posts.objects.create(PostTypeId_id=2,ParentId=q.id,Score=randint(1, 100),Body=question_accepted_answer_final,OwnerUserId=2,OwnerDisplayName='JunedRaj',Title=question_name_final)
		a.save()
	return render(request, 'fake/my.html', { 'mylist': mylist })	