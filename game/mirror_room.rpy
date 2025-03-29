init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #

#

define girl_in_mirror = Character("[women_name]")
define is_first_time_touch_mirror = False

transform mirror_room_to_lobby_transform:
    rotate 200

screen mirror_room_interaction():
    vbox:
        xpos 210
        ypos 265
        imagebutton auto "mirror_%s.png" action Jump("big_mirror")

    

    vbox:
        xpos 210
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("mirror_room_to_lobby") at mirror_room_to_lobby_transform
    
screen mirror_interaction():
    vbox:
        xpos 40
        ypos 40
        imagebutton auto "back_%s.svg" action Jump("on_exit_mirror")

    vbox:
        xpos 1400
        ypos 850
        imagebutton auto "mini box_%s.png" action Jump("on_box_open")

label on_exit_mirror:
    hide screen mirror_interaction_scr
    jump on_mirror_room

label mirror_room_to_lobby:
    hide screen interact_mirror_room
    jump scene3_repeat

label big_mirror:
    hide screen interact_mirror_room
    scene mirror big with dissolve
    
    if not is_first_time_touch_mirror:
        show mini box_idle:
            xpos 1400
            ypos 850
        mc "Gương ?"
        show lilith with Dissolve(1)
        play sound "appear.mp3"
        with Shake((0, 0, 0, 0), 0.3, dist=30)
        "!!!!!!!"
        girl_in_mirror "Ngươi….đến….mắc kẹt…chết..mãi mãi………"
        mc "Hả !!!"
        hide lilith with Dissolve(1)
        mc "Cái quái gì vậy ???"
        show num7 panic with dissolve:
            xalign 0.4
            yalign 0.3
        num7 "Có lẽ là một người lâu không được giao tiếp thôi…"
        show num7 fool with dissolve
        num7 "Cơ mà ở kia có một chiếc hộp kìa !!"
        hide num7 with dissolve
        $ is_first_time_touch_mirror = True

    show screen mirror_interaction as mirror_interaction_scr
    show mini box_idle:
        xpos 1400
        ypos 850
    while True:
        pause


label on_mirror_room:
    play sound "footsteps.mp3"
    hide screen board_inspect_img
    hide screen door_open_img
    hide screen go_back_to_stair
    hide screen go_to_mirror_room
    hide screen go_to_the_fork_of_lobby
    scene mirror_room with fade
    show screen mirror_room_interaction as interact_mirror_room

    while True:
        pause