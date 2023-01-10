def read_file(filename="", text=""):
    """Writes a string to a file usning utf encoding.

    Args:
        filename: The name of the file to be written.
        text: The text to be written to the file.

    Returns:
        The number of characters added
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
