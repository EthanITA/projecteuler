class BinaryTree:
    value: tuple = ()
    left, right = None, None

    def insert_values(self, *val):
        self.value = val
        return self

    @property
    def value_product(self):
        from my_libs.my_funcs import product
        return product(self.value)
