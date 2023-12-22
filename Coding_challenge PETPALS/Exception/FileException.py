class FileHandlingException(Exception):
    pass


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read data from the file
            data = file.read()
            print(f"Data read from file: {data}")
    except FileNotFoundError:
        raise FileHandlingException("File not found.")
    except Exception as e:
        raise FileHandlingException(f"Error reading file: {e}")

