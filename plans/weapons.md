# Weapons plan

## Introduction

- Players have 375 HP
- Head shot deals double damage
- No default attachments in Battle Royale
- All players have 4 options to deal damage: Primary weapon, Secondary weapon, sidearm, and melee
- Weapon swap delay is fixed at 0.6 second

## Weapons

|          Weapon | Base Player Damage per bullet | Vehicle Damage | Base Swing | Jump Swing |  Fire cooldown (seconds)  | Reload duration (seconds) | Walk speed | Clip size | [Fire type\*](#full-auto-vs-semi-auto) | Head penetration | Bullet type | BR Ammo type | Default scope | Purpose                        |
| --------------: | :---------------------------: | :------------: | :--------: | :--------: | :-----------------------: | :-----------------------: | :--------: | :-------: | :------------------------------------: | :--------------: | :---------: | :----------: | :-----------: | :----------------------------- |
|    Sniper Rifle |              200              |      200       |    TODO    |    TODO    |            2.5            |            3.0            |    90%     |     5     |               Semi-Auto                |       yes        | projectile  |    Heavy     |      8x       | Long distance burst damage     |
|        Revolver |              125              |       50       |    TODO    |    TODO    |            1.0            |            2.5            |    100%    |     6     |               Semi-Auto                |       yes        |   hitscan   |    Light     |      4x       | short-mid range burst damage   |
|   Assault Rifle |              60               |       15       |    TODO    |    TODO    |           0.12            |            1.5            |    95%     |    30     |               Full-Auto                |        no        |   hitscan   |    Rifle     |      2x       | short-mid range tracking       |
|     Burst Rifle |              20               |       15       |    TODO    |    TODO    | [0.1/0.6\*](#burst-rifle) |            2.0            |    90%     |    18     |     Semi-Auto (3 shots per click)      |        no        |   hitscan   |    Light     |      2x       | Assault Rifle but more burst-y |
|         Shotgun |              32               |       10       |    TODO    |    TODO    |            0.8            |            2.0            |    95%     |     5     |    Semi-Auto (8 bullets per click)     |        no        |   hitscan   |   Shotgun    | 2x iron sight | Short range burst damage       |
|             SMG |              60               |       20       |    TODO    |    TODO    |            0.1            |            1.5            |    95%     |    25     |               Full-Auto                |        no        |   hitscan   |    Light     | 2x iron sight | short range tracking           |
|        Crossbow |              375              |       20       |    TODO    |    TODO    |            N/A            |            2.0            |    100%    |     1     |               Semi-Auto                |        no        | projectile  |    Arrow     | 2x iron sight | short range insta-kill         |
|         minigun |              50               |       20       |    TODO    |    TODO    |            0.1            |            5.0            |    80%     |    100    |               Full-Auto                |        no        |   hitscan   |    Heavy     | 2x iron sight | Anti-vehicle tracking          |
| Rocket Launcher |      [20\*](#explosions)      |      1000      |    TODO    |    TODO    |            N/A            |            3.0            |    80%     |     1     |               Semi-Auto                |        no        | projectile  |     N/A      | 2x iron sight | Anti-vehicle burst damage      |
|          Pistol |              50               |       10       |    TODO    |    TODO    |           0.15            |            1.5            |    100%    |    15     |               Semi-Auto                |        no        |   hitscan   |    Light     | 2x iron sight | Sidearm                        |

## Melee

| Weapon | Base Player Damage | Fire delay (seconds) |
| -----: | :----------------: | :------------------: |
|  Knife |        200         |          1           |
|   Fist |         50         |          1           |

## Grenades

### Frag

TODO

### Smoke

TODO

### Stun

TODO

## Technical details

### Full Auto vs Semi Auto

There are two major fire types in Exyle.io.
The most common type is Semi-Auto where you have to click multiple times to shoot multiple shots.
Full-Auto weapons on the other hand, shoots automatically as long as there are ammos left in the clip.
Basically, Full-Auto weapons allow you to hold down the fire key, while Semi-Auto doesn't.

### Head Penetration

Sniper Rifle and Revolver have the ability to penetrate enemy head and shoot the next target (if there are any).
This only works for head-shots, and the damage is not reduced after a penetration.
Bonus points are rewarded for each penetrations.

### Explosions

Explosive weapons in Exyle.io act quite similar to TNTs in Minecraft.
When a RPG projectile or a grenade explode, it casts invisible rays in all direction,
and the more ray hits a player, more damage is dealt.
I like to think this as number of fragments that hit the player.
The number and the length of these rays can be adjusted to tweak the damage and range.

### Burst Rifle

As the name implies, the burst rifle shoots bullets in short bursts.
Each burst consist of 3 bullets which fire after 0.1 second after the previous one,
and you can only initiate a burst every 0.6 second.
If you are familiar with krunker.io, you can think of it as the famas weapon.

### Swing

TODO
