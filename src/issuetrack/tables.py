import django_tables2 as tables
from django_tables2.utils import A
from .models import Issue



class IssueTable(tables.Table):
	closed = tables.BooleanColumn(yesno='Yes,No')
	class Meta:
		model = Issue
		attrs = {'class':'table table-striped table-condensed', 'id':'report-table'}
		empty_text = "There are no issues matching the search criteria"
		fields = ('id','applicant_name','application_no','birth_date','license_no','_issue_description','created','closed')
		orderable = False

class IssueListTable(tables.Table):
	closed = tables.BooleanColumn(yesno='Yes,No')
	id = tables.LinkColumn('issue_detail', args=[A('pk')])
	class Meta:
		model = Issue
		attrs = {'class':'table table-striped table-condensed table-hover table-bordered', 'id':'issue-list-table'}
		empty_text = "There are no issues matching the search criteria"
		fields = ('id','applicant_name','application_no','birth_date','license_no','title','created','closed')