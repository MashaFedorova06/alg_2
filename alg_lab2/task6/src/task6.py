from alg_lab2.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"

def is_valid_bst(nodes):
    """Проверяет, является ли данное дерево корректным BST."""
    if not nodes:
        return "CORRECT"
    def check(node_index, min_val, max_val):
        """Рекурсивная проверка корректности BST."""
        if node_index == -1:
            return True
        key, left, right = nodes[node_index]
        if not (min_val < key < max_val):
            return False
        return check(left, min_val, key) and check(right, key, max_val)

    return "CORRECT" if check(0, float("-inf"), float("inf")) else "INCORRECT"


def main(input_path, output_path):
    nodes = open_file(input_path, 6)
    result = is_valid_bst(nodes)
    print_in_terminal(nodes, result, "---Task_6 Lab_2---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
