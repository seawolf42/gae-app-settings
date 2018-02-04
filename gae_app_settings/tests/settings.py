import unittest

# import mock

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from ..settings import UNSET
from ..settings import AppSetting


test_key = 'aaa'
test_value = 'bbb'


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
