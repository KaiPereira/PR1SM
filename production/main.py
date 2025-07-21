# NOTE THIS SCRIPT WAS MAJORITY AI GENERATED
# The neopixel wiring took quite a long time and iterations to get clean, so I don't really have too much time anymore :(
# I need to do quite a bit of testing to get the neopixels how I like em, so I'm just leaving it like that 
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers

import supervisor

keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
keyboard.modules.append(layers)

rgb_ext = RGB(
    pixel_pin=board.D0,
    num_pixels=87,
    hue_default=0, 
    sat_default=255,
    val_default=64,
    animation_mode=0
)
keyboard.extensions.append(rgb_ext)

keyboard.keymap = [
    [
        KC.ESC,  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12,
        KC.PRNT, KC.SLCK, KC.PAUS,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
        KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.MENU, KC.RCTL
    ]
]

keyboard.keymap[0][0] = KC.TO(0) 
keyboard.keymap[0][1] = KC.RGB_TOG
keyboard.keymap[0][2] = KC.RGB_MOD
keyboard.keymap[0][3] = KC.RGB_HUI
keyboard.keymap[0][4] = KC.RGB_HUD
keyboard.keymap[0][5] = KC.RGB_SAI
keyboard.keymap[0][6] = KC.RGB_SAD
keyboard.keymap[0][7] = KC.RGB_VAI 
keyboard.keymap[0][8] = KC.RGB_VAD  

if __name__ == '__main__':
    keyboard.go()

