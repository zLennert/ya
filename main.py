def on_button_pressed_a():
    basic.show_string("" + str((randint(1, 1000))))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("" + str((randint(1, 6))))
    basic.show_string("" + str((randint(1, 6))))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
