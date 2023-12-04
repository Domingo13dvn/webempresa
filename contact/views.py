from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.

def contact(request):
    contact_form=ContactForm()

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            content = request.POST.get('content')
            mail=EmailMessage("Mensaje de app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name, mail, content), 
            '',
            ["mingovela13@gmail.com"], 
            reply_to=[mail])

            try:
                mail.send()
             
                return render(request, "core/base.html")
                
            except:
                return render(request, "contact/contact.html", {'miFormulario': contact_form})

    return render(request, "contact/contact.html", {'miFormulario': contact_form})

