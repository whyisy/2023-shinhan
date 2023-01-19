from django.contrib.auth.hashers import check_password
from .models import Member   #전에는 import User 썼는데 여기서는 member에서 가져와서 썼음

class MemberAuth:
    def authenticate(self, request, username=None, password=None, *args, **kwargs):   #우리는 username, password를 사용하는 걸 이미 알기 때문에, 변수명을 명시하고 기본값을 넣은 것. 안쓸꺼면 하단에 username = kwargs[username]? 뭐 이런 식으로      
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            else:    
                return None
        
        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None

        print(member, member.password)
        if check_password(password, member.password):


            if member.status == '일반':
                return member
        return None

    def get_user(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None
        return member #if member.is_active and member.status == '일반' else None  (인증단계에서 이미 거르기 때문에 할 필요 x)