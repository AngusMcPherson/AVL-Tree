class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if node is not None:
        return node.height
    else:
        return 0

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def getBalance(node):
    if node is not None:
        return getHeight(node.left) - getHeight(node.right)
    else:
        return 0

def leftRotate(y):
    x = y.right
    t2 = x.left
    x.left = y
    y.right = t2
    updateHeight(y)
    updateHeight(x)
    return x

def rightRotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    updateHeight(y)
    updateHeight(x)
    return x

def insert(node, value):
    if not node:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    else:
        return node
    updateHeight(node)
    balance = getBalance(node)
    if balance > 1 and value < node.left.value:
        return rightRotate(node)
    if balance < -1 and value > node.right.value:
        return leftRotate(node)
    if balance > 1 and value > node.left.value:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    if balance < -1 and value < node.right.value:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    return node


def leftMax(node):
    current = node
    while current.right:
        current = current.right
    return current


def delete(node, value):
    if not node:
        return node
    if value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:
        if not node.left or not node.right:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        else:
            temp = leftMax(node.left)
            node.value = temp.value
            node.left = delete(node.left, temp.value)
    if not node:
        return node
    updateHeight(node)
    balance = getBalance(node)
    if balance > 1:
        if getBalance(node.left) >= 0:
            return rightRotate(node)
        else:
            node.left = leftRotate(node.left)
            return rightRotate(node)
    if balance < -1:
        if getBalance(node.right) <= 0:
            return leftRotate(node)
        else:
            node.right = rightRotate(node.right)
            return leftRotate(node)
    return node

def preorder(node, result):
    if node:
        result.append(str(node.value))
        preorder(node.left, result)
        preorder(node.right, result)

def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(str(node.value))
        inorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(str(node.value))


moves = input().split()
root = None
for move in moves:
    if move[0] == "A":
        root = insert(root, int(move[1:]))
    elif move[0] == "D":
        root = delete(root, int(move[1:]))
    elif move in ("PRE", "IN", "POST"):
        if not root:
            print("EMPTY")
        else:
            result = []
            if move == "PRE":
                preorder(root, result)
            elif move == "IN":
                inorder(root, result)
            elif move == "POST":
                postorder(root, result)
            print(" ".join(result))
        break
