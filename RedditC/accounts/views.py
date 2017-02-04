from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout


def signup(request):
	if request.method == "POST":
		if request.POST["password"] == request.POST["password1"]:
			try:
				user = User.objects.get(username = request.POST["username"])
				return render(request,'accounts/new_account.html', {'message': "Username has already been taken"})
			except User.DoesNotExist:
				User.objects.create_user(username = request.POST["username"], password = request.POST["password"])
				return redirect('home')
		else:
			return render(request,'accounts/new_account.html', {'message': "Passwords didn't match"})
	else:
			return render(request,'accounts/new_account.html')

def login(request):
	if request.method == "POST":
		username1 = request.POST["username"]
		passwd = request.POST["password"]
		user = authenticate(username = username1, password = passwd)
		if user is not None:
			auth_login(request, user)
			if request.POST.get('next') is not None:
				return redirect(request.POST['next'])
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'message':"Invalid Username or Password"})
	else:
		return render(request, 'accounts/login.html')

def logout_view(request):
    if request.POST:
    	logout(request)
    	return redirect('home')