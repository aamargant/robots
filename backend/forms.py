from django import forms

class robotsForm(forms.Form):
    website = forms.CharField(help_text="Enter the wbesite to get the robotos.txt from (default: capterra.com)")