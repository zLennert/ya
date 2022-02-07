input.onButtonPressed(Button.A, function () {
    basic.showString("" + randint(1, 1000))
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + randint(1, 6))
    basic.showString("" + randint(1, 6))
})
basic.forever(function () {
	
})
