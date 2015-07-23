# custom-user-profiles

Create custom-user profiles easily with this simple app.


## Install

    pip install custom_user_profiles


## Quick start

##### add to `INSTALLED_APPS` setting

```python
INSTALLED_APPS = (
    # ...
    'custom_user',
    'custom_user_profiles
)
```

##### set `AUTH_USER_MODEL` setting

```python
AUTH_USER_MODEL = 'custom_user_profiles.CustomUser'
```

> The `CustomUser` inherit from `AbstractEmailUser` model from [django-custom-user](https://github.com/jcugat/django-custom-user)

If you want to create your own custom user

```python
from custom_user_profiles.models import AbstractCustomUser

class CustomUser(AbstractCustomUser):    
	# ...
```


##### create your profile models

```python
from custom_user_profiles.models import Profile

class Buyer(Profile):
    # ...

class Seller(Profile):
    # ...
```


## Usage

```python
@login_required
def view(request):
    profile = request.user.profile
    if request.user.is_seller:
        ...
```

Also `AbstractCustomUser` provides a **chainable** `QuerySet` manager:

```python
from django.contrib.auth import get_user_model
User = get_user_model()

User.queryset.seller() # get all users with 'seller' profile
User.queryset.buyer() # get all users with 'buyer' profile
User.queryset.something() # raises django.core.exceptions.FieldError
```

> `objects` manager is still available (e.g. `User.objects.create(...)`).
