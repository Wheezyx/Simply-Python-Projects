import pygal

from pygal.style import DarkGreenBlueStyle as DGBS, BlueStyle as BS


def get_pygal_config():
    my_config = pygal.Config()
    my_config.x_label_rotation = 40
    my_config.show_legend = False
    my_config.title_font_size = 23
    my_config.label_font_size = 13
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    return my_config


def get_chart_style(style):
    return DGBS if style == 'W' else BS
