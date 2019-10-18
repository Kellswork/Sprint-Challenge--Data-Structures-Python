class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # return value if self.value == value
        # if value == self.value:
        #     return
        if value < self.value:
            # checks if the left has a child
            if self.left is None:
                # if it have a value doesn't we assign it value and return
                self.left = BinarySearchTree(value)

            else:
                # if it does, we change the root to the current value
                self.left.insert(value)

        elif value >= self.value:
            # checks if the left has a child
            if self.right is None:
                # if it doesn't we assign it value and return
                self.right = BinarySearchTree(value)

            else:
                # if it does, we change the root to the current value
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if value is == to self.value, return value
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
