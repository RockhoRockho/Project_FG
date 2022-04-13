from member.models import Member

def flag_processor(request):
    flag = 1
    if request.session.get('user') :
        flag = 1
    else:
        flag = 0    

    member = Member.objects.get(member_id = request.session.get('user'))
    return {'flag': flag, 'member':member}