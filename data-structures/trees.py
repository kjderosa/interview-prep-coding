__author__ = 'Kyle DeRosa'


# so I guess I could do this a couple of ways - classes, dictionaries, lists

# Tree
# Binary Tree
# Binary Search Tree
# Red-Black Tree
#

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root:
            return repr(self.root) + '\n' + self._repr(self.root, '-->')
        else:
            return repr(self.root)

    def _repr(self, node, plus):
        out = ""
        if node.left:
            out += plus + repr(node.left) + '\n' + self._repr(node.left, plus + '-->')
        if node.right:
            out += plus + repr(node.right) + '\n' + self._repr(node.right, plus + '-->')
        return out

    def getroot(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                node.left.parent = node
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
                node.right.parent = node
            else:
                self._insert(data, node.right)

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return None

    def _search(self, data, node):
        if data is node.data:
            return node
        elif data < node.data and node.left is not None:
            self._search(data, node.left)
        elif data > node.data and node.right is not None:
            self._search(data, node.right)

    def delete(self, data):
        # removes first instance of data
        if self.root is data:
            self._delete_fix_tree(self.root)
        elif data < data and self.root.left is not None:
            self._delete(data, self.root.left)
        else:
            self._delete(data, self.root.right)

    def _delete(self, data, node):
        if data is node.data:
            self._delete_fix_tree(node)
        elif data < node.data:
            self._delete(data, node.left)
        else:
            self._delete(data, node.right)

    def _delete_fix_tree(self, node):
        if node.left is None and node.right is None:
            node.data = None
        elif node.left is None and node.right is not None:
            node.parent.right = node.right
            node.right.parent = node.parent
        else:
            min_right = self._min_right(node.right)
            # remove parent's child relationship
            min_right.parent.left = None
            # insert into place
            min_right.parent = node.parent
            min_right.left = node.left
            min_right.right = node.right
            # adjust child's parent nodes
            node.left.parent = min_right
            node.right.parent = min_right
            # adjust parent's child node
            if node.parent.left is node:
                node.parent.left = min_right
            else:
                node.parent.right = min_right

    def _min_right(self, node):
        if node.left is None:
            return node
        else:
            return self._min_right(node.left)

# Big O test
# insert (log n); insert into tree, longest possible path;
# insert (n); can take n if tree is completely unbalanced
# delete (log n); delete from tree, longest possible path;
# delete (n); can take n if tree is completely unbalanced
# search (log n); search tree, longest possible path;
# search (n); can take n if tree is completely unbalanced
# sorted search - tree is implictly sorted
# sort  - tree is implictly sorted

# space
# n elements, with n-1 ptrs; 2(n-1) if parent and child pointers
