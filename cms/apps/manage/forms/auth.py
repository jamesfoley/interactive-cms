from django import forms

from cms.apps.users.models import User


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    # Override for custom user authentication
    def is_valid(self):

        # Get base validation
        valid = super(LoginForm, self).is_valid()

        # If not valid we've failed at basic form validation, return
        if not valid:
            return valid

        # Passed form validation, check for a user
        try:
            # Get user object
            user = User.objects.get(email=self.cleaned_data['email'], is_staff=True)

            # Check user password
            if not user.check_password(self.cleaned_data['password']):
                raise User.DoesNotExist
            else:
                return True

        except User.DoesNotExist:

            # Failed, return false
            self.add_error('email', 'The username or password was incorrect')
            self.add_error('password', 'The username or password was incorrect')
            return False


