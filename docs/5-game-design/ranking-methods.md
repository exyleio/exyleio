# Ranking methods

## OpenSkill

OpenSkill is a implementation of a ranking method proposed in the paper
[A Bayesian Approximation Method for Online Ranking (2011)
](https://www.csie.ntu.edu.tw/~cjlin/papers/online_ranking/online_journal.pdf)
by **Ruby C. Weng** and **Chih-Jen Lin**. We are using the partial-pair
Bradley-Terry model to be specific because of its marginal, but consistently
better performance and accuracy.

## Simple time comparison

For game modes such as
[Speedrun](/docs/game-design/game-modes/standard/speedrun) and
[Prop hunt](/docs/game-design/game-modes/special/prop-hunt), a simple time
comparison algorithm is used to rank the players.

## Why not this?

### Elo

Though Elo is definitely a popular ranking algorithm used in many competitive
online games, it has several shortcomings that make it unsuitable and
undesirable for our purpose. Here's few of them: the inability to accurately
rank players in a non-1v1 match, slow convergence time, inflation over time,
occasional more-than-acceptable levels of fluctuation, etc.

### Glicko 2

Glicko is an algorithm often regarded as a suitable replacement of Elo, and it
does solve many of its issues, but it also comes with some of its own set of
problems. Here's a few of them: it is still not designed for non-1v1 matches,
there's no immediate feedback because ranks only update once every so often,
ranks decay over time (volatility), the system can be exploited by deliberately
under-performing then popping off, etc.

### TrueSkill

TrueSkill is just perfect. It is actually designed to rank gamers even for
non-1v1 matches, and has no significant drawbacks when it comes to the
technology itself. However, it can only be used for Xbox Live games or
non-commercial games due to its license.
