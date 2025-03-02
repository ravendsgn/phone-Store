from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone
from .forms import PhoneForm


def home(request):
    phones = Phone.objects.all().order_by('-id')
    return render(request, 'store/home.html', {'phones': phones})


def phone_detail(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    return render(request, 'store/detail.html', {'phone': phone})


def add_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PhoneForm()
    return render(request, 'store/add_phone.html', {'form': form})


def edit_phone(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_detail', phone_id=phone.id)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'store/edit_phone.html', {'form': form, 'phone': phone})


def delete_phone(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    if request.method == 'POST':
        phone.delete()
        return redirect('home')
    return render(request, 'store/delete_phone.html', {'phone': phone})
