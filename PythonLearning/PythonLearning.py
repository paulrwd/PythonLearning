def main():
    x, y = 300, 300
    width, height = 200, 300
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height,  walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_width, width, roof_height)


def draw_house_foundation(x, y, width, height):
    print("Основание", x, y, width, height)
    pass


def draw_house_walls(x, y ,  width, height):
    print("Стены", x, y, width, height)
    pass


def draw_house_roof(x, y ,  width, height):
    print("Крыша", x, y, width, height)
    pass


if __name__ == "__main__":
    main()
