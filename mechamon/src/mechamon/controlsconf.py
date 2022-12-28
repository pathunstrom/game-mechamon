from ppb import buttons, keycodes

import mechamon.constants as constants
import mechamon.events as events
import mechamon.systems.controller as controller

inputs = [
    controller.Axis(constants.CONTROLS_VERTICAL, keycodes.S, keycodes.W),
    controller.Axis(constants.CONTROLS_HORIZONTAL, keycodes.A, keycodes.D),
    controller.Impulse(
        constants.CONTROLS_INTERACT, buttons.Primary, events.InteractRequested
    ),
    controller.Impulse(constants.CONTROLS_QUIT, keycodes.Escape, events.QuitRequested),
]
