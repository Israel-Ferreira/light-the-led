from pyfirmata import Arduino, PWM


def get_arduino_instance(arduino_board_usb: str, led_pins: list[int]):
    board =  Arduino(arduino_board_usb)
    arduino_led_pins_pwm(board, led_pins)
    
    return board


def arduino_led_pins_pwm(board: Arduino, led_pins: list[int]):
    for led_pin in led_pins:
        board.digital[led_pin].mode = PWM
        

def blink_leds_in_purple_color(arduino_board, red_pin, green_pin, blue_pin):
    arduino_board.digital[red_pin].write(1)
    arduino_board.digital[green_pin].write(0)
    arduino_board.digital[blue_pin].write(1)

    