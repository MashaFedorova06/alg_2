from alg_lab3.utils import open_file, write_file, print_in_terminal

INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"

def dfs(graph, start, end, visited):
    if start == end:
        return True
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited):
                return True
    return False



def main(input_path, output_path):
    data = open_file(input_path, 1)
    print(data)
    visited = {i: False for i in range(1, data[0] + 1)}
    result = 1 if dfs(data[1], data[2], data[3], visited) else 0
    print_in_terminal(data, result, "---Task_6 Lab_2---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
