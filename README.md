# Google AppEngine App Settings

This package provies a straightforward way to store and access environment-specific and secret/private variables in the Google App Engine Datastore.


## Quick start

Install `gae_app_settings`:

    $ pip install gae_app_settings

In your settings module or some other module that loads at startup:

```python
from gae_app_settings import AppSetting
value = AppSetting.get('MY_SETTING_KEY', DEFAULT_VALUE)
```



## Full documentation

AppSetting is a class that is used to persist/store sensitive values in your environment. It is designed to work just like a dictionary, but it is limited to just string values.

Settings cannot be set programmatically, they are only retrievable:

```python
value = AppSetting.get('MY_SETTING_KEY', DEFAULT_VALUE)
```

**NOTE:** regardless of the type of `DEFAULT_VALUE `, `value` will always be a string. This is to ensure that the return value is of the same type whether the setting is set or unset, as a set value will be a string.

You can also retrieve values without passing a default:

```python
value = AppSetting.get('MY_SETTING_KEY')
```

**Note:** If no default value is provided and the key has not been given a value in the datastore, the `get()` call will raise a `KeyError` and a placeholder entry will be created in the datastore. Once the placeholder has been replaced with a value future calls to `get()` will succeed.


## Best practices

The following best practices are recommended:

1. Settings should be loaded at program start and stored locally in a `settings.py` or similar module
1. Default values should be provided for every setting:
    1. these should be the values that make sense when running/testing locally
    1. placeholders will be inserted into the Datastore, and these only need to be overwritten if there are environment-specific settings that need to be set (in production, all values should be set)
1. Do not change the type of the `value` property in the datastore; coersion should happen on the result of the call to `get()`
