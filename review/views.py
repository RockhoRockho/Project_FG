from django.shortcuts import render

def review(request, member_pk):
    return render(request, 'review.html')
