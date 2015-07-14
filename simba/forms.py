from django import forms
from django.contrib.auth.models import User
from simba.models import Course, UserProfile, BetaCode, Role

class BetaCodeForm(forms.ModelForm):

	email = forms.EmailField(label="Indirizzo email")


	
    # An inline class to provide additional information on the form.
    	class Meta:
        # Provide an association between the ModelForm and a model
        	model = BetaCode
        	exclude = ('code', 'gen_date','valid',)

class RoleForm(forms.ModelForm):
	OPTIONS = (('Normal', 'Normal'),('Board', 'Board'),)

	name = forms.CharField(max_length=128, label="Ruolo")
	label = forms.MultipleChoiceField(choices=OPTIONS, label="Etichetta")
	#label = forms.CharField(max_length=128, label="Normal/Board")

	
    # An inline class to provide additional information on the form.
    	class Meta:
        # Provide an association between the ModelForm and a model
        	model = Role
        	fields = ('name','label')


	

class CourseForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the course type.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course
        fields = ('name',)


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields =('username', 'email','first_name', 'last_name', 'password')

class UserProfileForm(forms.ModelForm):
    birthplace = forms.CharField(max_length = 128,  help_text="Please enter the user birthplace.")
    provincia = forms.CharField(max_length = 10, help_text="Please enter the user bp district.")
    lives = forms.CharField(max_length = 128, help_text="Please enter the user'scurrent city")
    birthdate = forms.DateTimeField()
    address = forms.CharField(max_length = 128)
    phone = forms.CharField(max_length = 128)
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    is_fc = forms.BooleanField(label="Fuoricorso");
    


    class Meta:
    # Provide an association between the ModelForm and a model
        model = UserProfile
	
	        # What fields do we want to include in our form?
	        # This way we don't need every field in the model present.
	        # Some fields may allow NULL values, so we may not want to include them...
	        # Here, we are hiding the foreign key.
	        # we can either exclude the category field from the form,
        exclude = ('user', 'role','date','status', 'wifi_access', 'wifi_pending', 'avatar' )
    	    #or specify the fields to include (i.e. not include the category field)
    	    #fields = ('title', 'url', 'views')

