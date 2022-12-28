import ppb

import mechamon.constants as constants


class Scene(ppb.Scene):

    background_color = constants.BRAND_CONTRAST_COLOR

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(
            ppb.Sprite(
                image=ppb.Text(
                    "Settings", font=constants.font, color=constants.BRAND_FONT_COLOR
                ),
                size=constants.TITLE_SIZE,
                position=ppb.Vector(0, 6),
            )
        )

        self.add(
            ppb.Sprite(
                image=ppb.Text(
                    "There are no settings, hit escape to return.",
                    font=constants.font,
                    color=constants.BRAND_FONT_COLOR,
                )
            )
        )

    def on_quit_requested(self, event, signal):
        signal(ppb.events.StopScene())
