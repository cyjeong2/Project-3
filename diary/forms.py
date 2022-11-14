from django import forms
from diary.models import Memory,KeywordPost


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = "__all__"
        # fields = ["title", "content"]

class KeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordPost
        fields = "__all__"