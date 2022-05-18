from ppb import buttons, keycodes

import mechamon
from mechamon import events
from mechamon.systems import controller

inputs = [
    controller.Axis(mechamon.CONTROLS_VERTICAL, keycodes.S, keycodes.W),
    controller.Axis(mechamon.CONTROLS_HORIZONTAL, keycodes.A, keycodes.D),
    controller.Impulse(mechamon.CONTROLS_INTERACT, buttons.Primary, events.InteractRequested),
    controller.Impulse(mechamon.CONTROLS_QUIT, keycodes.Escape, events.QuitRequested)
]
