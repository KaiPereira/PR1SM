# PR1SM - Stacked Acrylic Keyboard

PR1SM is a minimalistic, stacked acrylic keyboard with neopixel backlight, running on KMK. It's built on a cheap, compact 2 layer PCB and has a fully fledged TKL (tenkeyless) layout.

![Pasted image 20250718024216.png](journal/Pasted%20image%2020250718024216.png)

## Custom Features
- Fully laser cut stacked case that will leak the RGB colors
- Full sized TKL (tenkeyless) layout with a function row
- Complete RGBA backlight on every single key with a power neopixel
- Decoupling caps, and stabilizing resistors for smooth power
- Simply runs off of a Raspberry Pi Pico
- Exposed black silkscreen design on a white PCB

## CAD Design

I used Onshape to design my keyboard like all of my projects. It was a bit tricky, because everything needed to be stock size and was going to be laser cut, so I couldn't have like partially cut in designs that a 3D printer could accomplish.

Anyways the entire case is just held together using M3 screws and it's all stacked so it should be decently rigid. The acrylic will let all the colors through, and it'll look sick.

![Pasted image 20250718023041.png](journal/Pasted%20image%2020250718023041.png)
![Pasted image 20250718023104.png](journal/Pasted%20image%2020250718023104.png)

*The silkscreen is actually black as shown in the render*

The case is separated into 5 separate laser cut pieces, respectively 3 - 3.5mm, 1 - 1.5mm and 1 - 5mm plate so it's relatively thin and pretty easy to assemble. [Onshape Link](https://cad.onshape.com/documents/8b572caa0e2769c057d91df7/w/f3c5c8a5f25f2593dceb7e8f/e/dc4500617840d95f6da4efee?renderMode=0&leftPanel=false&uiState=687a14d121cd8749fec3b29b)

## PCB Design

I designed the entire PCB in KiCad. I tried to stick to all best practices and the neopixels have decoupling and a resistor to smooth voltage. The keys are just a simple key matrix, and the MCU is a Pi Pico. I used the KiCad image converter to do the images, and some of them are drawn by me, others are AI generated and then there's some taken from the internet.

![Pasted image 20250718023504.png](journal/Pasted%20image%2020250718023504.png)

Now the PCB is a bit interesting, because it uses a ground fill on the bottom, and then a power fill on the top, the back lines run horizontally, while the front traces run vertically. Via's are on all the neopixel power lines for the fill with the decoupling caps right beside them.

![Pasted image 20250718023624.png](journal/Pasted%20image%2020250718023624.png)

Some 3D photo's:

![Pasted image 20250720013311.png](journal/Pasted%20image%2020250720013311.png)
![Pasted image 20250720013340.png](journal/Pasted%20image%2020250720013340.png)
## Firmware

PR1SM uses KMK firmware which is written in Python. I programmed all the keys in a matrix and then the backlit neopixels are just running in a wave pattern.

## Bill of Materials (BOM)
Here's everything you'll need to build your own PR1SM keyboard:
- 89x Cherry MX Switches
- 89x Keycaps for a TKL keyboard
- 90x SK6812 Mini-E LED's
- 1x Raspberry Pi Pico
- 3x 3.5mm thick acrylic panels
- 1x 5mm thick acrylic panel
- 1x 1.5mm thick acrylic panel
- 10x Low profile M3 bolts/nuts

Here's the link to the spreadsheet: https://docs.google.com/spreadsheets/d/1PX1jr134__XBLFXCxBkakxo4KN2pxjdmwIgQ4_i7XN4/edit?usp=sharing

![Pasted image 20250720012424.png](journal/Pasted%20image%2020250720012424.png)

## Credits & Help

Thanks to @cheyao and the KiCad discord server for helping me with the wiring and the decoupling caps. @alcovesofastridpark on reddit for the main inspiration for the stacked acrylic and backlight. And of course @qcoral and @acornitum for starting Highway, the program funding this keyboard.
