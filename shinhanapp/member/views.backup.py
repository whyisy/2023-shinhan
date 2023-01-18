from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Member

# Create your views here.

# 로그인 페이지
# 기능 1 : 로그인 화면 출력
# 기능 2: 아이디. 비밀번호 입력받아서 로그인 되는 것.
def login(request):
    if request.method == 'POST':
            user_id = request.POST.get("user_id")
            password = request.POST.get("password")
            
            if Member.objects.filter(user_id=user_id).exists():
                member = Member.objects.get(user_id=user_id)    #unique=True 때문에 값이 무조건 1개이기 때문에, .get을 써도 오류 없음
                
                if check_password(password, member.password):
                    request.session['user_pk'] = member.id 
                    request.session['user_id'] = member.user_id   #로그인 성공!!
                    return redirect('/')

            #로그인 실패!

    return render(request,'login.html')

def logout(request):
    if 'user_pk' in request.session:
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')

# 회원가입 페이지 노출
# 회원가입 기능 개발
def register(request):
    if request.method == 'POST':
        member = Member(
            user_id = request.POST.get("user_id"),
            password = make_password(request.POST.get("password")),
            name = request.POST.get("name"),
            age = request.POST.get("age"),
        )
        member.save()
        return redirect('/member/login')
    return render(request,'register.html')

    # if request.method == 'POST':           #강사님 코드, github 참조
    #     user_id = request.POST.get("user_id")
    #     password = make_password(request.POST.get("password")),
    #      name = request.POST.get("name")
    #      age = request.POST.get("age")

    #      member = Member(
    #         user_id=user_id,
    #         pass
    #      )