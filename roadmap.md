# Exyle.io Roadmap

Game development is no easy task.
Making a quality game takes a surprising amount of time and effort.
That's why I have divided the development processes into different stages so it is much easier for me to manage different tasks, and also prevent myself from falling into the pit of unproductiveness.
The following are the five major stages of development:

## Planning

**(we are here)**

This is the very first stage of the development process.
No code written at this stage is expected to survive until the release.
In this stage, we explore different options and make technical decisions that are hard to change in the future.
This includes the game engine and related libraries, online infrastructure, hosting provider, code architecture, and many many more.
We also prepare as much extensive documentations and planning details as possible.

## Proof of concept

Hold until: [bevyengine](https://github.com/bevyengine/bevy) 0.8 releases

If a general outline is more or less complete,
it is time to build the technical foundation.
This is the stage where we build the backbone of the game.
Basically every code written after this point is only an addition to the code written at this stage of the development.

## Alpha dev

Now that we have a solid foundation to work on, it's time to make the game feel like an actual game.
In this stage, we fine tune the "game feel" until it's just right.
This includes the control, weapon balance, map layout, server region selection, etc.

## Beta dev

In this stage, we work on non-critical and/or nice-to-have features such as clans, friends, nice UI, pretty 3D assets, etc.
This is the most repetitive and boring part of the development process in terms of technical complexity,
but in terms of visuals and presentation, it is the most important stage by a long shot.

## Release

Hold until: [webgpu](https://www.w3.org/TR/webgpu/) becomes a web standard. Learn more about it [here](./plans/webgpu.md).

Once we smooth out all the rough edges, we can finally deliver the game to the public.
Hopefully the game can pay for itself at this point.
