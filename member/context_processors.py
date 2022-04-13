from member.models import Member

def flag_processor(request):
    flag = 1
    member = 0
    if request.session.get('user') :
        flag = 1
        member = Member.objects.get(member_id = request.session.get('user'))
    else:
        flag = 0    
    

    return {'flag': flag, 'member':member}