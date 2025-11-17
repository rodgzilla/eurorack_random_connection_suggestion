---
tags:
  - modular
  - music
  - module
  - sampler
url: https://squarp.net/rample/
manufacturer: "[[Squarp instruments]]"
controls:
  - encoder 1
  - encoder 2
  - encoder 3
  - encoder 4
  - pitch
  - bits
  - filter
  - freeze
  - assign / levels
  - listen
  - master encoder
  - volume
inputs:
  - gate 1
  - gate 2
  - gate 3
  - gate 4
  - cv 1
  - cv 2
  - cv 3
  - cv 4
  - midi in
  - midi thru
outputs:
  - out 1
  - out 2
  - out 3
  - out 4
  - mix
up:
  - "[[Eurorack module]]"
  - "[[Sample]]"
  - "[[Eurorack voice]]"
---

# Concept

[[Eurorack]] 4-voice sample player & audio processor

![[Pasted image 20240521115013.jpg]]


# Use

## Voice levels

To control the level / overdrive of the various voices, we can hold the `assign` button and then `listen` to enter the Levels effect mode.

## Mode buttons

### Button 1

Button 1 controls [[Pitch]] on single press and start point on double press.

### Button 2

Button 2 controls bits on single press and length on double press.

### Button 3

Button 3 controls [[Filter]] on single press and [[Envelope]] on double press.

### Button 4

Button 4 controls freeze on single press and run mode on double press.


# Kits
## Selecting a kit

We can select a kit by rotating the encoder and load it by pressing it. We can scroll fast by holding `assign` while rotating the encoder.

When scrolling through the kits, we can press the buttons 1, 2, 3 and 4 to display the samples names in the kit.

If we hold `assign` while loading a kit, the FX parameters will be kept.

## What's inside a kit?

Each kit folder includes up to 12 [[Sample]]s (.wav files) per voice. There are 4 voices: audio outputs `SP1`, `SP2`, `SP3` and `SP4`.

If a voice includes more than 1 [[Sample]], this voice use the "multi-layers" features. On the example below, `SP1`, `SP2` and `SP3` are using layers.

![[inside_a_kit.webp]]


## Trig a [[Sample]]

Use the gate input 1 to play `SP1` ([[Sample]] 1), gate input 2 to play `SP2`, gate input 3 to play `SP3` and gate input 4 to play `SP4`.

You can see the [[Sample]]s playing on the screen, thanks to the 4 vu-meers:

![[screen_vu-meters.webp]]

Each [[Sample]] is always outputted on its dedicated audio output (`1`, `2`, `3`, `4`) and unplugged audio outputs are normalled to `mix` output.

To pre-listen a [[Sample]], hold `listen` and press the mode buttons `1`, `2`, `3` or `4`.

Double press `listen` to stop all [[Sample]]s.

# General

## Exit

Press `listen` to quit the current mode (kit select, assign mode, settings, ...).

## Assign a CV input

Each of the 4 CV inputs can be assigned to any effect / parameter of any voice:
- Press `assign`
- Select the CV input (►`1`, ►`2`, ►`3`, ►`4`),
- Select the [[Sample]](s) to control (`SP1`, `SP2`, `SP3`, `SP4` or `ALL SAMPLES),
- Select the effect / parameter to assign (pitch, bits, filter, freeze, start, length, env, run, levels, layers, T-F (trig freeze), v/oct).

T-F (trig freeze) will enable the freeze effect only if a gate is detected on this CV input.

## Mute groups

Mute groups allow each [[Sample]] to be muted by one or more [[Sample]]s, very handy to create open / close and conditional behaviors. While holding `assign`, select the sample to be group-muted (by pressing `1`, `2`, `3` or `4`) and then select the [[Sample]] triggering the mute (up to 3 [[Sample]]s).

Let's take a few examples:

- `SP1` muted by `SP2` -> hold `assign`, press `1`, `2`, release `assign`.
- `SP2` muted by `SP1` + `SP4` -> hold `assign`, press `2`, `1`, `4`, release `assign`.
- Delete `SP1` mute groups -> hold `assign`, press `1`, release `assign`.

## Layers

Press `assign`, release it, then press `1`, `2`, `3` or `4` to enter the layers mode: the screen displays the running layer of the voice.

![[layer_mode.webp]]


Press once again `1`, `2`, `3` or `4` to enter the per voice layer playback mode (manual, random, cyclic, ...) of the currently selected voice.

If the `LAYERS` setting is set to `MANUAL`, you can manually select the layer with the main encoder. Press the encoder to listen to the selected layer while scrolling through them.

# Audio effects and parameters workflow

## Effects rack

Each voice has it own "rack" of effects, and all audio effects can be enabled at the same time, allowing you to manipulate your samples in real time, from a gentle lowpass ([[Filter]]) to a massive destruction!

Each potentiometer controls the selected effect amount, per voice. Pot 1 will always control `SP2`, Pot 2 will control `SP2`, ...

Rotate a potentiometer (or select an effect with `1`, `2`, `3` or `4`) to display the "4-voice effect values" view:

![[effects_workflow-01.webp]]


## Audio effects

Select an audio effect ([[Pitch]], bits, filter, freeze) with `1`, `2`, `3` or `4`.

Tip: Edit the 4-voice values at the same time by holding an effect button and rotating the menu encoder (e.g. hold `PITCH`  + rotate the encoder).

### [[Pitch]]

A great sounding [[Pitch]] engine, based on a 6-pole interpolator. The range goes from -1 octave to +1 octave:

![[effect_pitch-01.webp]]

### Bits

Two different [[Bitcrushing]] [[Algorithm]]s, based on [[Sample rate reduction]] and resolution reduction. It produces [[Distortion]] and warms up the audio signal:

![[effect_bits-01.webp]]

### [[Filter]]

A low [[Resonance]] [[Filter]], DJ-style, cutting off the high frequencies ([[Low pass filter]]) or the low frequencies ([[High pass filter]]):

![[effect_filter-01.webp]]

### Freeze

When enabled (pot ≠ midpoint), [[Rample]] will sample and loop a fraction of the played waveform, creating a glitching effect:

![[effect_freeze-01.webp]]

Uniquely to the freeze effect, you can activate / deactivate the effect independently of the amount, by assigning a CV input to "T-F" (trig freeze).

### Levels

Hold `assign` and press `listen` to enter the levels mode. Turn the knob to left to decrease the voice gain, or turn to the right to drive the signal

![[effect_levels-01.webp]]

## Advanced parameters

Double tap `1`, `2`, `3` or `4` to select start point, length, env or run mode.

### Start point

Set the beginning of the [[Sample]] playback. If setting `SLICER = EXP`, the start point goes from 0% to 100% of the sample total length. If `SLICER` is set to a value (`/8/`, `/16`, `/32`, `/64`, `/128`, `/12`, `/12`, `/24`, `/48`), the [[Sample]] length is divided by this value into equal parts, handy to edit the start point of your [[Sample]] "in beats".

![[effect_start-01.webp]]
### Length

Set the duration of the [[Sample]]. Depending on the setting `SLICER = EXP`, the duration goes from 100% to 0% of the [[Sample]] total length. If `SLICER` is set to a value (`/8/`, `/16`, `/32`, `/64`, `/128`, `/12`, `/12`, `/24`, `/48`), the [[Sample]] length is divided by this value into equal parts, handy to edit the length of your [[Sample]] "in beats".

![[effect_length-01.webp]]

### Env

Turn the knob to the left to add [[Sample]] attack, or turn to the right to add [[Sample]] decay.

![[effect_env-01.webp]]

### Run mode

3 types of [[Sample]] playback:
- One shot -> a trig plays the [[Sample]] entirely.
- Toggle loop -> a trig alternatively plays / stops the sample.
- Gate high only -> [[Sample]] played only when gate is high.

![[effect_run-01.webp]]

## Momentary effects

Press and hold `1`, `2`, `3` or `4` to access the effect in "momentary mode". While holding, you can play with an effect parameter knob to change the sound, however the effect will be set back to its original value after releasing `1`, `2`, `3` or `4`.

In "momentary mode", turning the main encoder will affect all four voices. Pressing the encoder applies the momentary parameters.


# Patching ideas

```dataview
TABLE modules AS "Modules"
FROM #patching-idea 
WHERE contains(modules, [[]])
SORT file.cdate ASC
```
# Jams

```dataview
TABLE modules AS "Modules"
FROM #jam  
WHERE contains(modules, [[]])
SORT file.cdate ASC
```
