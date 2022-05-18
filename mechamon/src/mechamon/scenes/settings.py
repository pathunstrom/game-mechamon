import ppb
from ppb import keycodes

import mechamon


class Scene(ppb.Scene):

    background_color = mechamon.BRAND_CONTRAST_COLOR

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = ppb.Font(mechamon.TITLE_FONT, size=mechamon.TEXT_RENDER_SIZE)
        self.add(
            ppb.Sprite(
                image=ppb.Text(
                    'Settings',
                    font=self.font,
                    color=mechamon.BRAND_FONT_COLOR
                ),
                size=mechamon.TITLE_SIZE,
                position=ppb.Vector(0, 6)
            )
        )

        self.add(
            ppb.Sprite(
                image=ppb.Text(
                    'There are no settings, hit escape to return.',
                    font=self.font,
                    color=mechamon.BRAND_FONT_COLOR
                )
            )
        )

    def on_quit_requested(self, event, signal):
        signal(ppb.events.StopScene())
