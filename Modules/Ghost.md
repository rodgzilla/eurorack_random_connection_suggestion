---
tags:
  - modular
  - effect
  - delay
  - reverb
  - distortion
  - sidechain
  - filter
  - music
  - module
url: https://www.endorphin.es/modules/p/ghost
manufacturer: "[[Endorphin.es]]"
controls:
  - tone / gain
  - volume / drive
  - compressor
  - distortion
  - sidechain / env depth
  - cutoff cv
  - frequency
  - resonance
  - delay
  - reverb
  - repeats / tone
  - time / div
  - tail / predelay
inputs:
  - in 1
  - in 2
  - pre vca
  - post vca
  - dist cv
  - comp cv
  - sidechain trig in
  - vcf cv
  - reso cv
  - delay dry wet
  - delay time cv
  - reverb dry wet
  - delay repeat cv
  - reverb tail cv
  - clock in
  - reverb freeze
outputs:
  - envelope out
  - out 1
  - out 2
up:
  - "[[Eurorack module]]"
  - "[[Effect]]"
  - "[[Delay]]"
  - "[[Reverb]]"
  - "[[Filter]]"
  - "[[Distortion]]"
---
# Concept

Together with [[Andrew Huang]], [[Endorphin.]]es presents [[Ghost]], a creative and flexible stereo effects processor ([[Effect]], [[Reverb]], [[Distortion]], [[Filter]], [[Delay]], [[Sidechain]], [[Bit crusher]], [[Sample rate reduction]]) for Eurorack ([[Eurorack module]]).

Reverb, delay, filter and distortion are the tasty flavors of this audio-processing unit, which is able to realize many innovative effect chains in the blink of an eye due to its intuitive operation and configurability. Sonically, the entire palette from atmospheric to destructive is possible. Special treats are the sidechain-audio-ducking-envelope (available both in- and externally), with an additional intuitive one-button compressor and 8x oversampling of the distortion algorithm, all possible thanks to the latest generation ARM Cortex processor.

![[Pasted image 20240111125629.jpg]]

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
