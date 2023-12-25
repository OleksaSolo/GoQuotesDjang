# GoQuotesDjang
 GoITQuotesDjango

poetry add Django
django-admin startproject quotes

cd quotes

docker run ...
edit settings.py (DB)

poetry add psycopg2
python manage.py migrate
python manage.py createsuperuser (name, email, password)

python manage.py runserver (http://127.0.0.1:8000/   http://127.0.0.1:8000/admin)

python manage.py startapp quoteapp
edit settings.py (quoteapp)

quoteapp/models.py
python manage.py makemigrations
python manage.py migrate

quoteapp/admin.py (register models)

in quoteapp md /templates/quoteapp
here index.html

quoteapp/views.py 
quotes/urls.py
quoteapp/urls.py

quotes/quoteapp/templates/quoteapp/base.html

in quotes/quotes/settings.py (STATIC_URL)

quotes/quoteapp/static/quoteapp/style.css

quotes/quoteapp/templates/quoteapp/tag.html
quotes/quoteapp/forms.py

in quotes/quoteapp/views.py (tag)
in quotes/quoteapp/urls.py (tag)

quotes/quoteapp/templates/quoteapp/author.html
add in quotes/quoteapp/forms.py
add in quotes/quoteapp/views.py
add in quotes/qoteapp/urls.py

quotes/quoteapp/templates/quoteapp/quote.html
add in quotes/quoteapp/forms.py
add in quotes/quoteapp/views.py
add in quotes/qoteapp/urls.py

python manage.py startapp users
in quotes/quotes/settings.py (add users) in INSTALLED_APPS
in quotes/urls.py (add path'users')
quotes/users/forms.py
quotes/users/views.py
in users md templates/users
users/templates/users/signup.html
quotes/users/urls.py

qwerty  ytrewq123456

edit quotes/quoteapp/models.py (add User)
python manage.py makemigrations
python manage.py migrate 

edit quotes/quoteapp/views.py (add filter(user=request.user))
in quotes/users/views.py (add profile)
in quotes/users/urls.py (add profile)
quotes/users/templates/profile.html
poetry add pillow
quotes/users/models.py
python manage.py makemigrations
python manage.py migrate

in quotes/quotes/settings.py (MEDIA)
in quotes/quotes/urls.py (static)

quotes/users/signals.py
quotes/users/apps.py
in quotes/users/forms.py (Profile)
in quotes/users/views.py (ProfileForm)

testuser2   ytrewq123456

mudule 13

quotes/quotes/settings.py (constant email)
in quotes/users/templates/users/signup.html
in quotes/users/forms.py (email)
in quotes/users/urls.py (reset password)
in quotes/users/templates/users/login.html (reset password)
in quotes/users/views.py (class reset password)
quotes/users/templates/users/password_reset.html
quotes/users/templates/users/password_reset_email.html
quotes/users/templates/users/password_reset_subject.txt
quotes/users/templates/users/password_reset_done.html
quotes/users/templates/users/password_reset_confirm.html
quotes/users/templates/users/password_reset_complete.html



