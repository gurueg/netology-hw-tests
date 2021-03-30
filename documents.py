documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def user_help():
    print("'p'    – Поиск имени человека по номеру документа")
    print("'s'    – Поиск расположения документа на полке по номеру документа")
    print("'l'    - Вывод списка всех документов")
    print("'a'    - Добавление нового документа")
    print("'d'    – Удаление документ по номеру")
    print("'m'    - Перемещение документа на другую полку")
    print("'as'   - Добавление новой полки")
    print("'q'    - Завершение работы программы")
    print("'help' - Вывод справки по командам программы")
    print()


def get_document_owner_name(documents_list, doc_number):
    for document in documents_list:
        if (document["number"] == doc_number):
            return document["name"]

    return


def get_document_shelf(directories_dict, doc_number):
    for shelf in directories_dict.keys():
        if doc_number in directories_dict[shelf]:
            return shelf
    return


def print_documents_list(documents_list):
    for document in documents_list:
        print(document['type'], f"'{document['number']}'", document["name"])


def is_document_exists(documents_list, doc_number, doc_type=None):
    for document in documents_list:
        if document['number'] == doc_number and\
                document['type'] == doc_type or\
                document['number'] == doc_number and doc_type is None:
            return True
    return False


def add_document(documents_list, directories_dict):
    doc_number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    if (is_document_exists(documents_list, doc_number, doc_type)):
        print(f"Документ с номером {doc_number} типа {doc_type} уже существует!")
        return

    doc_owner = input("Введите имя владельца: ")
    shelf_number = input("Введите номер полки: ")

    if shelf_number not in directories_dict.keys():
        print(f"Полки номер {shelf_number} не существует")
        print("'y' - добавить новую полку и поместить туда документ")
        print("'n' - документ будет помещен на полку номер 1")

        user_command = input("Добавить новую полку?(y/n) ")
        if user_command == 'y':
            add_new_shelf(directories_dict, shelf_number)
        else:
            shelf_number = '1'

    documents_list.append({
        "type": doc_type,
        "number": doc_number,
        "name": doc_owner
    })
    directories_dict[shelf_number].append(doc_number)
    print("Документ успешно добавлен")
    return True


def delete_document(documents_list, directories_dict):
    doc_number = input("Введите номер документа для удаления: ")
    if not is_document_exists(documents_list, doc_number):
        print(f"Документа с номером {doc_number} не существует!")
        return

    for document in documents_list:
        if document["number"] == doc_number:
            doc_to_remove = document
    documents_list.remove(doc_to_remove)

    shelf_number = get_document_shelf(directories_dict, doc_number)
    directories_dict[shelf_number].remove(doc_number)
    print("Документ успешно удален")
    return True


def move_document(directories_dict):
    doc_number = input("Введите номер документа для перемещения: ")
    shelf_current = get_document_shelf(directories_dict, doc_number)
    if shelf_current is None:
        print(f"Документа с номером {doc_number} не существует!")
        return

    shelf_new = input("Введите номер полки: ")
    if shelf_new not in directories_dict.keys():
        print(f"Полки номер {shelf_new} не существует")
        user_command = input("Добавить новую полку?(y/n) ")
        if user_command == 'y':
            add_new_shelf(directories_dict, shelf_new)
        else:
            print("Команда не выполнена, несуществующая полка")
            return

    directories_dict[shelf_current].remove(doc_number)
    directories_dict[shelf_new].append(doc_number)
    print("Документ успешно перемещен")
    return True


def add_new_shelf(dir_dict, new_shelf=None):
    if new_shelf is None:
        new_shelf = input("Введите номер полки: ")

    if new_shelf in dir_dict.keys():
        print("Такая полка уже существует! Новая полка добавлена не будет")
        return

    dir_dict[new_shelf] = list()
    print("Новая полка добавлена")
    return new_shelf


def main(doc_list, dir_dict):
    user_help()
    while True:
        user_command = input("Введите команду: ")
        if user_command == 'p':
            number = input('Введите номер документа: ')
            owner = get_document_owner_name(doc_list, number)

            if (owner is not None):
                print(f'Владелец документа номер {number} - {owner}')
            else:
                print('Документа с таким номером не существует')
            print()

        elif user_command == 's':
            number = input('Введите номер документа: ')
            shelf_number = get_document_shelf(dir_dict, number)
            if (shelf_number is not None):
                print(f'Документ номер {number} хранится на полке номер {shelf_number}')
            else:
                print('Документ с таким номером на полках отсутствует')
            print()

        elif user_command == 'l':
            print_documents_list(doc_list)
            print()

        elif user_command == 'a':
            add_document(doc_list, dir_dict)
            print()

        elif user_command == 'd':
            delete_document(doc_list, dir_dict)
            print()

        elif user_command == 'm':
            move_document(dir_dict)
            print()

        elif user_command == 'as':
            add_new_shelf(dir_dict)
            print()

        elif user_command == 'help':
            user_help()
            print()

        elif user_command == 'q':
            break
        else:
            print('Несуществующая команда, повторите ввод')
            print()


if __name__ == '__main__':
    unittest.main()
    # main(documents, directories)
