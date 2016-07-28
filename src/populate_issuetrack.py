import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tracko.settings')

import django
django.setup()

from issuetrack.models import Issue,Tag,Comment
from django.contrib.auth.models import User

def populate():
	creator = User.objects.get(pk=1)

	# Add tags here
	add_tag(creator,'Fees')
	add_tag(creator,'Scrutiny')
	add_tag(creator,'Approval')
	add_tag(creator,'Test')
	add_tag(creator,'Print')

	# Add issues here
	issue1 = add_issue(title = 'Scrutiny gives error',application_no = '1000',birth_date='1984-10-11',applicant_name='Thapa')
	issue2 = add_issue(title = 'DL not printing',application_no = '1001',birth_date='1985-11-21',applicant_name='Doctor')
	issue3 = add_issue(title = 'Make correction to DL',application_no = '1002',birth_date='1986-01-14',applicant_name='Ram kumar')
	issue4 = add_issue(title = 'Unable to apply',application_no = '1003',birth_date='1987-12-21',applicant_name='Surjit Singh')
	issue5 = add_issue(title = 'Approval not working',application_no = '1004',birth_date='1988-04-16',applicant_name='Sham')
	issue6 = add_issue(title = 'Testing failed',application_no = '1005',birth_date='1989-08-12',applicant_name='Banarsi dass')
	issue7 = add_issue(title = 'Incorrect details shown',application_no = '1006',birth_date='1990-03-03',applicant_name='Pluto')
	issue8 = add_issue(title = 'Slot not booking',application_no = '1007',birth_date='1990-04-09',applicant_name='Akhbar')
	issue9 = add_issue(title = 'Scrutiny gives error',application_no = '1008',birth_date='1945-09-25',applicant_name='Som dutt')
	issue10 = add_issue(title = 'Scrutiny gives error',application_no = '1009',birth_date='1965-05-13',applicant_name='Sham')


	# Add comments here
	add_comments(creator=creator,issue =issue1,body='chal gaya ab')


	for i in Issue.objects.all():
		print "{0}".format(str(i))



def add_tag(creator,tag):
	t = Tag.objects.get_or_create(creator=creator,tag=tag)[0]
	t.save()
	return t

def add_issue(title,application_no,birth_date,applicant_name):
	if not title:
		title = 'Fees not being paid'
	creator = User.objects.get(pk=1)
	i = Issue.objects.get_or_create(title = title,application_no=application_no,birth_date=birth_date,applicant_name=applicant_name)[0]
	i.project = 'SAR'
	i.creator = creator
	i.owner = creator
	i.office = 'SAM'
	i.license_no = 'JK21 201313131311'
	i.issue_description = 'Sample Issue description'
	i.save()
	return i

def add_comments(creator,issue,body=''):
	c = Comment.objects.get_or_create(creator = creator,issue = issue,body = body)[0]
	c.save()
	return c

if __name__ == '__main__':
	print "Starting issuetrack population script"
	populate()