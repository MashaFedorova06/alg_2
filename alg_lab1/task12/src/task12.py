from alg_lab1.utils import open_file, write_file, print_in_terminal


INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def subsequence_greedy(n, sequence):
    summa = sum(sequence)

    if summa % 2 != 0:
        return '-1'

    goal_summa = summa / 2
    current_summa = 0
    result = []

    sorted_indices = sorted(range(n), key=lambda i: sequence[i], reverse=True)

    for i in sorted_indices:
        if current_summa + sequence[i] <= goal_summa:
            current_summa += sequence[i]
            result.append(i + 1)
            if current_summa == goal_summa:
                return str(len(result)) + '\n' + ' '.join(map(str, sorted(result)))

    return '-1'


def main(input_path, output_path):
    n, numbers = open_file(input_path, 12)
    result = subsequence_greedy(n, numbers)
    print_in_terminal(([n, numbers]), result, "---Task_12 Lab_1---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
