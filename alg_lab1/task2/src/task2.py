from alg_lab1.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"

def min_refills(d, m, n, stops):
    stops = [0] + stops + [d]

    num_refills = 0 # Количество заправок
    current_refill = 0 # Текущая заправка

    while current_refill <= n:
        last_refill = current_refill

        while current_refill <= n and (stops[current_refill + 1] - stops[last_refill] <= m):
            current_refill += 1

        # Если не удалось сделать заправку
        if current_refill == last_refill:
            return -1

        if current_refill <= n:
            num_refills += 1

    return num_refills

def main(input_path, output_path):
    d, m, n, stops= open_file(input_path, 2)
    result = min_refills(d, m, n, stops)
    print_in_terminal([d, m, n, stops], result, "---Task_2 Lab_1---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
