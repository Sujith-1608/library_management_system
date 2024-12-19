from django import forms
from .models import Library
from student.models import Student
from book.models import Book

class LibraryForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Select Student")
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label="Select Book")
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Library
        fields = ['student', 'book', 'start_date', 'end_date']


