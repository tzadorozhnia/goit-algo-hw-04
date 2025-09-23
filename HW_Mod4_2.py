def get_cats_info(f_path: str) -> list[dict]:
    """
    Читає текстовий файл з інформацією про котів та повертає список словників.

    :param f_path: Шлях до текстового файлу.
                 Файл має містити дані у форматі:
                 id,name,age (кожен запис у новому рядку).
    :return: Список словників з інформацією про котів.
             Кожен словник має структуру:
             {
                 "id": <рядок>,
                 "name": <рядок>,
                 "age": <рядок>
             }
    """
    cats_info = []
    try:
        with open(f_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Неправильний формат рядка: {line}")
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")

    return cats_info


cats_info = get_cats_info('D:/cats_file.txt')
print(cats_info)
