from django.shortcuts import render, get_object_or_404, redirect
from .models import contacts
from .forms import ContactForm

# Create your views here.

def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('contacts:contact-change', id=instance.id)
    else:
        print(form.errors)
    context = {
        'form': form
    }
    return render(request, "contact_create.html", context)

def contact_detail_view(request, id):
    obj = get_object_or_404(contacts, id=id)
    context = {
        "object": obj
    }
    return render(request, "contact_detail.html", context)

#def contact_update_view(request, id=id):
#    obj = get_object_or_404(contacts, id=id)
#    form = ContactForm(request.POST or None, instance=obj)
#    if form.is_valid():
#        contact_instance = form.cleaned_data
#        contact_instance.save(commit=True)
#        return redirect('contacts:contact-detail', id=instance.id)
#    context = {
#        'form': form
#    }
#    return render(request, "contact_create.html", context)

# update view for details
#def contact_edit_view(request, id):
#    # dictionary for initial data with
#    # field names as keys
#    context ={}
#
#    # fetch the object related to passed id
#    obj = get_object_or_404(contacts, id = id)
#
#    # pass the object as instance in form
#    form = ContactForm(request.POST or None, instance = obj)
#
#    # save the data from the form and
#    # redirect to detail_view
#    if form.is_valid():
#        contact_instance = form.save(commit=False)
#        contact_instance.save()
#        return redirect('contacts:contact-edit', id=contact_instance.id)

    # add form dictionary to context
#    context["form"] = form

#    return render(request, "contact_create.html", context)
def contact_change_view(request, id):
    context = {}
    obj = get_object_or_404(contacts, id = id)
    form = ContactForm(request.POST or None, instance = obj)
    if form.is_valid():
        #instance = form.save(commit=False)
        instance = form.save()
        return redirect('contacts:contact-details', instance.id)
    else:
        print(form.errors)
    context = {
        'form': form
    }
    return render(request, "contact_change.html", context)
