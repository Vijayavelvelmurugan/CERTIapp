from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        dob = request.POST['date_of_birth']
        mobile = request.POST['mobile_number']
        whats = request.POST['whatsapp_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            return HttpResponse("Your password and confirm password do not match!")
        else:
            # Create a new User object and save it
            user = User.objects.create_user(username=username, password=password1, last_name=last_name)
          
            user = authenticate(username=username, password=password1)
            if user:
                login(request, user)
                return redirect('login')  # Redirect to the login page after successful signup
            else:
                return HttpResponse("User creation failed.")

    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            return HttpResponse("Invalid login credentials. Please try again.")

    return render(request, 'login.html')

def homepage(request):
    # Add your homepage logic here
    return render(request, 'home.html')
