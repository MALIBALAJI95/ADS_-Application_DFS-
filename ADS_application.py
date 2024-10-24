class DataNode:
    def __init__(self, val, valid=True):
        self.val = val
        self.valid = valid
        self.l = None
        self.r = None

def create_data_tree(arr, valid_data_flags, i, n):
    if i < n:
        temp = DataNode(arr[i], valid_data_flags[i])
        root = temp
        root.l = create_data_tree(arr, valid_data_flags, 2 * i + 1, n)
        root.r = create_data_tree(arr, valid_data_flags, 2 * i + 2, n)
        return root
    return None

def recover_data_dfs(node):
    if node:
        if node.valid:
            print(f"Recovered Data: {node.val}")
        else:
            print(f"Skipping Corrupted Node: {node.val}")
        recover_data_dfs(node.l)
        recover_data_dfs(node.r)

data = [99 ,80 ,77 ,50 ,40 ,33 ,15  ]
valid_data_flags = [True, False, True, True, False, True, True]
n = len(data)
root = create_data_tree(data, valid_data_flags, 0, n)
recover_data_dfs(root)
