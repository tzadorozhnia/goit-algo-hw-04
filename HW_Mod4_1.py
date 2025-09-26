def total_salary(f_path: str) -> tuple[float, float]:
    """
        Розраховує загальну та середню заробітну плату розробників на основі текстового файлу.
        Файл повинен містити рядки у форматі:
                <Прізвище Ім'я>,<зарплата>
            Наприклад:
                Alex Korp,3000
                Nikita Borisenko,2000
                Sitarama Raju,1000
       :param f_path: шлях до текстового файлу з даними про зарплати
       :return: tuple[float, float]: кортеж, що містить:
            - total (float): загальну суму заробітних плат;
            - average (float): середню заробітну плату.
        При виникненні проблем при читанні файла total та average ==0
       """

    try:
        with open(f_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
        if not lines:
            print("Файл порожній.")
            return 0, 0
        total_local = 0
        quantity = len(lines)
        for line in lines:
            s_line = line.split(',')
            if len(s_line) == 2:
                try:
                    total_local = total_local + float(s_line[1])
                except ValueError:
                    total_local = total_local
        try:
            average_local = float(total_local / quantity)
        except ZeroDivisionError:
            print("Помилка: ділення на нуль!")
            return 0, 0
        else:
            return total_local, average_local
    except FileNotFoundError:
        print(f"Помилка: файл '{f_path}' не знайдено.")
        return 0, 0
    except IOError:
        print(f"Помилка: файл '{f_path}' не вдалося прочитати.")
        return 0, 0


total, average = total_salary('D:/test.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
