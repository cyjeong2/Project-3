from django import forms
from diary.models import Memory, KeywordPost


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        # fields = "__all__"
        fields = ["content", "Weather", "Drawing", "Emotion"]


class KeywordForm(forms.ModelForm):
    class Meta:
        model = KeywordPost
        fields = ["content1","content2","content3", "Weather", "Drawing", "Emotion"]
