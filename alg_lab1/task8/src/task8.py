from alg_lab1.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def max_lectures(requests):
    requests.sort(key=lambda x: x[1])
    end = 0  # Время окончания последней лекции
    lectures = 0 # Счетчик лекций

    # Проходим по каждому запросу в списке
    for i in requests:
        if i[0] >= end:
            lectures += 1
            end = i[1]
    return lectures


def main(input_path, output_path):
    requests = open_file(input_path, 8)
    result = max_lectures(requests)
    print_in_terminal(requests, result, "---Task_8 Lab_1---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
