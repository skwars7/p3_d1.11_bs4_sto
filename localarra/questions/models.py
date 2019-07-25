from django.db import models


class CloseReasonTypes(models.Model):
	Name			=	models.CharField(max_length=40)
	Description		=	models.CharField(max_length=250,null=True,blank=True)

	def __str__(self):
		return self.Name

class PostTypes(models.Model):
	Name			=	models.CharField(max_length=250)
	
	def __str__(self):
		return self.Name

class Posts(models.Model):
	PostTypeId				=	models.ForeignKey(PostTypes, on_delete=models.CASCADE)
	AcceptedAnswerId		=	models.IntegerField(null=True, blank=True) #check and defile post id is ailable or not
	ParentId				=	models.IntegerField(null=True, blank=True) #it is attachted question id 	
	CreationDate			=	models.DateTimeField(auto_now_add=True)
	DeletionDate			=	models.DateTimeField(null=True, blank=True)
	Score					=	models.IntegerField(default='0')
	ViewCount				=	models.IntegerField(default='0')
	Body					=	models.TextField()
	OwnerUserId				=	models.IntegerField() #after we cahnge it to auth_user 
	OwnerDisplayName		=	models.CharField(max_length=40)
	LastEditorUserId		=	models.IntegerField(null=True,blank=True)
	LastEditorDisplayName	=	models.CharField(max_length=40,null=True,blank=True)
	LastEditDate			=	models.DateTimeField(null=True,blank=True)
	LastActivityDate		=	models.DateTimeField(auto_now_add=True)
	Title					=	models.CharField(max_length=140, null=True, blank=True)
	Tags					=	models.CharField(max_length=250, null=True, blank=True)
	AnswerCount				=	models.IntegerField(default='0')
	CommentCount			=	models.IntegerField(default='0')
	FavoriteCount			=	models.IntegerField(default='0')
	ClosedDate				=	models.DateTimeField(null=True, blank=True)
	CommunityOwnedDate		=	models.DateTimeField(null=True, blank=True)

	def __str__(self):
		if self.Title == None:
			Title = 'it\'s not a question'
		else:
			Title = self.Title
		return Title

class Tags(models.Model):
	TagName			=	models.CharField(max_length=250)
	Count			=	models.IntegerField(default='0')
	ExcerptPostId	=	models.ForeignKey(Posts, on_delete=models.CASCADE,null=True, blank=True)
	WikiPostId		=	models.IntegerField(null=True, blank=True) #coming soon primary key

	def __str__(self):
		return self.TagName

class PostTags(models.Model):
	PostId			=	models.ForeignKey(Posts, on_delete=models.CASCADE)
	TagId			=	models.ForeignKey(Tags, on_delete=models.CASCADE)

	def __int__(self):	#change the str instade of int for see what is there
		return self.PostId,self.TagId

class VoteTypes(models.Model):
	Name			=	models.CharField(max_length=250)
	def __str__(self):
		return self.Name

class Votes(models.Model):
	PostId			=	models.ForeignKey(Posts, on_delete=models.CASCADE)
	VoteTypeId		=	models.ForeignKey(VoteTypes, on_delete=models.CASCADE)
	UserId			=	models.IntegerField() #coming soon primary key
	CreationDate	=	models.DateTimeField(auto_now_add=True)
	BountyAmount	=	models.IntegerField(null=True, blank=True)