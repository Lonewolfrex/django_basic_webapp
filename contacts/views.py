from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def list_contacts(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contacts/list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return redirect('contacts:list')  # ✅ fixed
    return render(request, 'contacts/add.html', {'form': form})

@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:list')  # ✅ fixed
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/edit.html', {'form': form})

@login_required
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == "POST":
        contact.delete()
        return redirect('contacts:list')  # Redirect to contacts list after deletion

    # If GET request, show confirmation page
    return render(request, 'contacts/delete.html', {'contact': contact})
