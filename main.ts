input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("" + ("" + randint(1, 1000)))
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showString("" + ("" + randint(1, 6)))
    basic.showString("" + ("" + randint(1, 6)))
})
basic.forever(function on_forever() {
    
})
