from django import forms
from doct.app.models import Task, Contribute


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'link']


class ContributeForm(forms.ModelForm):
    class Meta:
        model = Contribute
        fields = ['ram', 'cpu', 'gpu', 'disk_space']
