from django import forms

from .models import Registrado

class RegModelFrom(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extencion = proveedor.split(".")
        if not extencion == "edu":
            raise forms.ValidationError("Por favor utiliza un email con la extencion .edu")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #Validaciones
        return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    
