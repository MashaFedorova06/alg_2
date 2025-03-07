from alg_lab4.task5.src.task5 import main as task5


def main(path):
    tasks = [(task5, [path + "/task5/txtf/input.txt", path + "/task5/txtf/output.txt"])
             ]
    for task, paths in tasks:
        task(paths[0], paths[1])


if __name__ == '__main__':
    main('.')
