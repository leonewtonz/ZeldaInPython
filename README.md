# ZeldaInPython

- VS Code Shortcut:
    - https://cult.honeypot.io/reads/20-vs-code-shortcuts-developers/
    - https://davidamos.dev/5-vs-code-shortcuts/

This is my personal project.
Credited to https://github.com/SpyderGamer/Zelda-with-Python/

## Class Level:
Important concept in pygame design
### visible_sprites:
- group for sprites that will be drawn (only group that draws sprites)
### ostacle_sprites:
-  group for sprites that player cab collide with



# Collision (@ Jun 26, 2023)
- Apply horizontal movement
- Check horizontal (x) collisions
- Do the same for vertical movement


# Camera and Overlap (@ Jun 26, 2023)
- Customizing the group
- Group's purpose:
  - Store and draw sprites
  - Call the update method
## Overlap
- The other of which one top is now based on the order when sprites were created. This create silly image. Because some sprite (rock) was create after player - this happen because the camera re-draw)
- This is why we need YSort, the sprites have higher y value will be on top

# Finished most basic mechanic of game. The rest will focus more on graphics.
- This is when we use Tiled Application (Free) to organize the map, player, enemy
