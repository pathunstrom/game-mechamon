import ppb

import mechamon


class PlayerCharacter(ppb.Sprite):
    speed = 4

    def on_update(self, event, signal):
        controls = event.controls
        move_vector = ppb.Vector(
            controls[mechamon.CONTROLS_HORIZONTAL],
            controls[mechamon.CONTROLS_VERTICAL]
        )
        if move_vector:
            self.position += move_vector.scale_to(self.speed) * event.time_delta


class Scene(ppb.Scene):
    background_color = (200, 75, 75)

    def __init__(self, *args, **kwargs):
        super(Scene, self).__init__(*args, **kwargs)

        self.add(PlayerCharacter())

    def on_quit_requested(self, event, signal):
        signal(ppb.events.StopScene())
