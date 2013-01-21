from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField()
    text = forms.CharField ( widget=forms.Textarea )
    
    def clean_title(self):
        cd = self.cleanded_data
        title = cd.get('title')
        
        if len(title) < 3:
            raise forms.validationError('Please title more then two chars')    
            return title
        
    def clean_text(self):
        cd = self.cleaned_data
        text = cd.get('text')
        
        if len(text) < 10:
            raise forms.ValidationError('Pease more text:)')
        return text
    
    def clean(self):
        cd = self.cleaned_data
        email = cd.get('mail')
        title = cd.get ('title')
        
        if mail == title:
            raise forms.ValidationError('Title should not be an email')
        
        return cd
        
        