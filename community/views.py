from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from .models import Community_review, Community_comment
from .forms import Community_reviewForm, Community_commentForm
# Create your views here.

@require_safe
def index(request):
    
    community_reviews = Community_review.objects.all()

    context = {
        'community_reviews': community_reviews,
    }

    return render(request, 'community/index.html', context)

@login_required
def detail(request, pk):

    community_review = get_object_or_404(Community_review, pk=pk)

    community_comment = Community_comment.objects.filter(review_id=community_review.pk)
    
    community_commentForm = Community_commentForm()

    context = {
        'community_review': community_review,
        'community_comment': community_comment,
        'community_commentForm': community_commentForm,
    }

    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = Community_reviewForm(request.POST)

        if form.is_valid():
            community_review = form.save(commit=False)
            community_review.user_id = request.user
            community_review.save()
            return redirect('community:detail', community_review.pk)

    else:
        form = Community_reviewForm()
    
    context = {
        'form': form,
    }

    return render(request, 'community/form.html', context)

@login_required
@require_POST
def comments_create(request, pk):
    
    community_review = get_object_or_404(Community_review, pk=pk)
    
    community_commentForm = Community_commentForm(request.POST)
    
    if community_commentForm.is_valid():
        community_comment = community_commentForm.save(commit=False)
        community_comment.review_id = community_review
        community_comment.user_id = community_review.user_id
        community_comment.save()
        return redirect('community:detail', community_review.pk)

    return redirect('community:index')