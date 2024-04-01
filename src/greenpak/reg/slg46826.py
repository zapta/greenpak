import os
from cffi import FFI

class SLG46826Reg:
    def __init__(self, header_path = None):
        """
        Initialize the SLG46826Reg instance.

        :param header_path: Path to the header file defining slg_register_t.
        """

        if header_path == None:
            header_path = 'c/slg46826_register_t.h'

        if not os.path.exists(header_path):
            raise FileNotFoundError(f"Header file not found: {header_path}")

        self.ffi = FFI()

        # Load the header file content
        with open(header_path, 'r') as header_file:
            header_content = header_file.read()

        # Define C declarations needed to use slg_register_t
        self.ffi.cdef(header_content)

        # Create an instance of slg_register_t
        self.reg = self.ffi.new("slg_register_t *")

    def update_reg_data(self, data):
        """
        Updates the reg_data of slg_register_t instance with provided data.

        :param data: A bytearray of size 256.
        """
        if not isinstance(data, bytearray) or len(data) != 256:
            raise ValueError("Data must be a bytearray of length 256")

        # Convert bytearray to bytes, as ffi.copy requires bytes object
        bytes_data = bytes(data)

        # Use ffi.memmove to update reg_data directly?
        self.ffi.memmove(self.reg.reg_data, bytes_data, len(bytes_data))


def main_test():
  slg = SLG46826Reg()

  random_data = bytearray(os.urandom(256))

  slg.update_reg_data(random_data)

  print( slg.reg.virtual_input_7)
  print( slg.reg.virtual_input_6)
  print( slg.reg.virtual_input_5)
  print( slg.reg.virtual_input_4)
  print( slg.reg.virtual_input_3)

if __name__ == "__main__":
   main_test()
