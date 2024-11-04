from django import forms
from django.forms import SelectMultiple, TextInput, Textarea
from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label = "Kurs Başlığı",
#         error_messages={
#             "required": "Kurs Başlığı Girmelisiniz."}, 
#         widget = forms.TextInput(attrs={"class": "form-control"}))
        
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control"}))
#     slug = forms.SlugField(widget = forms.TextInput(attrs={"class": "form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            "title": "Kurs Başlığı",
            "description": "Açıklama"
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required": "Kurs Başlığı Girmelisiniz.",
                "max_length": "Maksimum 50 Karakter Girmelisiniz."
            },
            "description": {
                "required": "Kurs Açıklaması Gereklidir."
            }
        }


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'imageUrl', 'slug', 'categories', 'isActive')
        labels = {
            "title": "Kurs Başlığı",
            "description": "Açıklama"
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "categories": SelectMultiple(attrs={"class": "form-control"})
        }
        error_messages = {
            "title": {
                "required": "Kurs Başlığı Girmelisiniz.",
                "max_length": "Maksimum 50 Karakter Girmelisiniz."
            },
            "description": {
                "required": "Kurs Açıklaması Gereklidir."
            }
        }
