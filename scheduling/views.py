from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Creature, TimeSlot, Booking

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('choose_creature')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('choose_creature')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def choose_creature(request):
    if hasattr(request.user, 'booking'):
        return redirect('my_booking')
    creatures = Creature.objects.all()
    return render(request, 'choose_creature.html', {'creatures': creatures})

@login_required
def choose_slot(request, creature_id):
    if hasattr(request.user, 'booking'):
        return redirect('my_booking')
    creature = Creature.objects.get(id=creature_id)
    slots = TimeSlot.objects.all()
    available_slots = [s for s in slots if s.spots_left() > 0]
    return render(request, 'choose_slot.html', {
        'creature': creature,
        'slots': available_slots
    })
