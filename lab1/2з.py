from task_1 import Book, BankAccount, Tattoo

if __name__ == "__main__":
    try:
        book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
        account = BankAccount("98765", 500.0)
        tattoo = Tattoo("Dragon", "Japanese", 15.5, 8)
    except Exception as e:
        print(f"Ошибка при создании объекта: {e}")

    try:
        book.read_chapter(-1)  # Вызвать метод с некорректным номером главы
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    try:
        account.deposit(-100)  # Вызвать метод с некорректной суммой депозита
    except ValueError as e:
        print(f"Ошибка: неправильные данные")

    try:
        tattoo.change_size(-5)  # Некорректный размер татуировки
    except ValueError as e:
        print(f"Ошибка в татуировке: {e}")
