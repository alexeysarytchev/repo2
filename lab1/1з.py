class Book:
    """
    Represents a book with its title, author, and number of pages.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book. Must be a positive integer.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Initializes a Book object.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
        Raises:
            TypeError: If any argument has an incorrect type.
            ValueError: If the number of pages is not a positive integer.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        if not isinstance(author, str):
            raise TypeError("Author must be a string.")

        if not isinstance(pages, int):
            raise TypeError("Pages must be an integer.")

        if pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")

        self.title = title
        self.author = author
        self.pages = pages

    def get_details(self) -> str:
        """
        Returns a string containing the book's details.
        Returns:
            str: A string containing the title, author, and number of pages.
        >>> book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
        >>> book.get_details()
        'Title: The Lord of the Rings, Author: J.R.R. Tolkien, Pages: 1178'
        """
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def read_chapter(self, chapter_number: int, chapter_length: int = 10) -> str:
        """
        Simulates reading a chapter of the book.
        Args:
            chapter_number (int): The chapter number to read. Must be a positive integer.
            chapter_length (int, optional): Approximate length of the chapter in pages. Defaults to 10.
        Returns:
            str: A message indicating which chapter was read.
        Raises:
            TypeError: If chapter_number or chapter_length are not integers.
            ValueError: If chapter_number or chapter_length are not positive.
        >>> book = Book("The Hobbit", "J.R.R. Tolkien", 310)
        >>> book.read_chapter(1)
        'Reading chapter 1...'
        """
        if not isinstance(chapter_number, int):
            raise TypeError("Chapter number must be an integer.")

        if not isinstance(chapter_length, int):
            raise TypeError("Chapter length must be an integer.")

        if chapter_number <= 0:
            raise ValueError("Chapter number must be a positive integer.")

        if chapter_length <= 0:
            raise ValueError("Chapter length must be a positive integer.")

        return f"Reading chapter {chapter_number}..."


class BankAccount:
    """
    Represents a bank account with a balance and account number.
    Attributes:
        account_number (str): The account number.
        balance (float): The current balance in the account. Must be non-negative.
    """

    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Initializes a BankAccount object.
        Args:
            account_number (str): The account number.
            balance (float, optional): The initial balance. Defaults to 0.0.
        Raises:
            TypeError: If the balance is not a float.
            ValueError: If the balance is negative.
        """
        self.account_number = account_number
        if not isinstance(balance, float):
            raise TypeError("Balance must be a float.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Deposits money into the account.
        Args:
            amount (float): The amount to deposit. Must be positive.
        Returns:
            float: The new balance after the deposit.
        Raises:
            TypeError: If the amount is not a float.
            ValueError: If the amount is not positive.
        >>> account = BankAccount("12345", 100.0)
        >>> account.deposit(50.0)
        150.0
        """
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws money from the account.
        Args:
            amount (float): The amount to withdraw. Must be positive and not exceed the balance.
        Returns:
            float: The new balance after the withdrawal.
        Raises:
            TypeError: If the amount is not a float.
            ValueError: If the amount is not positive or exceeds the balance.
        >>> account = BankAccount("67890", 200.0)
        >>> account.withdraw(100.0)
        100.0
        """
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance


class Tattoo:
    """
    Represents a tattoo with its design, style, size and estimated completion time.
    Attributes:
        design (str): The tattoo design description.
        style (str): The tattoo style (e.g., traditional, realism, watercolor).
        size (float): The tattoo size in square inches. Must be positive.
        hours_required (int): Estimated hours to complete. Must be positive integer.
    """

    def __init__(self, design: str, style: str, size: float, hours_required: int):
        """
        Initializes a Tattoo object.
        Args:
            design (str): The tattoo design description.
            style (str): The tattoo style.
            size (float): The tattoo size in square inches.
            hours_required (int): Estimated hours to complete.
        Raises:
            TypeError: If any argument has incorrect type.
            ValueError: If size or hours_required are not positive.
        Example:
            >>> tattoo = Tattoo("Dragon", "Japanese", 15.5, 8)
        """
        if not isinstance(design, str):
            raise TypeError("Design must be a string.")
        if not isinstance(style, str):
            raise TypeError("Style must be a string.")
        if not isinstance(size, (int, float)):
            raise TypeError("Size must be a number.")
        if not isinstance(hours_required, int):
            raise TypeError("Hours required must be an integer.")

        if size <= 0:
            raise ValueError("Size must be positive.")
        if hours_required <= 0:
            raise ValueError("Hours required must be positive.")

        self.design = design
        self.style = style
        self.size = float(size)
        self.hours_required = hours_required

    def get_details(self) -> str:
        """
        Returns a string containing the tattoo's details.
        Returns:
            str: A string with design, style, size and estimated time.
        Example:
            >>> tattoo = Tattoo("Rose", "Traditional", 8.2, 4)
            >>> tattoo.get_details()
            'Design: Rose, Style: Traditional, Size: 8.2 sq.in, Time: 4 hours'
        """
        return f"Design: {self.design}, Style: {self.style}, Size: {self.size} sq.in, Time: {self.hours_required} hours"

    def estimate_cost(self, hourly_rate: float = 150.0) -> str:
        """
        Estimates the tattoo cost based on hourly rate.
        Args:
            hourly_rate (float, optional): Artist's hourly rate. Defaults to 150.0.
        Returns:
            str: Formatted cost estimate string.
        Raises:
            TypeError: If hourly_rate is not a number.
            ValueError: If hourly_rate is not positive.
        Example:
            >>> tattoo = Tattoo("Wolf", "Realism", 20.0, 10)
            >>> tattoo.estimate_cost(200.0)
            'Estimated cost: $2000.0 (10 hours at $200.0/hour)'
        """
        if not isinstance(hourly_rate, (int, float)):
            raise TypeError("Hourly rate must be a number.")
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be positive.")

        total = self.hours_required * hourly_rate
        return f"Estimated cost: ${total} ({self.hours_required} hours at ${hourly_rate}/hour)"

    def change_size(self, new_size: float) -> str:
        """
        Updates the tattoo size and adjusts time estimate proportionally.
        Args:
            new_size (float): New size in square inches.
        Returns:
            str: Confirmation message with new details.
        Raises:
            TypeError: If new_size is not a number.
            ValueError: If new_size is not positive.
        Example:
            >>> tattoo = Tattoo("Skull", "Trash Polka", 10.0, 5)
            >>> tattoo.change_size(15.0)
            'Size updated: 15.0 sq.in. New estimated time: 7 hours'
        """
        if not isinstance(new_size, (int, float)):
            raise TypeError("Size must be a number.")
        if new_size <= 0:
            raise ValueError("Size must be positive.")

        ratio = new_size / self.size
        self.hours_required = max(1, int(round(self.hours_required * ratio)))
        self.size = new_size
        return f"Size updated: {self.size} sq.in. New estimated time: {self.hours_required} hours"
