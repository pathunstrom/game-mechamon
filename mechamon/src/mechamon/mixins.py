import ppb

import mechamon.constants as constants


class PlayerOverworldMovement(ppb.sprites.BaseSprite):
    speed = 4

    def on_update(self, event, signal):
        controls = event.controls
        move_vector = ppb.Vector(
            controls[constants.CONTROLS_HORIZONTAL],
            controls[constants.CONTROLS_VERTICAL],
        )
        if move_vector:
            self.position += move_vector.scale_to(self.speed) * event.time_delta
