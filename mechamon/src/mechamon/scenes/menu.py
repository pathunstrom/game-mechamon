import ppb

import mechamon.constants as constants
import mechamon.scenes as mechamon_scenes

BUTTON_LAYER = 1
TEXT_LAYER = 2

BUTTON_HEIGHT = 2
BUTTON_WIDTH = 7
BUTTON_SPACING = 0.5


def start_game():
    return ppb.events.StartScene(mechamon_scenes.corral.Scene)


def launch_settings():
    return ppb.events.StartScene(mechamon_scenes.settings.Scene)


class Button(ppb.RectangleSprite):
    image = ppb.Rectangle(
        *constants.BRAND_CONTRAST_COLOR, aspect_ratio=(BUTTON_WIDTH, BUTTON_HEIGHT)
    )
    height = BUTTON_HEIGHT
    width = BUTTON_WIDTH
    layer = BUTTON_LAYER
    event = lambda self: ppb.events.Quit()

    def on_interact_requested(self, event, signal):
        x_in_range = self.left <= event.position.x <= self.right
        y_in_range = self.bottom <= event.position.y <= self.top
        if x_in_range and y_in_range:
            signal(self.event())


buttons = [
    ("Start Game", start_game),
    ("Settings", launch_settings),
    ("Quit", lambda: ppb.events.Quit()),
]


class Scene(ppb.Scene):
    background_color = (71, 197, 255)

    def __init__(self, **props):
        super().__init__(**props)
        self.add(
            ppb.Sprite(
                image=ppb.Text(
                    "Mekanik Corral",
                    font=constants.TITLE_FONT,
                    color=constants.BRAND_FONT_COLOR,
                ),
                size=constants.TITLE_SIZE,
                position=ppb.Vector(-3.75, 6),
            )
        )
        button_top = 3
        for button_text, event_function in buttons:
            button = Button(event=event_function)
            button.left = 0
            button.top = button_top
            button_top = button.bottom - BUTTON_SPACING
            text = ppb.Sprite(
                image=ppb.Text(
                    button_text,
                    font=constants.TITLE_FONT,
                    color=constants.BRAND_FONT_COLOR,
                ),
                layer=TEXT_LAYER,
                size=BUTTON_HEIGHT * 0.8,
            )
            text.position = button.position
            self.add(button)
            self.add(text)
