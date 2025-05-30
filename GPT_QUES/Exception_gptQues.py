# Custom Exceptions
class FileError(Exception):
    """Base class for file-related exceptions."""
    pass

class FileNotFoundErrorCustom(FileError):
    pass

class EmptyFileError(FileError):
    pass

class UnsupportedFileTypeError(FileError):
    pass

class FilePermissionError(FileError):
    pass

# Function to read a file safely
def read_file(filename):
    try:
        # Check if the file exists
        try:
            with open(filename, "r") as file:
                content = file.read()
        except FileNotFoundError:
            raise FileNotFoundErrorCustom(f"Error: The file '{filename}' does not exist.")
        except PermissionError:
            raise FilePermissionError(f"Error: You do not have permission to read '{filename}'.")

        # Check for empty file
        if not content:
            raise EmptyFileError(f"Error: The file '{filename}' is empty.")

        # Check for supported file type (e.g., .txt only)
        if not filename.endswith(".txt"):
            raise UnsupportedFileTypeError(f"Error: Unsupported file type for '{filename}'. Only '.txt' files are allowed.")

        # If all good, return content
        print(f"Contents of '{filename}':\n{content}")

    # Handle custom exceptions
    except FileError as e:
        print(e)

# Main function to test the program
def main():
    print("=== Custom File Reader with Error Handling ===")
    filename = input("Enter the filename to read: ").strip()
    read_file(filename)

if __name__ == "__main__":
    main()
