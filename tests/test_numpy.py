from np import operations


numpy_operations=operations.NumpyOperations()

class TestOperations:

    def test_create_random(self):
        len=10
        vec=numpy_operations.create_random(len)
        assert vec.size == len

