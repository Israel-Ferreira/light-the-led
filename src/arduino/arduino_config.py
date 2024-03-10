from pyfirmata import Arduino, PWM


def get_arduino_instance(arduino_board_usb: str, led_pins: list[int]):
    board =  Arduino(arduino_board_usb)
    arduino_led_pins_pwm(board, led_pins)
    
    return board


def arduino_led_pins_pwm(board: Arduino, led_pins: list[int]):
    for led_pin in led_pins:
        board.digital[led_pin].mode = PWM
        