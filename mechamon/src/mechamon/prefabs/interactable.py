import ppb

import mechamon.constants as constants


class Interactable(ppb.sprites.BaseSprite):
    """Defines the interactable interface"""

    def interact(self, player, signal):
        pass


class Exit(Interactable, ppb.RectangleSprite):
    width = 2
    text = "Exit"
    next_scene = None
    replace_scene = True

    def __init__(self, **kwargs):
        print(f"Setting up Exit {self.text}")
        super().__init__(**kwargs)
        if self.next_scene is None:
            raise ValueError("Must have a next scene for an exit.")
        self.image = ppb.Text(self.text, font=constants.TEXT_FONT)

    def interact(self, player, signal):
        event = ppb.events.StartScene
        if self.replace_scene:
            event = ppb.events.ReplaceScene
        signal(event(self.next_scene))
