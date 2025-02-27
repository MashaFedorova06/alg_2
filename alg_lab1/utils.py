def open_file(file_path, task):
    with open(file_path, 'r') as file:
        if task == 7:
            k, n = map(int, file.readline().split())
            arr = [int(i) for i in file.readline().split()]
            return k, n, arr
        if task == 2:
            d = int(file.readline())
            m = int(file.readline())
            n = int(file.readline())
            stops = [int(i) for i in file.readline().split()]
            return d, m, n, stops
        if task == 8:
            n = int(file.readline())
            requests = []
            for i in range(n):
                start, end = map(int, file.readline().split())
                requests.append((start, end))
            return requests
        if task == 4:
            n = int(file.readline().strip())
            segments = []
            for _ in range(n):
                a, b = map(int, file.readline().strip().split())
                segments.append((a, b))
            return n, segments
        if task == 12:
            n = int(file.readline().strip())
            nums = list(map(int, file.readline().strip().split()))
            return n, nums
        if task == 11:
            W, n = list(map(int, file.readline().strip().split()))
            nums = list(map(int, file.readline().strip().split()))
            return W, n, nums
        if task == 100:
            n = int(file.readline())
            nodes = {i: [None, 0, 0] for i in range(1, n + 1)}  # Индексы с 1 по n

            for i, line in enumerate(file.readlines(), start=1):
                val, left, right = map(int, line.split())
                nodes[i][0] = val  # Записываем значение вершины
                if left != 0:
                    nodes[i][1] = left  # Устанавливаем левый ребенок
                if right != 0:
                    nodes[i][2] = right  # Устанавливаем правый ребенок

        return nodes



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
