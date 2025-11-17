---
tags:
  - modular
  - music
  - module
url: https://intellijel.com/shop/eurorack/mixup/
manufacturer: "[[Intellijel]]"
controls:
  - level 1
  - level 2
  - level 3
  - mute 1
  - mute 2
  - mute 3
inputs:
  - in 1
  - in 2
  - in 3L
  - in 3R
  - in 4L
  - in 4R
outputs:
  - mix L
  - mix R
up:
  - "[[Eurorack module]]"
  - "[[Mixer]]"
---
# Concept

[[Mixup (eurorack)]] makes is easy to combine your mono and stereo sources into a single stereo mix. You have mute and level control over the first three channels and, using a rear connector, you can chain multiple Mixups together into a hidden 5th stereo channel without using up channels on the front panel.

![[Pasted image 20240623234854.jpg]]
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
