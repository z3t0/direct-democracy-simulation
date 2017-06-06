from django import forms


class IssueForm(forms.Form):
    issue_title = forms.CharField(label='Issue title', max_length=50)
    issue_description = forms.CharField(label='Description', max_length=1000)
    print("New issue request received")
