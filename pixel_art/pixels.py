from colorama import init, Back, Style

init(autoreset=True)

BLACK = Back.BLACK + '  '
RED = Back.RED + '  '
GREEN = Back.GREEN + '  '
YELLOW = Back.YELLOW + '  '
BLUE = Back.BLUE + '  '
MAGENTA = Back.MAGENTA + '  '
CYAN = Back.CYAN + '  '
WHITE = Back.WHITE + '  '

COLORS_DICT = {
    'black' : BLACK,
    'red': RED,
    'green': GREEN,
    'yellow': YELLOW,
    'blue': BLUE,
    'magenta': MAGENTA,
    'cyan': CYAN,
    'white': WHITE 
    }


class Image():
  def __init__(self, w=7, h=7):
    self.width = w
    self.height = h
    self.img = self.init_list()

def init_list(self):
    lst = []
    for row in range(self.height):
        lst.append([])
    return lst
