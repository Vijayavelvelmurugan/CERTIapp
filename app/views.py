from datetime import datetime, date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Interest, UserProfile
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.password_validation import validate_password
import random
import string
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageDraw, ImageFont
import io
from .models import Interest
   

# Signup view
def signup(request):
    password_error = ""
    age_error = ""
    username_error = ""

    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        date_of_birth_str = request.POST['date_of_birth']
        mobile_number = request.POST['mobile_number']
        whatsapp_number = request.POST.get('whatsapp_number', '')
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        interests = request.POST.getlist('interests')

        date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            username_error = "This username is already taken. Please choose a different username."

        if password1 != password2:
            password_error = "Your password and confirm password do not match."
        else:
            try:
                validate_password(password1, User(username=username))
            except ValidationError as e:
                password_error = ", ".join(e.messages)

        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if age < 18:
            age_error = "Age should be above 18+"

        if username_error:
            interests = Interest.objects.all()
            messages.error(request, username_error)
        elif password_error:
            interests = Interest.objects.all()
            messages.error(request, password_error)
        elif age_error:
            interests = Interest.objects.all()
            messages.error(request, age_error)
        else:
            user = User.objects.create_user(username=username, password=password1, last_name=last_name)

            user_profile = UserProfile(
                user=user,
                date_of_birth=date_of_birth,
                mobile_number=mobile_number,
                whatsapp_number=whatsapp_number,
            )
            user_profile.save()
            user_profile.interests.set(interests)

            user = authenticate(username=username, password=password1)
            if user:
                login(request, user)
                return redirect('custom_login')

    interests = Interest.objects.all()
    return render(request, 'signup.html', {'interests': interests, 'password_error': password_error, 'age_error': age_error, 'username_error': username_error})

# Certificate view
@login_required(login_url='custom_login')
def certificate_view(request):
    user_name = request.user.username
    event_name = "Your Event Name"

    registration_date = datetime.now().strftime("%Y-%m-%d")

    registration_no = generate_registration_number()

    context = {
        'user_name': user_name,
        'event_name': event_name,
        'registration_date': registration_date,
        'registration_no': registration_no,
    }

    return render(request, 'certificate.html', context)

# Logout view
def logout_view(request):
    return redirect('custom_login')

# Login view
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login.html')

# Function to generate a random alphanumeric registration number
def generate_registration_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

# About view
def about(request):
    return HttpResponse("This is the about page.")

# Homepage view
@login_required(login_url='custom_login')
def homepage(request):
    user_name = request.user.username
    return render(request, 'home.html', {'user_name': user_name})

def add_interest(request):
    interest = Interest(name="Your Interest Name", price=100.00)
    interest.save()
    return HttpResponse('Interest added successfully')

def generate_certificate(request):
    image = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    draw.text((100, 100), "Certificate of Participation", fill='black', font=font)
    draw.text((100, 150), f"This is to certify that {request.user.username}", fill='black', font=font)

    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')

    response = HttpResponse(image_bytes.getvalue(), content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="certificate.png"'

    return response

   
  
