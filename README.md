# custom-user-profiles

Create custom-user profiles easily with this simple app.


## Install

    pip install custom_user_profiles


## Quick start

#### add to `INSTALLED_APPS` setting

```python
INSTALLED_APPS = (
    # ...
    'custom_user',
    'custom_user_profiles
)
```

#### set `AUTH_USER_MODEL` setting

```python
AUTH_USER_MODEL = 'custom_user_profiles.CustomUser'
```

> The `CustomUser` inherit from `AbstractEmailUser` model from [django-custom-user](https://github.com/jcugat/django-custom-user)

If you want to create your own custom user, extend `custom_user_profiles.models.AbstractCustomUser`.

```python
from custom_user_profiles.models import AbstractCustomUser

class CustomUser(AbstractCustomUser):    
	# ...
```

#### create your profile models

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

