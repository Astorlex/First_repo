import os
import sys
import shutil
import zipfile
import tarfile


def get_input_folder():
    if len(sys.argv) <= 1:
        print('Не вказаний шлях до папки')
        exit(1)

    input_folder = sys.argv[1]

    if not os.path.exists(input_folder):
        print(f'Шлях "{input_folder}" не існує')
        exit(1)

    if not os.path.isdir(input_folder):
        print(f'Шлях "{input_folder}" не є папкою')
        exit(1)

    return input_folder


CATEGORIES = {
    'images': ['.png', '.jpeg', '.svg', '.gif', '.jpg'],
    'video': ['.mov', '.mp4', '.mkv', '.avi'],
    'documents': ['.docx', '.doc', '.txt', '.pdf', '.xls', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.gz', '.zip', '.tar', '.rar', '.tgz']
}

UNKNOWN_CATEGORY = 'unknown'

TRANSLIT_DICT = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
    'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ь': '', 'ю': 'iu', 'я': 'ia',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'IE', 'Ж': 'ZH', 'З': 'Z',
    'И': 'Y', 'І': 'I', 'Ї': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P',
    'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ь': '', 'Ю': 'IU', 'Я': 'IA'
}


def normalize_char(char):
    if char in TRANSLIT_DICT:
        return TRANSLIT_DICT[char]
    elif char.isalpha() or char.isdigit():
        return char
    else:
        return '_'


def normalize(input_str):
    return ''.join(map(normalize_char, input_str))


def get_category_by_extension(ext):
    for category_name, ext_list in CATEGORIES.items():
        if ext in ext_list:
            return category_name
    
    return UNKNOWN_CATEGORY


def create_folder_if_not_exists(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


def move_file(file_path, category_folder):
    old_filename = os.path.basename(file_path)
    old_filename, ext = os.path.splitext(old_filename)
    new_filename = normalize(old_filename) if ext else old_filename
    new_filename = new_filename + ext
    old_filename = old_filename + ext

    shutil.copy(file_path, category_folder)

    old_file_path = os.path.join(category_folder, old_filename)
    new_file_path = os.path.join(category_folder, new_filename)

    os.rename(old_file_path, new_file_path)

    return new_file_path


def uncompress(archive_path):
    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r', metadata_encoding="utf-8") as zip_ref:
            zip_ref.extractall(os.path.dirname(archive_path))
        return True
    elif archive_path.endswith('.tar') or archive_path.endswith('.tar.gz') or archive_path.endswith('.tgz') or archive_path.endswith('.gz'):
        with tarfile.open(archive_path, 'r') as tar_ref:
            tar_ref.extractall(os.path.dirname(archive_path))
        return True
    else:
        print(f"Непідтримуваний тип архіву: {archive_path}")
        return False


def process_file_store(file_store, output_folder):
    create_folder_if_not_exists(output_folder)

    for category, filenames in file_store.items():
        category_folder = os.path.join(output_folder, category)
        create_folder_if_not_exists(category_folder)

        for filename in filenames:
            new_file_path = move_file(filename, category_folder)

            if category == 'archives':
                is_ok = uncompress(new_file_path)

                if is_ok:
                    os.remove(new_file_path)


def sort_folder(folder, output_folder):
    file_store = {}

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            filename = os.path.join(dirpath, filename)

            category = get_category_by_extension(ext)

            if category in file_store:
                file_store[category].append(filename)
            else:
                file_store[category] = [filename]

    process_file_store(file_store, output_folder)


def run_analytics(folder):
    supported = set(sum([ ext for ext in CATEGORIES.values() ], []))
    known = set()
    unknown = set()


    for dirpath, dirnames, filenames in os.walk(folder):
        category = os.path.basename(dirpath)

        if category in [*CATEGORIES.keys(), UNKNOWN_CATEGORY]:
            if filenames:
                print(f'Файли в {category:15}', ', '.join(filenames))
            if dirnames:
                print(f'Папки в {category:15}', ', '.join(dirnames))
            if filenames or dirnames:
                print()

        for filename in filenames:
            _, ext = os.path.splitext(filename)

            if not ext:
                ext = 'Без розширення'

            if ext not in supported:
                unknown.add(ext)
            else:
                known.add(ext)


    print()
    print('Розширення, які зустрічалися: ', ', '.join(known))
    print('Розширення, які невідомі скрипту: ', ', '.join(unknown))


def cleanup_dir(dir):
    shutil.rmtree(dir)


input_folder = get_input_folder()
parent_folder = os.path.dirname(input_folder)
output_folder = os.path.join(parent_folder, 'Sorted')

sort_folder(input_folder, output_folder)
run_analytics(output_folder)
cleanup_dir(input_folder)