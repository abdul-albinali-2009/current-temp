let current_temp = 0
basic.forever(function on_forever() {
    
    current_temp = input.temperature()
    basic.showNumber(current_temp)
    basic.pause(1000)
    basic.clearScreen()
})
