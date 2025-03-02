from alg_lab3.task1.src.task1 import main as task1
from alg_lab3.task2.src.task2 import main as task2

def main(path):
    tasks = [(task1, [path + "/task1/txtf/input.txt", path + "/task1/txtf/output.txt"]),
             (task2, [path + "/task2/txtf/input.txt", path + "/task2/txtf/output.txt"])
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
