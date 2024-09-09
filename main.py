from pathlib import Path

from PIL import Image, ImageDraw
from fire import Fire


def make_grid(cell_size: int = 64, line_color: str = "black", line_width: int = 2):
    # Calculate total image size
    image_size = cell_size * 3

    # Create a new image with a white background
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)

    # Draw vertical lines
    for x in range(1, 3):
        pos = x * cell_size
        draw.line([(pos, 0), (pos, image_size)], fill=line_color, width=line_width)

    # Draw horizontal lines
    for y in range(1, 3):
        pos = y * cell_size
        draw.line([(0, pos), (image_size, pos)], fill=line_color, width=line_width)

    return image


def add_circle_in_grid(image, position: str, color: str):
    cell_size = image.width // 3
    draw = ImageDraw.Draw(image)

    if position == "top_left":
        x, y = 0, 0
    elif position == "top_right":
        x, y = 2, 0
    elif position == "bottom_left":
        x, y = 0, 2
    elif position == "bottom_right":
        x, y = 2, 2
    elif position == "left":
        x, y = 0, 1
    elif position == "right":
        x, y = 2, 1
    else:
        raise ValueError("Invalid position")

    x_pos = x * cell_size + cell_size // 2
    y_pos = y * cell_size + cell_size // 2
    radius = cell_size // 4
    draw.ellipse(
        [(x_pos - radius, y_pos - radius), (x_pos + radius, y_pos + radius)],
        fill=color,
    )
    return image


def generate_data(output_dir: str = "data"):
    for color in ["red", "green"]:
        for position in [
            "top_left",
            "top_right",
            "bottom_left",
            "bottom_right",
            "right",
            "left",
        ]:
            image = make_grid()
            image = add_circle_in_grid(image, position, color)
            path = Path(output_dir) / f"{color}_{position}.jpg"
            path.parent.mkdir(parents=True, exist_ok=True)
            image.save(path)


"""
conda create -n badminton-footwork python=3.11 -y
conda activate badminton-footwork
pip install -r requirements.txt
python main.py generate_data 
"""


if __name__ == "__main__":
    Fire()
