# Overview

## Introduction

Each weapons are tactically distinct and has properties that make it suitable
for certain types of situations.

- Players have 375 HP
- Head shot deals double damage
- All players have 4 options to deal damage: Primary weapon, Secondary weapon,
  sidearm, and melee
- Weapon swap delay is fixed at 0.6 second
- Game-mode-specific information can be found in the
  [game-modes document](../game-modes/common).

## Guns

|          Weapon | Base Player Damage per bullet | Vehicle Damage | Recoil | Fire cooldown (seconds) | Reload duration (seconds) | Damage falloff | Clip size | Walk speed | Base Swing | Jump Swing | [Fire type\*](#full-auto-vs-semi-auto) | Head penetration | hitscan distance | bullet velocity | BR Ammo type | Default scope | Purpose                      |
| --------------: | :---------------------------: | :------------: | :----: | :---------------------: | :-----------------------: | :------------: | :-------: | :--------: | :--------: | :--------: | :------------------------------------: | :--------------: | :--------------: | :-------------: | :----------: | :-----------: | :--------------------------- |
|    Sniper Rifle |              200              |      160       |  WIP   |           2.5           |            3.0            |      WIP       |     5     |    90%     |    WIP     |    WIP     |               Semi-Auto                |       yes        |        0         |       WIP       |    Heavy     |      8x       | Long distance burst damage   |
|   Hunting Rifle |              100              |       80       |  WIP   |          1.25           |            2.0            |      WIP       |    10     |    95%     |    WIP     |    WIP     |               Semi-Auto                |        no        |       WIP        |       WIP       |    Light     |      4x       | Sniper but weaker and faster |
|   Assault Rifle |              60               |       20       |  WIP   |          0.12           |            1.5            |      WIP       |    30     |    95%     |    WIP     |    WIP     |               Full-Auto                |        no        |       WIP        |       WIP       |    Rifle     |      2x       | short-mid range tracking     |
|         Shotgun |              32               |       10       |  WIP   |           0.8           |            2.0            |      WIP       |     5     |    95%     |    WIP     |    WIP     |    Semi-Auto (8 bullets per click)     |        no        |       WIP        |       WIP       |   Shotgun    | 2x iron sight | Short range burst damage     |
|             SMG |              60               |       20       |  WIP   |           0.1           |            1.5            |      WIP       |    25     |    95%     |    WIP     |    WIP     |               Full-Auto                |        no        |       WIP        |       WIP       |    Light     | 2x iron sight | short range tracking         |
|         minigun |              70               |       30       |  WIP   |           0.1           |            5.0            |      WIP       |    100    |    80%     |    WIP     |    WIP     |               Full-Auto                |        no        |       WIP        |       WIP       |    Heavy     | 2x iron sight | Anti-vehicle tracking        |
| Rocket Launcher |      [20\*](#explosions)      |      1000      |  WIP   |           N/A           |            3.0            |      WIP       |     1     |    80%     |    WIP     |    WIP     |               Semi-Auto                |        no        |        0         |       WIP       |     N/A      | 2x iron sight | Anti-vehicle burst damage    |
|          Pistol |              50               |       10       |  WIP   |           0.3           |            1.5            |      WIP       |    15     |    100%    |    WIP     |    WIP     |               Semi-Auto                |        no        |       WIP        |       WIP       |    Light     | 2x iron sight | Sidearm                      |

<!-- put damage falloff graph here as well as the python matplotlib code used to create it -->

## Melee

| Weapon | Base Player Damage | Fire delay (seconds) |
| -----: | :----------------: | :------------------: |
|  Knife |        200         |          1           |
|   Fist |         50         |          1           |

## Grenades

|        Weapon | Base Player Damage | Fire delay (seconds) |
| ------------: | :----------------: | :------------------: |
|  Frag Grenade |        200         |          1           |
| Smoke Grenade |         50         |          1           |
|  Stun Grenade |         50         |          1           |

## Full Auto vs Semi Auto

There are two major fire types in Exyle.io.
The most common type is Semi-Auto where you have to click multiple times to shoot multiple shots.
Full-Auto weapons on the other hand, shoots automatically as long as there are ammos left in the clip.
Basically, Full-Auto weapons allow you to hold down the fire key, while Semi-Auto doesn't.

## Head Penetration

Some weapons have the ability to penetrate enemy head and shoot the next target (if there are any).
This only works for head-shots, and the damage is not reduced after a penetration.
Bonus points are rewarded for each penetrations.

## Explosions

Explosive weapons in Exyle.io act quite similar to TNTs in Minecraft.
When a RPG projectile or a grenade explode, it casts invisible rays in all direction,
and the more ray hits a player, more damage is dealt.
You can think of this as the number of fragments that hit the player.
The number and the length of these rays can be adjusted to tweak the damage and range.
Also, in case of RPGs, the rays are longer and more dense in the front,
so players are encouraged to make a direct hit as instead of relying on the splash damage.

## Crosshair

custom crosshair client only

## Swing

WIP

## Recoil

WIP

## Damage falloff

WIP

## Fire Rate

Due to super bullet issue, fire rate can not be higher than 60 bullets / sec
