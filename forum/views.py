from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Issue
from .forms import IssueForm


@login_required
def index(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)


        if form.is_valid():
            issue_title = form.cleaned_data["issue_title"]
            issue_description = form.cleaned_data["issue_description"]
            issue = Issue(title=issue_title, description=issue_description, author=request.user.citizen)

            issue.save()
            # redirect
            return HttpResponseRedirect('/')

    else:
        form = IssueForm()

    latest_isssues_list = Issue.objects.all()

    context = {
        'latest_issues_list': latest_isssues_list,
        'form': form
    }

    return render(request, 'forum/index.html', context)

def issueDetail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    return render(request, 'forum/issue.html', {'issue': issue})
