# Mechamon Design

Like all parts of this documentation, this is a living document and subject to change.
While the [prototype](prototype) is operating on assumptions, this will be used to record intentional 
design 
thoughts.

## Building and Customization

I want the customization to not be raw menu based.
While this is fine in other robot games,
I want a feeling of the physicality of customization and want to bring a
lightweight simulation style game to the customization:

Menus are replaced with labeled (and smart sorting) drawers where you can
select the parts you want.

This would necessitate certain constraints on part design:

Much of the performance of a model should be in hidden, invisible, or superficial
places.
Base speed, base health, accuracy, number of weapon slots, how they combine into
fire control.

External parts (legs, arms, eyes, armor shells) should be modifications on the base
stats allowing fine-tuning of the performance of the robot.

In general, the cores can be the primary differentiator in raw power, with the
external parts being free to collect at any time.

The actual process of building should be more or less like building a PC: you
need to remove the external casing to reach the easily available parts, and
those need to be removed to access core parts. All of this needs an interface
that makes managing a change feel accessible.

Also, make sure there is a "simplified" UI for folks who would prefer to skip
the simulation game.
