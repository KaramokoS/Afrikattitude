from django import forms
from .models import Commentaire


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('Nom', 'email', 'Message', 'Téléphone')

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)

        #self.fields['body'].widget.attrs.update(title =  'Your name')
