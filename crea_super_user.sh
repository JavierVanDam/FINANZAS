echo "from django.contrib.auth import get_user_model;User = get_user_model();User.objects.create_superuser(email='javiervandam@gmail.com', password='piero')" | python manage.py shell
