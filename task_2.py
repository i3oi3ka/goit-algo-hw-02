# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги
# (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом.
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
# а також бути нечутливою до регістру та пробілів.

from collections import deque


def is_palindrom(text: str) -> bool:
    data = text.lower().replace(" ", "")
    queue = deque(data)
    while len(queue) > 1:
        if queue.pop() != queue.popleft():
            return False
    return True


print(is_palindrom(input("Enter text: ")))
