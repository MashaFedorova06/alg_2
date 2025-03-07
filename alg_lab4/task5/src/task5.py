from alg_lab4.utils import open_file, write_file, print_in_terminal


INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def prefix_function(s):
    n = len(s)
    prefix = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j

    return prefix



def main(input_path, output_path):
    data = open_file(input_path, 5)
    result = " ".join(map(str, prefix_function(data)))
    print_in_terminal(data, result, "---Task_5 Lab_4---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
