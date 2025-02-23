def open_file(file_path, task):
    with open(file_path, 'r') as file:
        if task == 6:
            n = int(file.readline().strip())
            nodes = []
            for _ in range(n):
                k, l, r = map(int, file.readline().strip().split())
                nodes.append((k, l, r))
            return nodes

        if task == 8:
            n = int(file.readline())
            # Создаем словарь для хранения данных о вершинах. Ключ - индекс вершины, значение - список из трех элементов
            nodes = {i: [None, 0, 0] for i in range(1, n + 1)}

            for i, line in enumerate(file.readlines(), start=1):
                val, left, right = map(int, line.split())
                nodes[i][0] = val  # Записываем значение вершины в словарь
                if left != 0:
                    nodes[i][1] = left  # Устанавливаем индекс левого ребенка
                if right != 0:
                    nodes[i][2] = right  # Устанавливаем индекс правого ребенка

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
