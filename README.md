# Google AppEngine App Settings

This package provies a straightforward way to store and access environment-specific and secret/private variables in the Google App Engine Datastore.


## Quick start

Install `gae_app_settings`:

    $ pip install gae_app_settings

In your settings module or some other module that loads at startup:

```python
from gae_app_settings import AppSetting
MY_SETTING = AppSetting.get('MY_SETTING_KEY')
```

The first time you try to retrieve a key from AppSettings, the `get()` call will raise a `KeyError` and a placeholder entry will be created in the datastore. Once the placeholder has been replaced with a value in the datastore the call to `get()` will succeed.
