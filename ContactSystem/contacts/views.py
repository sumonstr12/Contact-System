from django.shortcuts import render, redirect
from django.http import Http404
from .models import Contact
from .forms import ContactForm

# View to list all contacts
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'templates/home.html', {'contacts': contacts})

# View to add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'templates/add_contact.html', {'form': form})

# View to edit a contact
def edit_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        raise Http404("Contact not found")

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'templates/edit_contact.html', {'form': form})

# View to delete a contact
def delete_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        raise Http404("Contact not found")

    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'templates/delete_contact.html', {'contact': contact})
