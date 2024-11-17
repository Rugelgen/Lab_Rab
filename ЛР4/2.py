# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def perevod_csv_v_json(filename) -> None:
    import csv
    import json
    data = []
    # TODO считать содержимое csv файла

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for i in reader:
            data.append(i)
            with open(OUTPUT_FILENAME, "w+") as out:
                json.dump(data, out, indent=4)
    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


