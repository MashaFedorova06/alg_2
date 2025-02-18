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
