from .models import Issue,Comment
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField,FormActions,StrictButton

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        exclude = ('creator','created','tags')
        widgets = {
            'birth_date':forms.DateInput(attrs={'class':'datepicker'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class IssueListFormHelper(FormHelper):    
    form_id = 'issue-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    # field_class = 'col-xs-3'
    # label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Issue Records',
                    InlineField('id'),
                    InlineField('birth_date'),
                    InlineField('closed'),
                    InlineField('application_no')
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search', 
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )
