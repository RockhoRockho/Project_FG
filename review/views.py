from urllib.request import Request
from django.shortcuts import render
from review.models import Review
from member.models import Member
from django.http import Http404

def review(request):
    all_review = Review.objects.all().order_by('-id')
    all_count = Review.objects.all().count()

    context = {
        'review' : all_review,
        'count' : all_count
    }
    return render(request, 'review.html', context)

def review_write(request):
    return render(request, 'review_update.html')

def review_detail(request):
    return render(request, 'review_update.html')

def review_update(request):
    return render(request, 'review_update.html')

    
def review_delete(request):
    return render(request, 'review_update.html')