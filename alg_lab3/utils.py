def open_file(file_path, task):
    with open(file_path, 'r') as file:
        if task == 1:
            n, m = map(int, file.readline().split())
            graph = {i: [] for i in range(1, n + 1)}
            for _ in range(m):
                u, v = map(int, file.readline().split())
                graph[u].append(v)
                graph[v].append(u)
            u, v = map(int, file.readline().split())
            return n, graph, u, v

        if task == 2:
            n, m = map(int, file.readline().split())
            graph = {i: [] for i in range(1, n + 1)}
            for _ in range(m):
                u, v = map(int, file.readline().split())
                graph[u].append(v)
                graph[v].append(u)
            return n, graph

        if task == 12:
            n, m = map(int, file.readline().split())
            corridors = []
            for _ in range(m):
                corridors.append(map(int, file.readline().split()))
            k = int(file.readline())
            path = map(int, file.readline().split())
            return n, m, corridors, k , path


def write_file(ans, file_path, task=0):
    with open(file_path, 'w') as file:
        if isinstance(ans, list):
            file.write(" ".join(ans))
        else:  # для числового ответа
            file.write(str(ans))


def print_in_terminal(input_data, output_data, task_name):
    print(task_name)
    print("Входные данные:")
    print(input_data)
    print("Результат:")
    print(output_data, '\n')
