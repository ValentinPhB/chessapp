
class MenuEntry:
    def __init__(self, option, handler):
        self._option = option
        self.handler = handler

    def __repr__(self):
        return f'MenuEntry({self._option}, {self.handler})'

    def __str__(self):
        return str(self._option)


class Menu:
    def __init__(self):
        self._entries = {}
        self._autokey = 1

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]

    def add(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1

        self._entries[str(key)] = MenuEntry(option, handler)

    def items(self):
        return self._entries.items()
