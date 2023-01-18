from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout   #이름 겹치니까 밑에 login을 signin으로 바꿔줌 (함수이름은 그대로)

# Create your views here.

# 로그인 페이지
# 기능 1 : 로그인 화면 출력
# 기능 2: 아이디. 비밀번호 입력받아서 로그인 되는 것.
def signin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect('/')

# 회원가입 페이지 노출
# 회원가입 기능 개발
def register(request):
    if request.method == 'POST':
        User.objects.create_user(           #create_user에서 아이디, 이메일은 필수 / 일일이 작성할 필요 없고 훨씬 편하다
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password'),
        )
        return redirect('/member/login/')

    return render(request,'register.html')