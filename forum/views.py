from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Issue


@login_required
def index(request):
    latest_isssues_list = Issue.objects.all()

    context = {
        'latest_issues_list': latest_isssues_list
    }

    return render(request, 'forum/index.html', context)


def issueDetail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)

    return render(request, 'forum/issue.html', {'issue': issue})
