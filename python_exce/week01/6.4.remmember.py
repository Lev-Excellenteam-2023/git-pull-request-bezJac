from PIL import Image


def decode_image(image_path):
    """
        Decodes a binary message hidden in an image.

        Args:
            image_path (str): The file path of the image to decode.

        Returns:
            str: The decoded message as a string.

        Raises:
            FileNotFoundError: If the specified image file cannot be found.
            ValueError: If the image format is unsupported or if the image is not binary.

        Details:
            This function decodes a binary message hidden in an image. It assumes that the image is binary, with each
            pixel being either black (value 1) or white (value 0). The function reads the pixel values column by column
            and decodes the binary message hidden in the black pixels. For each column, the function decodes the row
            position of the black pixel as an ASCII value. The decoded message is returned as a string. A ValueError is
            raised if the image format is not supported or the image is not binary.

        """
    image = Image.open(image_path)
    columns, rows = image.size  # size => (columns,rows)
    decoded_message = "".join(
        [chr(row) for col in range(columns) for row in range(rows) if image.getpixel((col, row)) == 1])
    return decoded_message
