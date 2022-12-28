import ppb

import mechamon.mixins as mixins
import mechamon.prefabs as prefabs
import mechamon.utils as utils
import mechamon.scenes.corral as corral

INTERACTABLE = "interactable"


class PlayerCharacter(mixins.PlayerOverworldMovement, ppb.Sprite):
    pass


class Scene(ppb.Scene):
    background_color = 207, 174, 117

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add(PlayerCharacter())
        self.add(
            prefabs.interactable.Exit(text="Corral", next_scene=corral.Scene),
            tags=[INTERACTABLE],
        )

    def on_quit_requested(self, event, signal):
        signal(ppb.events.StopScene())

    def on_interact_requested(self, event, signal):
        player = next(self.get(kind=PlayerCharacter))
        for interactable in self.get(tag=INTERACTABLE):
            if utils.collision_rect_to_rect(interactable, player):
                interactable.interact(player, signal)
