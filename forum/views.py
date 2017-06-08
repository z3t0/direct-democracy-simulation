from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Issue
from .forms import IssueForm


def index(request):
    latest_isssues_list = Issue.objects.all()

    context = {
        'latest_issues_list': latest_isssues_list,
    }

    return render(request, 'forum/index.html', context)

def issueDetail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    return render(request, 'forum/issue.html', {'issue': issue})

@login_required
def newIssue(request):
    if request.method == "POST":
        form = IssueForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            issue = Issue(title=title, description=description, author=request.user.citizen)

            issue.save()

            return HttpResponseRedirect(issue.get_absolute_url())

    else:
        form = IssueForm()

    context = {'form': form}

    return render(request, 'forum/new_issue.html', context)
