from django.shortcuts import render
from .models import User
from django.contrib import messages

def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        DOB = request.POST["dob"]
        gender = request.POST["gender"]
        address = request.POST["address"]

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Choose a different one.")
            return render(request, "register.html")

        # Create user
        User.objects.create(
            username=username,
            password=password,
            DOB=DOB,
            gender=gender,
            address=address
        )

        users = User.objects.all()
        return render(request, "success.html", {"users": users})

    return render(request, "register.html")
