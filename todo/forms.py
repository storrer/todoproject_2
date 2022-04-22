from django import forms

from todo.models import Task, Comment
# class TaskForm(forms.Form):
#     description = forms.CharField(label='Add task', max_length=255)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].label = 'Add Task'

# ModelForm for Comment creation (rendered in detail.html)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']