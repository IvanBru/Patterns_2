from user_settings import UserSettings
from user_settings_caretaker import UserSettingsCaretaker

user_settings = UserSettings()
caretaker = UserSettingsCaretaker(user_settings)
user_settings.set_notification_setting("Email", True)
user_settings.set_notification_setting("SMS", False)
caretaker.save_settings()
user_settings.set_notification_setting("Push", True)
caretaker.save_settings()
caretaker.undo_settings()