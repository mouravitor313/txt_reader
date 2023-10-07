class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def open_file_read(arch_name):
        with open(arch_name) as archive:
            return archive.read()

    @staticmethod
    def open_file_readlines(arch_name):
        with open(arch_name) as archive:
            return archive.readlines()