from django.conf import settings
settings.configure()
from django.contrib.auth import get_user_model

User = get_user_model()


from usuarios.models import Usuario

user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'John'
user.last_name = 'Citizen'
user.save()