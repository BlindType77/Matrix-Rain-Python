try:
    import bext, colorama
    from colorama import Style
    from pynput import keyboard
    import sys
    import random
    import time
except ImportError:
    print('Bext and colorama modules are required to run the program')
    sys.exit()
keyboard_commands = {
    'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110',
    'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100',
    'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010',
    's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000',
    'y': '01111001', 'z': '01111010', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100',
    'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010',
    'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000',
    'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110',
    'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', '0': '00110000', '1': '00110001',
    '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111',
    '8': '00111000', '9': '00111001', '`': '01100000', '-': '00101101', '=': '00111101', '[': '01011011',
    ']': '01011101', '\\': '01011100', ';': '00111011', '\'': '00100111', ',': '00101100', '.': '00101110',
    '/': '00101111', 'Key.space': '00100000', '\t': '00001001', '\n': '00001010', '\r': '00001101', '\x1b': '00101100',  # Escape key
    'Key.caps_lock': '01000000', 'Key.shift': '00100000', 'Key.ctrl_l': '00010000', 'Key.alt_l': '00001000', 'Key.tab': '00001001',
    'Key.backspace': '00001000', 'Key.enter': '00001010', 'Key.insert': '01001001', 'Key.delete': '01011100', 'Key.home': '01001000',
    'Key.end': '01000101', 'Key.page_up': '01000111', 'Key.page_down': '01110100', 'Key.up': '00010111', 'Key.down': '00011100',
    'Key.left': '00011000', 'Key.right': '00011101', 'Key.f1': '01000110', 'Key.f2': '01110011', 'Key.f3': '01100110', 'Key.f4': '01100101',
    'Key.f5': '01100100', 'Key.f6': '01100011', 'Key.f7': '01100010', 'Key.f8': '01100001', 'Key.f9': '00110000', 'Key.f10': '00110001',
    'Key.f11': '00110010', 'Key.f12': '00110011', 'Key.num_lock': '01101110', 'Key.scroll_lock': '01100011', 'Key.print_screen': '01000111',
    'Key.pause': '00100000'
}


Inputarray = []
class Drop:
    def __init__(self):
      
        self.x = random.randint(3, width)
        self.x2 = 16
        self.y = -1
        self.drop_type = random.randint(0, 2)
        self.timeout = random.randint(0, 3)
        self.wait_count = random.randint(0, 3)
        self.txt = ' '  # Initialize txt attribute

    def renew(self):
        self.__init__()
    def move(self):
        if self.wait_count < self.timeout:
            self.wait_count += 3
            return False
        else:
            self.wait_count = 0
            self.y += 1
            return True
def zero_draw():
  
    if drop.y < height:
        con_print(drop.x, drop.y - 1, lgreen, '')

def on_press(key):
    try:
        textval = key.char
        for char in textval:
            if char in keyboard_commands.keys():
                txt = str(keyboard_commands[char])
                drop.txt = txt
                txt = " "
                
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        bext.clear()
        sys.exit()
    try:
        textval = key.char
        for char in textval:
            if char in keyboard_commands.keys():
                txt = str(keyboard_commands[char])
                drop.txt = txt
                txt = " "
                
    except AttributeError:
        pass

def draw_drops():
    symbol = drop.txt
    if drop.drop_type == 1:
        con_print(drop.x, drop.y, green, " "+symbol)
        # zero_draw() 
    else:
        
        con_print(drop.x, drop.y, green, "" )
def draw_drops2():
    symbol = drop.txt
    if drop.drop_type == 1:
        con_print(drop.x2, drop.y, green, symbol)
        # zero_draw() 
    else:
        
        con_print(drop.x, drop.y, green, "" )        
def move_drops():
    for drop in drops:
        drop.move()

def is_rb_corner(x, y):
    return x == width and y == height

def con_print(x, y, color, symbol):
    if not is_rb_corner(x, y):
        bext.goto(x, y)
        sys.stdout.write(color)
        print(symbol, end="")

bext.title('Matrix')
bext.clear()
bext.hide_cursor()
width, height = bext.size()
width -= 1
height -= 2
blue = colorama.Fore.BLUE
green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX

drops = []
for i in range(1, width * 2 // 3):
    drop = Drop()
    drops.append(drop)

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
   while True:
       for drop in drops:
           if drop.move():
                
                draw_drops()
               

                if drop.y >= height:
                    
                    drop.renew ()
                    
                time.sleep(.00000000000000001)
       
        
           