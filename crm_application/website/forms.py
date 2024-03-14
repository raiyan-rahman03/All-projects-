from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import student_record
from.models import result

class SignUpForm(UserCreationForm):
    first_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'First Name'}) ,label="")
    last_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Email address'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class addrecord(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last name", "class": "form-control"}), label="")
    roll_no = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Roll Number (Must be integer)", "class": "form-control"}), label="")
    grade_level = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Grade Level", "class": "form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email (Enter a valid email)", "class": "form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"}), label="")
    class_room_no = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Class Room Number", "class": "form-control"}), label="")
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control"}), label="Upload an Image")
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={"placeholder": "Date of Birth (YEAR-MONTH-DATE)", "class": "form-control"}), label="")

    class Meta:
        model = student_record
        fields = ("first_name", "last_name", "roll_no", "grade_level", "email", "phone", "address", "class_room_no", "image", "date_of_birth")



class AddResultForm(forms.ModelForm):
    gpa = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "GPA score", "class": "form-control"}),
        label=""
    )
    bangla = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Bangla score", "class": "form-control"}),
        label=""
    )
    english = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "English score", "class": "form-control"}),
        label=""
    )
    math = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Math score", "class": "form-control"}),
        label=""
    )
    physics = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Physics score", "class": "form-control"}),
        label=""
    )
    biology = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Biology score", "class": "form-control"}),
        label=""
    )
    chemistry = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Chemistry score", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = result
        fields = ("gpa", "bangla", "english", "math", "physics", "biology", "chemistry")

