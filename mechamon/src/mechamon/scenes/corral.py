import ppb

import mechamon.constants as constants
import mechamon.mixins as mixins
import mechamon.scenes.beach as beach
import mechamon.utils as utils
import mechamon.prefabs as prefabs


INTERACTABLE = "interactable"


class PlayerCharacter(mixins.PlayerOverworldMovement, ppb.Sprite):
    pass


class Scene(ppb.Scene):
    background_color = (200, 75, 75)

    def __init__(self, *args, **kwargs):
        super(Scene, self).__init__(*args, **kwargs)
        self.add(PlayerCharacter())
        self.add(
            prefabs.interactable.Exit(
                position=ppb.Vector(0, 5), text="Beach", next_scene=beach.Scene
            ),
            tags=[INTERACTABLE],
        )

    def on_quit_requested(self, event, signal):
        signal(ppb.events.StopScene())

    def on_interact_requested(self, event, signal):
        player = next(self.get(kind=PlayerCharacter))
        for interactable in self.get(tag=INTERACTABLE):
            if utils.collision_rect_to_rect(interactable, player):
                interactable.interact(player, signal)
