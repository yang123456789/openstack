import random
from openstack.config import *
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.http import *
from django.shortcuts import *
import json
from django.contrib import messages

_upper_cases = LETTER_CASES.upper()
_numbers = ''.join(map(str, range(1, 10)))
init_chars = ''.join((LETTER_CASES, _upper_cases, _numbers))


def create_identify_code(
        size=(120, 30), chars=init_chars, img_type="GIF",
        mode="RGB", bg_color=(200, 255, 155), fg_color=(0, 0, 255),
        font_type="/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf",
        length=4, draw_lines=True, n_line=(1, 2),
        draw_points=True, font_size=18, point_chance=2):
    '''
    todo: Generate picture validate code
    :param size: Picture size
    :param chars: Allowed character set
    :param img_type: Picture saved format, the default is GIF, optional for GIF, JPEG, TIFF, PNG
    :param mode: Picture mode, the default is RGB
    :param bg_color: Background color, the default is white
    :param fg_color: Foreground color, verify code character color, default to blue
    :param font_size: Verification code font size
    :param font_type: Verification code font
    :param length: Number of verification code characters
    :param draw_lines: Whether the line is drawn
    :param n_line: The number of lines of interference, the number of formats, the default is (1, 2), only True for draw_lines
    :param draw_points: Whether to draw the disturbance point
    :param point_chance: The probability of the emergence of the scrambling, the size of the range of [0, 100]
    :return[0]: PIL Image instance
    :return[1]: Code to verify the string in the picture
    '''

    width, height = size
    # Create graphics
    img = Image.new(mode, size, bg_color)
    # Create brush
    draw = ImageDraw.Draw(img)

    def get_chars():
        '''Generates a string of a given length, returns a list format'''
        return random.sample(chars, length)

    def create_lines():
        '''Draw interference line'''
        line_num = random.randint(*n_line) # disturb line number
        for i in range(line_num):
            # starting point
            begin = (random.randint(0, size[0]),
                     random.randint(0, size[1]))
            # ending point
            end = (random.randint(0, size[0]),
                   random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        '''Draw the interference point'''
        chance = min(100, max(0, int(point_chance)))
        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        ''''Draw verification code character'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars)
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                    strs, font=font, fill=fg_color)
        return ''.join(c_chars)

    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()
    params = [
        1 - float(random.randint(1, 2)) / 100,
        0, 0, 0,
        1 - float(random.randint(1, 10)) / 100,
        float(random.randint(1, 2)) / 500,
        0.001,
        float(random.randint(1, 2)) / 500
    ]
    # create distortions
    img = img.transform(size, Image.PERSPECTIVE, params)
    # filter, boundary strengthening (greater threshold)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, strs


def utf8(param):
    if param is None or isinstance(param, str):
        return param
    return param.encode('utf-8')


def render_json(data):
    return HttpResponse(json.dumps(data), content_type="text/json")

# Create your views here.
