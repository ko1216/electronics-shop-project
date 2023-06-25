from src.item import Item


class MixinLang:

    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
            return self
        else:
            self._language = 'EN'
            return self


class Keyboard(MixinLang, Item):
    pass
