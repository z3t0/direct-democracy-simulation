from django import forms


class IssueForm(forms.Form):
    issue_title = forms.CharField(label='Issue title', max_length=50)
    print("New issue request received")
