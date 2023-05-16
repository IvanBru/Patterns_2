class UserSettingsMemento:
    def __init__(self, notification_settings):
        self.notification_settings = dict(notification_settings)

    def get_notification_settings(self):
        return self.notification_settings.copy()