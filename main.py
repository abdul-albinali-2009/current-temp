current_temp = 0

def on_forever():
    global current_temp
    current_temp = input.temperature()
    basic.show_number(current_temp)
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)
