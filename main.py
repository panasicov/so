class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            data = file.read()
        print(f"Data read from {self.file_path}:")
        print(data)
        return data


class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)
        print(f"Data written to {self.file_path}.")


class FileManipulator:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def write_file(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)
        print(f"Data written to {self.file_path}.")


# Exemplu de utilizare
input_file = "input.txt"   # Fișierul de intrare
output_file = "output.txt" # Fișierul de ieșire

# Instanțierea claselor
file_reader = FileReader(input_file)
file_writer = FileWriter(output_file)
file_manipulator = FileManipulator(file_reader, file_writer)

# Executarea manipulării
file_manipulator.manipulate_files()

