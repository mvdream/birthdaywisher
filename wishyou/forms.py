from django import forms

from wishyou.models import People


class PeopleForm(forms.ModelForm):
    name = forms.CharField(label="Name:")
    email = forms.CharField(label="Email Id:")
    # birthday = forms.DateField(input_formats=['%d/%m/%Y'],
    #                            widget=forms.DateInput(attrs={
    #                                'class': 'form-control datetimepicker-input',
    #                                'data-target': '#datetimepicker1'
    #                            }))
    image = forms.ImageField(label="Image:", required=False, widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = People
        fields = ['name', 'email', 'contact', 'birthday', 'your_name', 'your_email', 'your_contact']
        widgets = {
            'birthday': forms.DateInput(attrs={'id': "datepicker", 'required': True, 'readonly': True}),
        }
