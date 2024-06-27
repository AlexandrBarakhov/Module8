class InvalidDataException(Exception):  # исключение, вызываемое при получении некорректных данных
    def __init__(self, message):
        super().__init__(message)


class ProcessingException(Exception):  # исключение, вызываемое при возникновении ошибки во время обработки
    def __init__(self, message):
        super().__init__(message)


def process_data(data):  # функция, обрабатывающая данные и генерирующая исключения
    if data is None:
        raise InvalidDataException("Данные не могут быть None.")
    if not isinstance(data, list):
        raise InvalidDataException("Данные должны быть списком.")
    if len(data) > 10:
        raise InvalidDataException("Длина списка не должна превышать 10 элементов.")
    return data


def analyze_data(data):  # функция, анализирующая данные и передающая исключения
    try:
        processed_data = process_data(data)
    except InvalidDataException as e:
        print(f"Ошибка валидации данных: {e}")
        raise  # Передача исключения дальше
    except ProcessingException as e:
        print(f"Ошибка обработки данных: {e}")
        raise  # Передача исключения дальше
    else:
        print("Данные успешно обработаны.")
        return processed_data
    finally:
        print("Завершение анализа данных.")


def calculations(data):  # функция, вычисляющая среднее значение
    try:
        if not data:
            raise ProcessingException("Невозможно вычислить среднее значение для пустого списка.")
        average = sum(data) / len(data)
        print(f"Среднее значение: {average}")
    except TypeError:
        raise InvalidDataException("Список содержит элементы нечислового типа.")


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # корректные данные
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  # список из 11 элементов: вызовет исключение
        None,  # недопустимые данные: None
        "string",  # недопустимые данные: строка
        [],  # пустой список
        [1, 2, 'a', 4, 5],  # недопустимые данные: список содержит строку
    ]

    for i, test_data in enumerate(test_cases):
        print(f"\nТест {i + 1} с данными: {test_data}")
        try:
            result = analyze_data(test_data)
            if result is not None:
                calculations(result)
        except (InvalidDataException, ProcessingException) as e:
            print(f"Поймано исключение в главной функции: {e}")
