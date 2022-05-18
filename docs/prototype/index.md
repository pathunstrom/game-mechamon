# Mekanik Corral Prototype

This section details the requirements, decisions and features of the prototype
version of the game.

## The Core Loop

Following the [spiral method][d.king-spiral-method], the prototype isn't going
to be tiny sandboxes like I tend to do, but a more or less functional game with
stripped down features that I can expand as I work on them.

With the idea that I want a main menu, settings, the main camp/garage,
explorable areas and battle maps, that gives us the initial layout of required
sections:

1. Main menu
2. Settings
3. Main Camp
4. Customizing
5. The Beach
6. Battle Start
7. Battlefield: Low Tide
8. Battle End

The objects this suggests:

1. Menus (overlays with menus and buttons)
2. Player Character
3. Mecha (playable, but will also need to be controlled by AI)
4. Parts
   1. Guns
   2. Shells
   3. Chassis
5. Terrain
   1. Just treat as blocking for now

To turn into a strict checklist of requirements:

1. Menu
   1. Start Game (DONE!)
   2. Settings (DONE!)
   3. Quit (DONE!)
2. Camp
   1. Player (DONE)
   2. AI Bot
   3. Game Quit Prompt
      1. Quit with escape (DONE)
   4. Edit Menu
   5. Exit to Beach
   6. Interact Prompt
      1. Control Wired For Interaction (DONE)
      2. Key to the bot to customize
      3. Key to exit to shift to Beach
3. The Beach
   1. Some terrain bits
   2. Player
   3. Player bot - follows the player around.
   4. Wild bots
      1. For now, use prompt system to start battles
   5. Exit to Camp
4. Enter Battle
   1. Show enemy bot
   2. Show player bot
   3. Any key to continue
5. Low Tide battle map
   1. Plain ground
   2. Show limits of arena?
   3. Maybe a rock?
   4. AI for the enemy bot (it's just a copy of the player bot)
   5. Battle Mechanics
      1. Hard points with fixed rotation cones
      2. Separated speeds for each individual direction
      3. 
6. End Battle Screen
   1. Show loser
   2. Show winner
   3. Any key to return to the original map.
7. Settings
   1. Screen shake on/off
   2. Hold To Fire/Press to Fire
   3. Return to menu (DONE!)


This should complete the core. Future features as needed.


## Future Bits:

1. Collection of parts
2. Building Teams
3. Robot Selection - Battles
4. Robot Selection - Traveling Companions
5. Repair and Upgrade Mechanics
6. Randomized Battle Terrain
7. Stat System
8. Game Saves

[d.king-spiral-method]: https://twitter.com/delaneykingrox/status/1468804328857038849?s=20&t=Y1e55Ti05qeWCm9_PoWpIg