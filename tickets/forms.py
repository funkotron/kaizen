from django import forms
from tickets.models import Ticket

class UpdateTicketForm(forms.ModelForm):

    comment = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols': 70, 'rows': 4}),required=False)

    class Meta:
        model = Ticket
        fields = ['summary','assignee','status','category']

    def __init__(self,*args,**kwargs):
        super(UpdateTicketForm,self).__init__(*args,**kwargs)
        self.fields['summary'].label = "Summary <i class='icon-info-sign'></i>"
        self.fields['assignee'].label = "Assign <i class='icon-user'></i>"
        self.fields['status'].label = "Status <i class='icon-flag'></i> "
        self.fields['category'].label = "Category <i class='icon-th-large'></i>"
        self.fields['comment'].label = "Comment <i class='icon-comment'></i> "


    def __save__(self,*args,**kwargs):
        if 'comment' in self.cleaned_data:
            #TODO: Update this separately
            del self.cleaned_data['comment']
        super(UpdateTicketForm,self).__save__(*args,**kwargs)
