from django.contrib.auth.views import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n in dir(self):
            print(n)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )
