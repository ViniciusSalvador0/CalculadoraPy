from factories import make_root, make_buttons, make_display, make_label
from classes import Calculator

def main():
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    calculator = Calculator(root, label, display, buttons)
    calculator.start()

if __name__ == '__main__':
    main()