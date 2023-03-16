def on_forever():
    basic.show_leds("""
        # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                . . # . .
                . . # . .
                . . # . .
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    basic.pause(10)
    basic.show_leds("""
        # # # # #
                . . # . .
                . . # . .
                . . # . .
                # # # # #
    """)
    basic.pause(10)
    basic.show_icon(IconNames.HEART)
    basic.pause(10)
    basic.show_string("" + str((input.temperature())))
    music.play_melody("- - - - - - - - ", 120)
basic.forever(on_forever)
