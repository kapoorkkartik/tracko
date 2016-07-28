from braces.views import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import View,ListView,FormView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView,SingleObjectMixin
from django_tables2 import RequestConfig
from .models import Issue,Comment
from .forms import IssueForm,CommentForm,IssueListFormHelper
from .tables import IssueTable,IssueListTable
from .filters import IssueFilter
from .utils import PagedFilteredTableView
import django_filters

# Create your views here.

class IssueCreate(LoginRequiredMixin,CreateView):
	model = Issue
	form_class = IssueForm
	exclude = ['creator','tags','created']


class IssueDisplay(DetailView):
	model = Issue

	def get_context_data(self,**kwargs):
		context = super(IssueDisplay,
			self).get_context_data(**kwargs)
		context['form'] = CommentForm()
		return context

class CommentRecord(SingleObjectMixin,FormView):
	template_name = 'issuetrack/issue_detail.html'
	form_class = CommentForm
	model = Issue

	def post(self,request,*args,**kwargs):
		if not request.user.is_authenticated():
			return HttpResponseForbidden()
		self.object = self.get_object()
		return super(CommentRecord,
			self).post(request,*args,**kwargs)

	def get_success_url(self):
		return reverse('issue_detail',kwargs={'pk':self.object.pk})

	def form_valid(self,form):
		form.instance.creator = self.request.user
		form.instance.issue = get_object_or_404(Issue,pk=self.kwargs.get('pk'))
		form.save()
		return super(CommentRecord,self).form_valid(form)


class IssueDetail(LoginRequiredMixin,View):

	def get(self,request,*args,**kwargs):
		if 'pk' in self.request.GET:
			try:
				pk = int(self.request.GET.get('pk'))
				if pk <= 0:
					raise ValueError
			except ValueError:
				return HttpResponseRedirect('/issuetrack')
			return HttpResponseRedirect(reverse('issue_detail',kwargs = {'pk':pk}))
		view = IssueDisplay.as_view()
		return view(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		view = CommentRecord.as_view()
		return view(request,*args,**kwargs)


def reports(request):
	table = IssueTable(Issue.objects.all())
	return render(request,'issuetrack/reports.html',{'table':table})

class IssueUpdate(LoginRequiredMixin,UpdateView):
	model = Issue
	form_class = IssueForm
	exclude = ['creator','tags','created']


class IssueListView(LoginRequiredMixin,PagedFilteredTableView):
	model = Issue
	template_name = 'issuetrack/issue_list.html'
	context_object_name = 'issue_list'
	ordering = ['id']
	table_class = IssueListTable
	filter_class = IssueFilter
	formhelper_class = IssueListFormHelper

	def get_queryset(self):
		qs = super(IssueListView,
			self).get_queryset()
		return qs

	def post(self,request,*args,**kwargs):
		return PagedFilteredTableView.as_view()(request)


	def get_context_data(self,**kwargs):
		context = super(IssueListView,
			self).get_context_data(**kwargs)
		search_query = self.get_queryset()
		table = IssueListTable(search_query)
		RequestConfig(self.request,paginate={'per_page':10}).configure(table)
		context['table'] = table
		return context