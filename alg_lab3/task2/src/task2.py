from alg_lab3.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def find_components(n, graph):
    """Подсчитываем количество компонент связности в графе"""
    visited = set()
    components = 0

    def dfs(node):
        """Обход в глубину для пометки всех узлов в одной компоненте"""
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])

    for node in range(1, n + 1):
        if node not in visited:
            dfs(node)
            components += 1

    return components



def main(input_path, output_path):
    n, graph = open_file(input_path, 2)
    result = find_components(n, graph)
    print_in_terminal([n,graph], result, "---Task_2 Lab_3---")
    write_file(result, output_path)



if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
