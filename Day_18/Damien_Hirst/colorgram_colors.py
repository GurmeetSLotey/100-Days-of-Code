import colorgram

colors = colorgram.extract('Day_18/Damien_Hirst/Color_Palette/kirby_epic_yarn.jpg',30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)