import ppb

import mechamon

BUTTON_LAYER = 1
TEXT_LAYER = 2

BUTTON_HEIGHT = 2
BUTTON_WIDTH = 7
BUTTON_SPACING = 0.5


def start_game():
    from mechamon.scenes import corral
    return ppb.events.StartScene(corral.Scene)


def launch_settings():
    from mechamon.scenes import settings
    return ppb.events.StartScene(settings.Scene)


class Button(ppb.RectangleSprite):
    image = ppb.Rectangle(*mechamon.BRAND_CONTRAST_COLOR, aspect_ratio=(BUTTON_WIDTH, BUTTON_HEIGHT))
    height = BUTTON_HEIGHT
    width = BUTTON_WIDTH
    layer = BUTTON_LAYER
    event = lambda self: ppb.events.Quit()

    def on_button_released(self, event: ppb.events.ButtonReleased, signal):
        x_in_range = self.left <= event.position.x <= self.right
        y_in_range = self.bottom <= event.position.y <= self.top
        if x_in_range and y_in_range:
            signal(self.event())


buttons = [
    ("Start Game", start_game),
    ("Settings", launch_settings),
    ("Quit", lambda:ppb.events.Quit())
]


class Scene(ppb.Scene):
    background_color = (71, 197, 255)

    def __init__(self, **props):
        super().__init__(**props)
        self.font = ppb.Font(mechamon.TITLE_FONT, size=96)
        self.add(ppb.Sprite(
            image=ppb.Text("Mekanik Corral", font=self.font, color=mechamon.BRAND_FONT_COLOR),
            size=mechamon.TITLE_SIZE,
            position=ppb.Vector(-3.75, 6)
        ))
        button_top = 3
        for button_text, event_function in buttons:
            button = Button(event=event_function)
            button.left = 0
            button.top = button_top
            button_top = button.bottom - BUTTON_SPACING
            text = ppb.Sprite(image=ppb.Text(button_text, font=self.font, color=mechamon.BRAND_FONT_COLOR), layer=TEXT_LAYER, size=BUTTON_HEIGHT * 0.8)
            text.position = button.position
            self.add(button)
            self.add(text)
