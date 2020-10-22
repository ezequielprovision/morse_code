
morse_dict = {
    'A': '. _',         'B': '_ . . .',     'C': '_ . _ .',
    'CH':	'_ _ _ _',    'D': '_ . .',       'E': '.',
    'F': '. . _ .',     'G': '_ _ .',       'H': '. . . .',
    'I': '. .',         'J': '. _ _ _',     'K': '_ . _',
    'L': '. _ . .',     'M': '_ _',         'N': '_ .',
    'Ñ': '_ _ . _ _',   'O': '_ _ _',       'P': '. _ _ .',
    'Q': '_ _ . _',     'R': '. _ .',       'S': '. . .',
    'T': '_',           'U': '. . _',       'V': '. . . _', 
    'W': '. _ _',       'X': '_ . . _',     'Y': '_ . _ _',
    'Z': '_ _ . .',     '0': '_ _ _ _ _',   '1': '. _ _ _ _',
    '2': '. . _ _ _',   '3': '. . . _ _',   '4': '. . . . _',
    '5': '. . . . .',   '6': '_ . . . .',   '7': '_ _ . . .',
    '8': '_ _ _ . .',   '9': '_ _ _ _ .',   '.': '. _ . _ . _',
    ',': '_ . _ . _ _', '?': '. . _ _ . .', '"': '. _ . . _ .',
    '!': '_ _ . . _ _'   
}


class MorseException(Exception):
    pass


def convert_to_morse(message):
    result = ''
    message = message.upper()
    for ix, letter in enumerate(message):
        if letter in morse_dict:
            result += morse_dict[letter] + '\n'
        elif not letter == ' ':
            raise MorseException(ix + 1, letter)
    return result


def export_result(message, morse_msg):
    user_file = (input('Ingrese un nombre con el que se creara el archivo\n').replace(' ', '_')).lower()
    with open('results\\{}'.format(user_file), 'a') as f:
        f.write("""
Mensaje:

{}

Convertido a Codigo Morse:

{}

############   #############    """.format(message, morse_msg))

def main():
    while True:
        message = input('Ingrese un mensaje para convertir en Morse, o "0" para salir\n')
        if message == '0':
            break
        try:
            morse_msg = convert_to_morse(message)
        except MorseException as e:
            print('ERROR:\nNo se puede convertir el caracter Nº {}: "{}"'.format(e.args[0], e.args[1]))
        else:
            print(morse_msg)
            save_text = input('Para guardar el resultado ingrese "y", sino ingrese una tecla cualquiera\n')
            if save_text == 'y':
                export_result(message, morse_msg)


if __name__ == '__main__':
    main()