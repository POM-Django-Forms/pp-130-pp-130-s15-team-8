from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib import messages
from order.models import Order


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        first_name = request.POST.get('first_name')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Користувач з таким email вже існує.')
            return redirect('register')

        if role == "librarian":
            is_librarian = True
            is_guest = False
            is_staff = True
        else:
            is_librarian = False
            is_guest = True
            is_staff = False

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            is_librarian=is_librarian,
            is_guest=is_guest,
            is_staff=is_staff,
            is_active=True,
        )
        return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('profile')

        else:
            messages.error(request, 'Неправильний email або пароль')
            return render(request, 'login.html')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_detail.html', {'user': user})


@login_required
def user_profile(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "profile.html", {"orders": user_orders})
