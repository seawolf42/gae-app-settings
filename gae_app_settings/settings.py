from google.appengine.ext import ndb


UNSET = '<NOT SET>'
UNSET_MSG_FMT = 'attempt to retrieve setting {0} failed'


class AppSetting(ndb.Model):

    key = ndb.StringProperty()
    value = ndb.StringProperty()

    @staticmethod
    def get(key):
        setting = AppSetting.query(AppSetting.key == key).get()
        if not setting:
            setting = AppSetting(key=key, value=UNSET)
            setting.put()
        if setting.value == UNSET:
            raise KeyError(UNSET_MSG_FMT.format(key))
        return setting.value
