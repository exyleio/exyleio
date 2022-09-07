# Game Mode

## Introduction

Exyle.io provides many different game modes with different maps and mechanics.
Each game mode also has its own rating algorithm and leaderboard to ensure the
most objective ranking and match making possible.

## Tutorial

- players can only access different game modes if they pass the tutorial

## Custom rooms

- players can create custom rooms where they can set a password and change the game settings.
- costs coin to create rooms
- supporters can create rooms for free

## Respawn

Some game modes allow respawn while others don't. Respawn cooldown is fixed at 5 seconds.

## Game modes

### Team Death Match

Team Death Match is a game mode where two groups of 8 players compete against each other for 10 minutes to get more kills off of each other.

| Field          | Value             |
| -------------- | ----------------- |
| Team size      | 8 players         |
| Special Reward | kills and damages |

- players can only change their weapons in the spawn area
- players can choose their next weapons in advance when they're outside the spawn area.
  Weapons will automatically switch once the player enters the spawn area.
- there is no limit to how many times players can reload
- pointing system
  - each kill adds 1 point to the team
  - when a player leaves, the points they've earned will be deducted from the team
  - when a player rejoins, and is put into the other team, the points they've earned will be transferred too.
- rating system: WIP

### Solo Death Match

Solo Death Match is a game mode where 8 players compete against each other for the most amount of kills.

| Field          | Value            |
| -------------- | ---------------- |
| Special Reward | kill and damages |

- players can only change their weapons before (re)spawn.
  Players can preselect which weapon to use on (re)spawn.
- rating system: WIP

### Capture Points

Capture Points is a game mode where two groups of 8 players compete against each other to take control of the capture points.

| Field          | Value                                   |
| -------------- | --------------------------------------- |
| Special Reward | kills, damages, and time spent on flags |

- there are 10 candidates for capture point location, of which 5 are selected at random
- a team wins when they capture all the points for 5 seconds,
  or have more points than the enemy team at the end of the match.
- a point is considered captured when the flag has been fully raised by a team.
- all flags are visible on the minimap, and is colored depending on the state of it.
  - green: captured by your team
  - yellow: not captured by any team
  - red: captured by enemy team
- rating system: WIP

### Battle Royale

Battle Royale is a game mode where up to 30 players are dropped in a large map and fight until one player is left standing.

| Field          | Value             |
| -------------- | ----------------- |
| Special Reward | last man standing |

- players can pick up weapons and attachments from different parts of the map
- a plasma circle closes in every two minutes
- if more than one player is alive until the end of the match, no one is awarded as the winner.
- there are no default attachments for weapons
- weapon attachments
- rating system: WIP

### Speedrun

Speedrun is a game mode where players have to navigate from start to finish in the most efficient way possible.

- it is similar to [krunker.io's bhop maps](https://www.youtube.com/watch?v=Z47Ssa4ZU9U)
  - but no checkpoints and falling off the map. Instead, players have to climb back up the pit.
- unlike other game modes, there is no such thing as an "end of a match" or deaths.
- option to toggle other player visibility and opacity
- option to toggle ghost player of their personal best record
- no weapons
- the timing is calculated locally, and is verified once a player reaches the end of the map,
  so this game mode only exists in one server. It will show up when players select different region,
  but the server is only located in one.
- there is an option to toggle a ghost for player's personal best and/or world best
- rating system: None. There is only a timing leaderboard

### Vehicles only

WIP

| Field          | Value      |
| -------------- | ---------- |
| Special Reward | most kills |

tank vs tank
jet vs jet

- has a vehicle unique to this game mode: tanks
- players can only change their vehicle before (re)spawn.
  Players can preselect which vehicle to use on (re)spawn.
- rating system: WIP

### Prop hunt

only in custom game modes
