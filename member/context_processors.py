def flag_processor(request):
    flag = 1
    if request.session.get('user') :
        flag = 1
    else:
        flag = 0    
    return {'flag': flag}