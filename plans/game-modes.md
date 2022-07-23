# Game Mode

## Introduction

Game modes are different types game mechanics which provide diverse ways to enjoy the game.
Each game mode has its own rating algorithm and leaderboard to ensure the most objective ranking and match making possible.
Game modes (and servers) will be released gradually as the game grows in size to ensure at least some level of player activity in each lobby.
Also, some maps may not be available, or only available in certain game modes.

Related documents:

- [weapons](./weapons.md)

## How game modes are arranged

Exyle.io uses the Server-Lobby-Room model to organize different rooms.

On the highest level, there are the servers which are physical hardware located on specific locations where they can provide a responsive,
low latency experience.
Within each server, there are different lobbies which correspond to one and only one game mode.
Finally, there are multiple rooms within each lobby which can grow or shrink in size in response to the number of concurrent players.

Here is a simple tree-like structure to help you understand how rooms are organized.

```
Region 1 server
├── Game mode 1 Lobby
|    ├── Room 1
|    ├── Room 2
|    └── ...
└── ...

Region 2 server
├── Game mode 1 Lobby
|    ├── Room 1
|    ├── Room 2
|    └── ...
└── ...

...
```

Private lobby where players can customize game modes

## Rewards

At the end of each round, each players are rewarded with coins for their performance (and participation).
Players with the best performance are rewarded extra coins. This is called special rewards.
In case two or more players have the same performance, whichever reached the value first will be rewarded.
One player can receive multiple special rewards.

## Respawn

Some game modes allow respawn while others don't. Respawn cooldown is fixed at 5 seconds.

## Classic Game modes

### Team Death Match

Team Death Match is a game mode where two groups 8 players compete against each other for 10 minutes to get more kills off of each other.

| Field          | Value             |
| -------------- | ----------------- |
| Team size      | 8 players         |
| Special Reward | kills and damages |

- players can only change their weapons in the spawn area
- players can choose their next weapons in advance when they're outside the spawn area.
  Weapons will automatically switch once the player enters the spawn area.
- respawn logic:
  - there are 8 different spawnpoints per spawn area
  - players spawn randomly in different spawn points
  - players cannot press the respawn button for 5 seconds after death
- there is no limit to how many times players can reload
- pointing system
  - each kill adds 1 point to the team
  - when a player leaves, the points they've earned will be deducted from the team
  - when a player rejoins, and is put into the other team, the points they've earned will be transferred too.
- rating system: TODO

### Solo Death Match

Solo Death Match is a game mode where 8 players compete against each other for the most amount of kills.

| Field          | Value            |
| -------------- | ---------------- |
| Special Reward | kill and damages |

- players can only change their weapons before (re)spawn.
  Players can preselect which weapon to use on (re)spawn.
- respawn logic:
  - there are 8 different spawnpoints that are distributed evenly throughout the map
  - if there are no players, they spawn on the middlemost spawnpoint (manually picked by the developers)
  - players cannot press the respawn button for 5 seconds after death
- rating system: TODO

### Capture Points

Capture Points is a game mode where two groups of 8 players compete against each other to take control of the capture points.

| Field          | Value                                   |
| -------------- | --------------------------------------- |
| Special Reward | kills, damages, and time spent on flags |

- there are 10 candidates for capture point location, of while 5 are selected at random
- a team wins when they capture all the points for 5 seconds,
  or have more points than the enemy team at the end of the match.
- a point is considered captured when the flag has been fully raised by a team.
- all flags are visible on the minimap, and is colored depending on the state of it.
  - green: captured by your team
  - yellow: not captured by any team
  - red: captured by enemy team
- rating system: TODO

### Bomb Game

Bomb Game is a game mode where two groups of 4 players diffuse and detonate bombs planted across the map.

| Field          | Value                                   |
| -------------- | --------------------------------------- |
| Special Reward | kills, damages, and time spent on bombs |

- there are 6 candidates for bomb plantation location of which 3 are selected at random
  - each bomb can exist in either one of two location
- minimap
  - initially, the diffusing team can only see 6 question marks on the map
  - once a bomb has been found, its position will be shown on the map, removing one question mark.
  - the detonating team can always see the position of all the bombs
- how to win
  - The diffusing team wins if they successfully diffuse all 3 bombs
  - The defending team wins if at least 1 bomb is not diffused until the end of the match
- rating system: TODO

## Special Game modes

### Battle Royale

Battle Royale is a game mode where up to 30 players are dropped in a large map and fight until one player is left standing.

| Field          | Value             |
| -------------- | ----------------- |
| Special Reward | last man standing |

- players can pick up weapons and attachments from different parts of the map
- a plasma circle closes in every two minutes
- if more than one player is alive until the end of the match, no one is awarded as the winner.
- there are no default attachments for weapons
- rating system: TODO

### Speedrun

Speedrun is a game mode where players find their way to a certain target and try to do so as quickly as possible

- it is similar to [krunker.io's bhop maps](https://www.youtube.com/watch?v=Z47Ssa4ZU9U)
- unlike other game modes, there is no such thing as an "end of a match" or deaths.
- no weapons can be used in this game mode (only fists)
- the timing is calculated locally, and is verified once a player reaches the end of the map,
  so this game mode only exists in one server. It will show up when players select different region,
  but the server is only located in one.
- there is an option to toggle a ghost for player's personal best and/or world best
- rating system: None. There is only a timing leaderboard

### Vehicles only

TODO

| Field          | Value      |
| -------------- | ---------- |
| Special Reward | most kills |

- has a vehicle unique to this game mode: tanks
- players can only change their vehicle before (re)spawn.
  Players can preselect which vehicle to use on (re)spawn.
- rating system: TODO
