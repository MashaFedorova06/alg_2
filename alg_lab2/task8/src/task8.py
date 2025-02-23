from alg_lab2.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def get_height(node, nodes):
    if node == 0:
        return 0
    left, right = nodes[node][1], nodes[node][2]
    # Рекурсивно вычисляем высоту левого и правого поддерева
    # Выбираем максимальную
    return max(get_height(left, nodes), get_height(right, nodes)) + 1


def main(input_path, output_path):
    nodes = open_file(input_path, 8)
    result = get_height(1, nodes)
    print_in_terminal(nodes, result, "---Task_8 Lab_1---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)