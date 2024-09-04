import argparse
from PIL import Image
import os


def convert_image(input_file, output_format):
    # Open the input image
    with Image.open(input_file) as img:
        # Define the output file path
        base = os.path.splitext(input_file)[0]
        output_file = f"{base}.{output_format}"
        
        # Debugging: Print the output format
        print(f"Output format: {output_format}")
        
        # Check if the format is supported by PIL
        if output_format.upper() not in Image.SAVE:
            raise ValueError(f"Unsupported output format: {output_format}")
        
        # Save the image in the new format
        img.save(output_file, format=output_format)
        print(f"Image saved as {output_file}")

def main():

    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Convert .webp images to .png or .jpg"
    )
    parser.add_argument(
        "input_file",
        help="Path to the input .webp file"
    )
    parser.add_argument(
        "output_format",
        choices=["png", "jpeg"],
        help="Output format (png or jpg)"
    )
    
    args = parser.parse_args()
    
    # Convert the image
    convert_image(args.input_file, args.output_format)

if __name__ == "__main__":
    main()