---
tags:
  - modular
  - vco
  - voice
  - music
  - module
url: https://noiseengineering.us/products/manis-iteritas-alia
manufacturer: "[[Noise Engineering]]"
controls:
  - pitch
  - lpf
  - envelope
  - bash
  - smash
  - saw mod
  - profundity
  - skin / liquid / metal
  - bass / alto / treble
  - hit
inputs:
  - pitch
  - envelope
  - b/a/t
  - bash
  - lpf
  - saw mod
  - deep
  - smash
  - trig
  - s / l / m
outputs:
  - envelope out
  - out
up:
  - "[[Eurorack module]]"
  - "[[Eurorack voice]]"
  - "[[Voltage controlled oscillator (VCO)]]"
  - "[[Alia platform]]"
---
# Concept

Manis Iteritas is revived on [[Noise Engineering]]’s [[Alia platform]] and sounds just as hard as its predecessor.

Like [[Noise Engineering]]’s Versio ([[Versio platform]]) and Legio ([[Legio platform]]) modules, the Alia series is a modular platform ([[Alia platform]]). The point is variety, thanks to interchangeable firmware and thus interchangeable sound. All you have to do is connect your module to your computer via USB cable to switch between different [[Firmware]]s for free. There are of course panels and overlays to make the front panel match the loaded module! Alia focuses on oscillators and immediately includes two classics from [[Noise Engineering]]’s lineup.

[[Manis Iteritas Alia (MIA)]] is the reincarnation of a well-known module ([[Eurorack module]]) from [[Noise Engineering]]. Designed for hard, harsh, metallic and industrial sounds, MIA is a complete voice ([[Voltage controlled oscillator (VCO)]], [[Eurorack voice]])!

The internal sound creation relies solely on sawtooth waves and offers plenty of parameters to bend them and make them even more jagged. Profundity adds more [[Oscillator]]s to your sound, which you can then detune. Smash is a [[Distortion]] stage and Saw Mod sounds like Hard(est) Sync or (power) PWM. The integrated lowpass filter can tone it all down if needed. The VCA ([[Voltage controlled attenuator (VCA)]]) envelope has an out of its own. The Bash pot is a bipolar attenuverter for it feeding the envelope to Filter, Profundity and Smash.

![[Pasted image 20240111125604.jpg]]

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