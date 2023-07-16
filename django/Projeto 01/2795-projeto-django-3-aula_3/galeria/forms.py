from django import forms


from galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    class meta:
        model = Fotografia 

        exclude = ['publicada',]
        widgets = {
            'nome': forms.TextInput(attrs={'Class':'form-control'}),
            'legenda': forms.TextInput(attrs={'Class':'form-control'}),
            'categoria': forms.TextInput(attrs={'Class':'form-control'}),
            'legenda': forms.Textarea(attrs={'Class':'form-control'}),
            'foto ': forms.FileInput(attrs={'Class':'form-control'}),
            'data_fotografia': forms.DateInput(attrs={'Class':'form-control','type':'date'},format='%d/%m/%Y',),
            'usuario ': forms.Select(attrs={'Class':'form-control'}),
        }
        