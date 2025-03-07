def open_file(file_path, task):
    with open(file_path, 'r') as file:
        if task == 5:
            s = file.readline().strip()
            return s


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
