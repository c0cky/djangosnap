from django import forms
from django_comments.forms import CommentForm
from tagalong_comments.models import TagalongComment

class TagalongCommentForm(CommentForm):
    # up_vote = forms.IntegerField()
    # down_vote = forms.IntegerField()

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return TagalongComment

    # def get_comment_create_data(self):
    #     # Use the data of the superclass, and add in the title field
    #     data = super(TagalongCommentForm, self).get_comment_create_data()
    #     data['up_vote'] = self.cleaned_data['up_vote']
    #     data['down_vote'] = self.cleaned_data['down_vote']
    #     return data