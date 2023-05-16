from user_settings import UserSettings

class UserSettingsCaretaker:
    def __init__(self, user_settings):
        self.user_settings = user_settings
        self.mementos = []

    def save_settings(self):
        memento = self.user_settings.create_memento()
        self.mementos.append(memento)

    def undo_settings(self):
        if len(self.mementos) > 1:
            memento = self.mementos.pop()
            self.user_settings.restore_from_memento(self.mementos[-1])