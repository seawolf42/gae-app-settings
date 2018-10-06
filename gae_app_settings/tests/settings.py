import unittest

# import mock

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from ..settings import UNSET
from ..settings import AppSetting


test_key = 'aaa'
test_value = 'bbb'
test_default = 'ccc'
test_default_int = 42
test_default_int_stringified = str(test_default_int)


class AppSettingTest(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_setting_returns_value_if_set(self):
        self.setting = AppSetting(key=test_key, value=test_value)
        self.setting.put()
        self.assertEqual(AppSetting.get(test_key), test_value)

    def test_nonexisting_setting_raises_exception(self):
        with self.assertRaises(KeyError):
            AppSetting.get(test_key)

    def test_nonexisting_setting_creates_placeholder_entity(self):
        try:
            AppSetting.get(test_key)
        except KeyError:
            pass
        entity = AppSetting.query(AppSetting.key == test_key).get()
        self.assertEqual(entity.value, UNSET)

    def test_created_but_unset_settings_raises_exception(self):
        self.setting = AppSetting(key=test_key, value=UNSET)
        self.setting.put()
        with self.assertRaises(KeyError):
            AppSetting.get(test_key)

    def test_default_value_returned_if_unset(self):
        result = AppSetting.get(test_key, test_default)
        self.assertEqual(result, test_default)

    def test_default_value_returned_if_created_but_unset(self):
        self.setting = AppSetting(key=test_key, value=UNSET)
        self.setting.put()
        self.assertEqual(AppSetting.get(test_key, test_default), test_default)

    def test_default_value_does_not_replace_existing_value(self):
        self.setting = AppSetting(key=test_key, value=test_value)
        self.setting.put()
        self.assertEqual(AppSetting.get(test_key, test_default), test_value)

    def test_default_value_does_not_replace_unset_value(self):
        self.setting = AppSetting(key=test_key, value=UNSET)
        self.setting.put()
        AppSetting.get(test_key, test_default)
        with self.assertRaises(KeyError):
            AppSetting.get(test_key)

    def test_default_value_returned_is_string(self):
        result = AppSetting.get(test_key, test_default_int)
        self.assertIsInstance(result, str)
        self.assertEqual(result, test_default_int_stringified)

    def test_return_none_instead_of_exception(self):
        result = AppSetting.get(test_key, raise_exception=False)
        self.assertEqual(result, None)

    def test_no_exception_and_default(self):
        result = AppSetting.get(test_key, default=test_default, raise_exception=False)
        self.assertEqual(result, test_default)

    def test_no_exception_and_saved(self):
        self.setting = AppSetting(key=test_key, value=test_value)
        self.setting.put()
        self.assertEqual(AppSetting.get(test_key, raise_exception=False), test_value)
