import device

def convertToMeterValue(value: float):
    """ Converts an FL Studio meter float value to an MCU compatible value (one char hex) """

    value_max = 1.3 # FL Studio max value
    meter_value = int(value / value_max * 127) # 127 — max value in X touch one

    # If there's any activity, make sure the meter shows it
    if (value > 0.001 and meter_value == 0):
        meter_value = 1

    # If there's no activity, clear the meter (15)
    if value == 0:
        meter_value = 0

    return meter_value;

def setButton(button: int, button_state: int):
    """ Take a button and turn it on or off """
    device.midiOutMsg(0xB0, 0, button, button_state)

""" Color: black, red, green, yellow, blue, magenta, cyan, white """
def sendText(evt, color: str, first_line: str, second_line: str, invert_upper = False, invert_lover = False):
    firstFourBytes = '0000'
    if color == 'red':
        firstFourBytes = '0001'
    elif color == 'green':
        firstFourBytes = '0010'
    elif color == 'yellow':
        firstFourBytes = '0011'
    elif color == 'blue':
        firstFourBytes = '0100'
    elif color == 'magenta':
        firstFourBytes = '0101'
    elif color == 'cyan':
        firstFourBytes = '0110'
    elif color == 'white':
        firstFourBytes = '0111'

    invert_up_byte = '1' if invert_upper else '0'
    invert_down_byte = '1' if invert_lover else '0'

    binary_str = '00' + invert_down_byte + invert_up_byte + firstFourBytes

    print(binary_str)

    first_line_hex = first_line.encode('ascii')[:7].ljust(7).hex().zfill(14)
    second_line_hex = second_line.encode('ascii')[:7].ljust(7).hex().zfill(14)

    print(int(binary_str, 2));
    print('{:x}'.format(int(binary_str, 2)));

    #                40 — X-Touch
    final = 'f0002032414c00' + '{:x}'.format(int(binary_str, 2)).zfill(2) + first_line_hex + second_line_hex + 'f7'

    print(final);

    try:
        result = device.midiOutSysex(bytearray.fromhex(final));
        print(result)
    except Exception as e:
        print(repr(e))

