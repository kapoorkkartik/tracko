import django_filters
from .models import Issue


class IssueFilter(django_filters.FilterSet):
	class Meta:
		model = Issue
		fields = {
		'id':['exact'],
		'application_no':['exact'],
		'applicant_name':['icontains'],
		'birth_date':['exact'],
		'closed':['exact'],
		}