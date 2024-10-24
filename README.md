# ADS_-Application_DFS-

# Data Recovery from Corrupted Binary Tree Database

This project demonstrates how to recover valid data from a corrupted binary tree database using **Depth First Search (DFS)** traversal, specifically in **pre-order**. Each node in the binary tree represents a data point, some of which might be corrupted. The algorithm recovers only the valid data by traversing the binary tree.

## Project Overview

### Step 1: **Defining the DataNode Class**

The `DataNode` class is the fundamental building block of the binary tree. Each `DataNode` represents a unit of data in the database and has the following properties:

- `val`: Stores the actual data value.
- `valid`: A flag indicating whether the data is valid (`True`) or corrupted (`False`).
- `l` and `r`: Pointers to the left and right child nodes in the binary tree.

```python
class DataNode:
    def __init__(self, val, valid=True):
        """
        Initialize a DataNode.
        :param val: The value stored in the node.
        :param valid: A boolean flag indicating whether the data is valid (True) or corrupted (False).
        """
        self.val = val  # Data value
        self.valid = valid  # Flag for data validity (True means valid, False means corrupted)
        self.l = None  # Left child (pointer to another data node)
        self.r = None  # Right child (pointer to another data node)
```

### Step 2: **Creating the Binary Tree Structure**

The `create_data_tree` function constructs the binary tree using a list of data values and a corresponding list of validity flags. The tree is constructed using a **level-order insertion** method, with each node connected to its left and right children recursively.

```python
def create_data_tree(arr, valid_data_flags, i, n):
    """
    Recursively create a binary tree structure from a list of values and their corresponding validity flags.
    :param arr: List of data values.
    :param valid_data_flags: List of boolean flags indicating the validity of each data node.
    :param i: The current index in the list.
    :param n: Total number of elements in the list.
    :return: The root of the binary tree (DataNode).
    """
    if i < n:
        # Create a new node with the current element and its validity
        temp = DataNode(arr[i], valid_data_flags[i])
        root = temp
        
        # Recursively assign the left and right children (binary tree structure)
        root.l = create_data_tree(arr, valid_data_flags, 2 * i + 1, n)
        root.r = create_data_tree(arr, valid_data_flags, 2 * i + 2, n)
        
        return root  # Return the created node (root of this subtree)
    return None  # Return None if the index is out of bounds
```

### Step 3: **Recovering Valid Data using DFS (Pre-order Traversal)**

The `recover_data_dfs` function performs a **pre-order DFS traversal**. This means that the algorithm visits the current node first, processes it if valid, and then recursively visits the left and right children. If a node is found to be corrupted, it is skipped.

```python
def recover_data_dfs(node):
    """
    Perform a pre-order DFS to recover valid data from the tree.
    :param node: The current node in the tree (DataNode).
    """
    if node:
        # Pre-order step: Process the current node first (root)
        if node.valid:
            print(f"Recovered Data: {node.val}")  # Process the valid data (recover)
        else:
            print(f"Skipping Corrupted Node: {node.val}")  # Skip the corrupted node
        
        # Recursively traverse the left subtree (DFS)
        recover_data_dfs(node.l)
        
        # Recursively traverse the right subtree (DFS)
        recover_data_dfs(node.r)
```

### Step 4: **Running the Example**

In this example, we define a dataset representing some financial data points and a corresponding validity array indicating whether each node is valid or corrupted. We create the binary tree from this data and use DFS to recover only the valid nodes.

```python
# Example usage:
data = [99, 80, 77, 50, 40, 33, 15]  # Sample data points
valid_data_flags = [True, False, True, True, False, True, True]  # Validity of each node

# Create the binary tree (database)
root = create_data_tree(data, valid_data_flags, 0, len(data))

# Recover valid data using DFS (Pre-order Traversal)
print("Recovering Data from the Database (Pre-order DFS):")
recover_data_dfs(root)
```

### Example Output:

```
Recovering Data from the Database (Pre-order DFS):
Recovered Data: 99
Skipping Corrupted Node: 80
Recovered Data: 77
Recovered Data: 50
Skipping Corrupted Node: 40
Recovered Data: 33
Recovered Data: 15
```

## How It Works

1. **DataNode Class**: Defines each node in the tree with a value and validity flag.
2. **Tree Creation**: Builds a binary tree from a given list of values and their validity flags.
3. **Pre-order DFS**: Recovers valid data nodes by checking validity as it traverses the tree in pre-order.
