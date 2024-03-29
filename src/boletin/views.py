from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelFrom, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Bienvenid@"
    if request.user.is_authenticated:
        titulo = "Bienvenid@ %s" %(request.user)
    form = RegModelFrom(request.POST or None)

    context = {
        "titulo": titulo,
        "el_form": form,
    }

    if form.is_valid():
        instance = form.save(commit = False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        instance.save()

        context = {
            "titulo": "Gracias %s!" %(nombre)
        }

        if not nombre:
            context = {
                "titulo": "Gracias persona sin nombre"
            }

        print (instance)
        print (instance.timestamp)
            # form_data = form.cleaned_data
            # abc = form_data.get("email")
            # abc2 = form_data.get("nombre")
            # obj = Registrado.objects.create(email=abc, nombre=abc2)
    i = 1
    if request.user.is_authenticated and request.user.is_staff:
        queryset = Registrado.objects.all().order_by("-timestamp")
        context = {
            "queryset": queryset,
        }
    return render(request, "inicio.html",context)

def contact(request):
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
            # print (key)
            # print (form.cleaned_data.get(key))
        # for key, value in form.cleaned_data.items():
        #    print (key, value)

        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "dragoncelesty@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently = False,
        )

        # print (email, mensaje, nombre)

    context = {
        "form": form,
        "titulo": titulo,
    }
    return render(request, "forms.html", context)
