from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')  # Ensure home.html exists and is correctly placed

@login_required
def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        # Handle chatbot logic here
        response = "This is a dummy response."  # Replace with actual logic
        return render(request, 'chatbot.html', {'response': response})
    return render(request, 'chatbot.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('chat')  # Redirect to chat page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')  # Redirect to home page after logout
    return render(request, 'logout.html')  # Optionally, render a logout confirmation page or message

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('chat')  # Redirect to chat page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
