from alg_lab3.utils import open_file, write_file, print_in_terminal


INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


def solve(n, corridors, path):
    adj = {i: {} for i in range(1, n + 1)}

    for corridor in corridors:
        u, v, c = corridor
        adj[u][c] = v
        adj[v][c] = u

    current_room = 1

    for color in path:
        if color not in adj[current_room]:
            return "INCORRECT"

        current_room = adj[current_room][color]

    return str(current_room)


def main(input_path, output_path):
    n, m, corridors, k, path = open_file(input_path, 12)
    result = solve(n, corridors, path)
    print_in_terminal([n, m, corridors, k, path], result, "---Task_12 Lab_3---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)
