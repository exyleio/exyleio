# Database

## Introduction

Exyle.io uses a single [Redis](https://redis.io) cluster to store all its data.

## Structure

:::tip Useful links

- [Data types](https://redis.io/docs/data-types)

:::

|                                          Key |    Type    |                 Field/Member                 |                  Value/Score                   |
| -------------------------------------------: | :--------: | :------------------------------------------: | :--------------------------------------------: |
|                           `rank:<game-mode>` | Sorted Set |                player nanoid                 |                   rank point                   |
|           `rank:<game-mode>:days-number-one` | Sorted Set |                player nanoid                 | total number of days player was in the #1 rank |
| `rank:<game-mode>:longest-number-one-streak` | Sorted Set |                player nanoid                 |           player's longest #1 streak           |
|                                    `rank:xp` | Sorted Set |                player nanoid                 |                   Player XP                    |
|               `player:<player-nanoid>:items` |    Set     |                 item nanoid                  |                       -                        |
|                            `player:<nanoid>` |    Hash    | `username`, `coins`, `highest-rank`, `title` |           in-exhaustive player data            |
