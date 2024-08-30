from django.shortcuts import render, redirect
from .models import Room, Guest, Reservation, Staff, Feedback
from .forms import GuestForm, ReservationForm, FeedbackForm

def home(request):
    return render(request, 'hotel/base.html', {})

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'hotel/room_list.html', {'rooms': rooms})


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'hotel/make_reservation.html', {'form': form})

def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'hotel/staff_list.html', {'staff': staff})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'hotel/submit_feedback.html', {'form': form})

def reservation_success(request):
    return render(request, 'hotel/reservation_success.html')

def feedback_success(request):
    return render(request, 'hotel/feedback_success.html')
