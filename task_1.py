
import os
import shutil
import argparse

def process_directory(path, destination_dir):
    # Перебираємо всі елементи у директорії
    for item in os.listdir(path):
        item_path = os.path.join(path, item)  # шлях до поточного елементу

    # Якщо елемент є директорією, викликаємо функцію рекурсивно
        if os.path.isdir(item_path):
            process_directory(item_path, destination_dir)
        else:
    # Якщо елемент є файлом, він копіюється
            print(f"Обробка файлу: {item_path}")
            try:
                shutil.copy2(item_path, destination_dir)
            except Exception as e:
                print(f"Не вдалося скопіювати файл:{item_path}:{e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Дерево директорії")
    parser.add_argument('path', type=str, help="Шлях вихідна директорія")
    parser.add_argument('destination_dir', nargs='?', type=str, default='dist', help="Шлях кінцева директорія (за замовч.: dist)")
    args = parser.parse_args()


