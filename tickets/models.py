from django.db import models

class User(models.Model):
	""" A user """
	name=models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.name)

class Status(models.Model):
	"""A ticket status"""
	number=models.IntegerField()
	name=models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.name)

class Category(models.Model):
	"""A ticket status"""
	number=models.IntegerField()
	name=models.CharField(max_length=255)

	def __unicode__(self):
		return unicode(self.name)

class Ticket(models.Model):
	"""A ticket"""
	number=models.IntegerField()
	summary=models.CharField(max_length=255)
	status=models.ForeignKey(Status,blank=True,null=True)
	assignee=models.ForeignKey(User,blank=True,null=True)
	category=models.ForeignKey(Category,blank=True,null=True)

	def __unicode__(self):
		return unicode(self.number)

	def __save__(self,*args,**kwargs):
		"""Replicate the saved changes to remote system"""
		#Only save local changes if remote save is successful, otherwise throw error
		super(Ticket,self).__save__(*args,**kwargs)
		pass

