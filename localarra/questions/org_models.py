from django.db import models

class Posts(models.Model):
	PostTypeId				=	models.IntegerField()
	AcceptedAnswerId		=	models.IntegerField()
	ParentId				=	models.IntegerField()
	CreationDate			=	models.DateTimeField(auto_now_add=True)
	DeletionDate			=	models.DateTimeField()
	Score					=	models.IntegerField()
	ViewCount				=	models.IntegerField()
	Body					=	models.TextField()
	OwnerUserId				=	models.IntegerField()
	OwnerDisplayName		=	models.CharField(max_length=40)
	LastEditorUserId		=	models.IntegerField()
	LastEditorDisplayName	=	models.CharField(max_length=40)
	LastEditDate			=	models.DateTimeField()
	LastActivityDate		=	models.DateTimeField()
	Title					=	models.CharField(max_length=140)
	Tags					=	models.CharField(max_length=250)
	AnswerCount				=	models.IntegerField()
	CommentCount			=	models.IntegerField()
	FavoriteCount			=	models.IntegerField()
	ClosedDate				=	models.DateTimeField()
	CommunityOwnedDate		=	models.DateTimeField()

	def __str__(self):
		return self.Title

class CloseReasonTypes(models.Model):
	Name			=	models.CharField(max_length=40)
	Description		=	models.CharField(max_length=250)

	def __str__(self):
		return self.Name

class PostTags(models.Model):
	PostId			=	models.IntegerField()
	TagId			=	models.IntegerField()

class PostTypes(models.Model):
	Name			=	models.CharField(max_length=250)
	
	def __str__(self):
		return self.Name

class Tags(models.Model):
	TagName			=	models.CharField(max_length=250)
	Count			=	models.IntegerField()
	ExcerptPostId	=	models.IntegerField()
	WikiPostId		=	models.IntegerField()

	def __str__(self):
		return self.TagName

class Votes(models.Model):
	PostId			=	models.IntegerField()
	VoteTypeId		=	models.IntegerField()
	UserId			=	models.IntegerField()
	CreationDate	=	models.DateTimeField()
	BountyAmount	=	models.IntegerField()

class VoteTypes(models.Model):
	Name			=	models.CharField(max_length=250)
	def __str__(self):
		return self.Name