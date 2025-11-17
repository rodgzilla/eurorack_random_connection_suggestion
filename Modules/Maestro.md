---
tags:
  - modular
  - music
  - lfo
  - sequencer
  - module
url: https://acidraintechnology.com/products/maestro
manufacturer: "[[Acid rain technology]]"
controls:
  - high
  - low
  - square
  - random
  - save
  - load
  - clock
  - ramp up
  - rand down
  - triangle up
  - triangle down
  - smooth
  - bipolar
  - chain
  - 1/2
  - 1/4
  - 1/8
  - 1/16
  - 1/32
  - triplet
  - slow
  - mute
  - track 1
  - track 2
  - track 3
  - track 4
  - track 5
  - track 6
inputs:
  - clock
  - reset
  - track 1 gate
  - track 2 gate
  - track 3 gate
  - track 4 gate
  - track 5 gate
  - track 6 gate
outputs:
  - clock
  - reset
  - track 1
  - track 2
  - track 3
  - track 4
  - track 5
  - track 6
up:
  - "[[Eurorack module]]"
  - "[[Clock]]"
  - "[[Low frequency oscillator (LFO)]]"
---
# Concept

[[Maestro]] is a 6 channel clocked modulation controller inspired by the automation lanes found in [[Digital audio workstation (DAW)]] software, brought into [[Eurorack]] and made playable and performable. [[Maestro]] will push and pull the parameters of your other modules with rapid or slowly evolving voltages, always in perfect sync with eachother and the rest of your system.

![[Maestro_2000px_12.21.23_740x.webp]]

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
