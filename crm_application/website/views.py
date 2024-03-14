# website/views.py
from .models import student_record
from .forms import addrecord  # Import your form
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from . models import student_record
from .forms import addrecord
from . models import result


def home(request):
    record = student_record.objects.all()

    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):

            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')

        else:
            messages.success(
                request, "Sorry, there was an error. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {"data": record})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfuly logged out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def indivitual_data(request, pk):
    if request.user.is_authenticated:
        records = student_record.objects.get(id=pk)
        return render(request, 'indivitual.html', {'indivitual': records})
    else:
        messages.success(
            request, "Sorry, You have to login to view the individual data")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = student_record.objects.get(id=pk)
        record.delete()
        messages.success(request, "The record have successfully deleted.....")
        return redirect('home')
    else:
        messages.success(
            request, "Sorry, You have to login to delete a record ")
        return redirect('home')


def add_record(request):
    if request.method == 'POST':
        # Include request.FILES to handle file uploads
        form = addrecord(request.POST, request.FILES)
        if form.is_valid():
            # Create a record instance but don't save it yet
            record = form.save(commit=False)

            # Assuming 'image' is the name of the file input field in the form
            if 'image' in request.FILES:
                record.image = request.FILES['image']

            record.save()  # Save the record with the image

            messages.success(
                request, "The record has been successfully added.")
            return redirect('home')
        else:
            messages.error(
                request, "Check your form again. Make sure you've provided valid information.")
            return render(request, 'add_record.html', {'form': form})
    else:
        form = addrecord()
    return render(request, 'add_record.html', {'form': form})


def update(request, pk):
    if request.user.is_authenticated:
        record = student_record.objects.get(id=pk)

        if request.method == 'POST':
            form = addrecord(request.POST, request.FILES, instance=record)

            if form.is_valid():
                if 'image' in request.FILES:
                    # Update the image only if a new file is uploaded
                    record.image = request.FILES['image']
                form.save()
                messages.success(request, 'Successfully Updated')
                return redirect('home')

        else:
            form = addrecord(instance=record)

        return render(request, 'update.html', {'form': form})
    else:
        messages.success(
            request, "Sorry, You have to login to Update a record ")
        return redirect('home')



def update(request, pk):
    result = result.objects.get(id=pk)
    return render(request, 'update.html', {'reult': result})
