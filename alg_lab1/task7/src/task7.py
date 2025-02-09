from alg_lab1.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def problema_sapozhnika(k, minutes):
    sapogi_pochineni = 0
    time = 0  # Колличество затраченного времени
    minutes_sort = sorted(minutes)
    # Итерируемся по отсортированным сапогам и добавляем их, пока не закончится время.
    for m in minutes_sort:
        if time + m <= k:
            sapogi_pochineni += 1
            time += m
        else:
            break  # Нет времени на этот сапог

    return sapogi_pochineni


def main(input_path, output_path):
    k, n, minutes = open_file(input_path, 7)
    result = problema_sapozhnika(k, minutes)
    print_in_terminal([k, n, minutes], result, "---Task_7 Lab_1---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
