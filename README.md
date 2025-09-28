AVL Tree in Python
Overview

This project is a Python implementation of an AVL Tree, a self-balancing binary search tree that maintains height balance during insertions and deletions using left and right rotations. The AVL Tree ensures that operations such as search, insert, and delete remain efficient with logarithmic time complexity.

The implementation includes preorder, inorder, and postorder traversals and can dynamically process commands to build and modify the tree. It is designed for educational purposes and to demonstrate how a balanced binary search tree works from first principles.

Features

Insertion and deletion of integer values while maintaining AVL balance.

Automatic tree rebalancing using left, right, and double rotations.

Height tracking and balance factor calculation for each node.

Traversal methods:

Preorder (Root → Left → Right)

Inorder (Left → Root → Right)

Postorder (Left → Right → Root)

Interactive command-line interface for inserting, deleting, and printing traversals.

Input Format

The program accepts a single line of space-separated commands:

A<value> → Add a node with the given value

D<value> → Delete a node with the given value

PRE → Output preorder traversal

IN → Output inorder traversal

POST → Output postorder traversal
