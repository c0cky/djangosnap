from tagalong_comments.models import TagalongComment
from tagalong_comments.forms import TagalongCommentForm

def get_model():
    return TagalongComment

def get_form():
    return TagalongCommentForm