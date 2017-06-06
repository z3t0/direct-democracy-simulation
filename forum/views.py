from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import logging

from .models import Issue
from .forms import IssueForm

logger = logging.getLogger()


@login_required
def index(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)

        if form.is_valid():
            # process data
            # redirect
            logger.info('processed new issue form')

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
