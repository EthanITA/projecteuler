class BinaryTree:
    value = ()
    left, right = None, None

    def insert_values(self, *val):
        self.value = val
        return self
