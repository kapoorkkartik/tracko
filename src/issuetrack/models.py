from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Issue(models.Model):
	PROJECT_CHOICES = (
		('SAR','Sarathi'),
		('VAH','Vahan'),
		('OTH','Other'),
	)

	OFFICE_CHOICES = (
		('SAM','Samba'),
		('KAT','Kathua'),
		('REA','Reasi'),
		('JAM','Jammu'),
		('UDH','Udhampur'),
	)

	title = models.CharField(max_length = 50)
	application_no = models.CharField(max_length = 50,unique = True)
	birth_date = models.DateField()
	license_no = models.CharField(max_length = 50)
	applicant_name = models.CharField(max_length = 100)
	issue_description = models.TextField(blank=True,null=True)
	creator = models.ForeignKey(User,related_name = "create_issues",blank=True,null=True)
	owner = models.ForeignKey(User,related_name = "created",blank=True,null=True)
	office = models.CharField(max_length = 50,choices = OFFICE_CHOICES)
	closed = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add = True)
	project = models.CharField(max_length=100,choices = PROJECT_CHOICES)
	tags = models.ManyToManyField('Tag',related_name="issues",blank=True)

	def get_absolute_url(self):
		return reverse('issue_detail',kwargs={'pk':self.pk})

	def __unicode__(self):
		return self.title

	def _issue_description(self):
		return self.issue_description[:50] + '...'




class Tag(models.Model):
	creator = models.ForeignKey(User,related_name="tags",blank=True,null=True)
	tag = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.tag

class Comment(models.Model):
	creator = models.ForeignKey(User,related_name="comments",blank=True,null=True)
	issue = models.ForeignKey('Issue',related_name = "comments" ,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	body = models.TextField(max_length=3000)

	class Meta:
		ordering = ["-created"]

	def __unicode__(self):
		return unicode(self.issue.title if self.issue.title else '') + ":" + self.body[:20]

	def get_absolute_url(self):
		return reverse('issue_detail',kwargs={'pk':self.issue.pk})
