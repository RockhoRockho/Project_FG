from django.shortcuts import render

def member_login(request):
    context={

    }
    return render(request, 'member_login.html', context)
    
def member_join(request):
    return render(request, "member_join.html")

def member_terms(request):
    return render(request, "member_terms.html")

