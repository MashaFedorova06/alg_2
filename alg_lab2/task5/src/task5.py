from alg_lab2.utils import open_file, write_file, print_in_terminal


INPUT_TXT = "../txtf/input.txt"
OUTPUT_TXT = "../txtf/output.txt"


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive_dop(self.root, key)

    def insert_recursive_dop(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive_dop(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive_dop(node.right, key)

    def delete(self, key):
        self.root = self.delete_recursive_dop(self.root, key)

    def delete_recursive_dop(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_recursive_dop(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive_dop(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.find_min_dop(node.right)
                node.key = min_node.key
                node.right = self.delete_recursive_dop(node.right, min_node.key)

        return node

    @staticmethod
    def find_min_dop(node):
        while node.left is not None:
            node = node.left
        return node

    def exists(self, key):
        return self.exists_recursive_dop(self.root, key)

    def exists_recursive_dop(self, node, key):
        if node is None:
            return 'false'
        if key < node.key:
            return self.exists_recursive_dop(node.left, key)
        elif key > node.key:
            return self.exists_recursive_dop(node.right, key)
        return 'true'

    def next(self, key):
        return self.next_dop(self.root, key)

    def next_dop(self, node, key):
        if node is None:
            return "none"

        if key >= node.key:
            return self.next_dop(node.right, key)
        else:
            result = self.next_dop(node.left, key)
            if result != "none":
                return result
            else:
                return node.key


    def prev(self, key):
        return self.prev_dop(self.root, key)

    def prev_dop(self, node, key):
        if node is None:
            return "none"

        if key <= node.key:
            return self.prev_dop(node.left, key)
        else:
            res = self.prev_dop(node.right, key)
            if res != "none":
                return res
            else:
                return node.key


def main(input_path, output_path):
    tree = BinarySearchTree()
    commands = open_file(input_path, 5)
    print_list = []

    for line in commands:
        command, *args = line.strip().split()
        if command == "insert":
            tree.insert(int(args[0]))
        elif command == "delete":
            tree.delete(int(args[0]))
        elif command == "exists":
            print_list.append(tree.exists(int(args[0])))
        elif command == "next":
            print_list.append(tree.next(int(args[0])))
        elif command == "prev":
            print_list.append(tree.prev(int(args[0])))

    result = "\n".join(map(str, print_list))

    print_in_terminal(commands, result, "---Task_5 Lab_2---")
    write_file(result, output_path)


if __name__ == "__main__":
    main(INPUT_TXT, OUTPUT_TXT)