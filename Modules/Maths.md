---
tags:
  - modular
  - lfo
  - vco
  - utility
  - music
  - module
url: https://www.makenoisemusic.com/modules/maths
manufacturer: "[[Make Noise]]"
controls:
  - channel 1 cycle
  - channel 4 cycle
  - channel 1 level
  - channel 2 level
  - channel 3 level
  - channel 4 level
  - channel 1 rise
  - channel 1 fall
  - channel 1 log / exp
  - channel 4 rise
  - channel 4 fall
  - channel 4 log / exp
inputs:
  - channel 1 input
  - channel 1 trig
  - channel 2 input
  - channel 3 input
  - channel 4 trig
  - channel 4 input
  - channel 1 rise
  - channel 4 rise
  - channel 1 both
  - channel 4 both
  - channel 1 fall
  - channel 4 fall
  - channel 1 cycle
  - channel 4 cycle
outputs:
  - channel 1 output
  - channel 2 output
  - channel 3 output
  - channel 4 output
  - channel 1 end of rise
  - channel 1 normalized output
  - or
  - sum
  - inv
  - channel 4 normalized output
  - channel 4 end of cycle
up:
  - "[[Eurorack module]]"
  - "[[Clock]]"
  - "[[Low frequency oscillator (LFO)]]"
  - "[[Voltage controlled oscillator (VCO)]]"
---
# Concept

[[Maths]] builds on the tradition set into motion in the 1960’s when [[Don Buchla]] adapted circuits found within analog computers for musical purposes. Buchla’s Algebraic Processor, Model 257 and 281 changed the way music synthesizers utilize control voltages. [[Maths]] ([[Eurorack module]]) continues this great tradition of sculpting the control signals we use to sculpt our sound signals

- Scale, invert, amplify or integrate an incoming signal ([[Attenuator]])
- Perform addition, subtraction and analog logic OR manipulations ([[Logic]])
- With no signal applied, generate a variety of linear, logarithmic, or exponential functions ([[Function generator]])
- Functions as short as 2ms and as long as 25 minutes per cycle!
- Triggered Functions (envelope) ([[Envelope]])
- Continuous Functions (LFO) ([[Low frequency oscillator (LFO)]])
- LED indicates the activity on associated channel
- End of Rise and End of Cycle Pulses facilitate programming of more complex functions ([[Clock]])
- All outputs capable of driving a passive 4 way mult without loading effects (no buffered mult needed here)
- Perfect for modulating the DPO and just about anything else

![[Pasted image 20240111125540.jpg]]

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
