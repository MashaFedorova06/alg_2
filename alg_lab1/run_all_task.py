from alg_lab1.task7.src.task7 import main as task7
from alg_lab1.task11.src.task11 import main as task11
from alg_lab1.task11.src.task11 import main as task2



def main(path):
    tasks = [(task7, [path + "/task7/txtf/input.txt", path + "/task7/txtf/output.txt"]),
             (task11, [path + "/task11/txtf/input.txt", path + "/task11/txtf/output.txt"]),
             (task2, [path + "/task2/txtf/input.txt", path + "/task2/txtf/output.txt"]),
             (task8, [path + "/task2/txtf/input.txt", path + "/task2/txtf/output.txt"])
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
