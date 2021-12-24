# Reaction-Test-Dueling-Theme

A program created to test your reaction time with a wild-west dueling theme.

INSTRUCTIONS:
Hover your mouse over the cylinder, do not remove it while the displayed text says "Steady..."
When it says "Draw!" move your mouse to the silhouette and click it as fast as you can.
Your reaction time in milliseconds will display to the left.

KNOWN BUGS:
The python library "playsound" does not have a function to stop playing the sound if the
procedure is interrupted.  Because of this, if you leave the cylinder too early, the tension
violin will continue playing.  This can overlap with other sounds.
