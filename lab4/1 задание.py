class Notebook:
    """Базовый класс для блокнотов."""

    def __init__(self, brand: str, model: str, pages: int):
        """
        Инициализация блокнота.
        :param brand: Бренд блокнота.
        :param model: Модель блокнота.
        :param pages: Количество страниц.
        """
        self._brand = brand
        self._model = model
        self._pages = pages

    @property
    def brand(self) -> str:
        """Бренд блокнота."""
        return self._brand

    @property
    def model(self) -> str:
        """Модель блокнота."""
        return self._model

    @property
    def pages(self) -> int:
        """Количество страниц в блокноте."""
        return self._pages

    def write(self, text: str) -> str:
        """
        Запись текста в блокнот.
        :param text: Текст для записи.
        :return: Сообщение о записи текста.
        """
        return f"Текст '{text}' записан в блокнот."

    def __str__(self) -> str:
        """Строковое представление блокнота."""
        return f"Блокнот {self.brand} {self.model}, {self.pages} страниц."

    def __repr__(self) -> str:
        """Официальное строковое представление блокнота."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, pages={self.pages!r})"


class ElectronicNotebook(Notebook):
    """Класс для электронных блокнотов."""

    def __init__(self, brand: str, model: str, battery_life: float):
        """
        Инициализация электронного блокнота.
        :param brand: Бренд блокнота.
        :param model: Модель блокнота.
        :param battery_life: Время работы от батареи в часах.
        """
        super().__init__(brand, model, pages=0)  # Электронные блокноты не имеют физических страниц
        self._battery_life = battery_life

    @property
    def battery_life(self) -> float:
        """Время работы от батареи в часах."""
        return self._battery_life

    def write(self, text: str) -> str:
        """
        Запись текста в электронный блокнот.
        Перегрузка метода write для добавления специфического поведения для электронных блокнотов.
        В электронных блокнотах текст записывается цифровым способом.
        :param text: Текст для записи.
        :return: Сообщение о записи текста.
        """
        return f"Текст '{text}' записан в электронный блокнот."

    def __str__(self) -> str:
        """Строковое представление электронного блокнота."""
        return f"Электронный блокнот {self.brand} {self.model}, время работы от батареи: {self.battery_life:.2f} часов."

    def __repr__(self) -> str:
        """Официальное строковое представление электронного блокнота."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"battery_life={self.battery_life:.2f})")
