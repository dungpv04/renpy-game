define have_card = False

screen elevator_panel():
    vbox:
        xpos 1230
        ypos 400
        imagebutton auto "elevator panel_%s.png" action Jump("on_elevator_panel")

screen elevator_panel_idle():
    vbox:
        xpos 1230
        ypos 400
        add "elevator panel_idle"

screen elevator_inside_door():
    vbox:
        xpos 380
        ypos 68
        imagebutton auto "elevator door inside_%s.png" action Jump("exit_elevator")

screen elevator_num():
    vbox:
        xalign 0.698
        yalign 0.305
        add "elevator floor num"


screen elevator_arrow():
    vbox:
        xalign 0.698
        yalign 0.26
        add "elevator arrow up"

screen ending_demo():
    text "End demo" color "#ff0000" size 50 xalign 0.5 yalign 0.5

label exit_elevator:
    play sound "elevator open - close.mp3"
    hide screen elevator_inside_door
    hide screen elevator_panel
    show screen elevator_panel_idle
    pause 3.0
    hide screen elevator_num
    hide screen elevator_panel_idle
    jump on_go_to_elevator
    while True:
        pause

label on_elevator_panel:
    play sound "elevator button.mp3"
    hide screen elevator_panel
    hide screen elevator_inside_door
    show screen elevator_panel_idle
    if not have_card:
        "..."
        show num7 uwu with dissolve:
            xalign 0.3
            yalign 0.4
        num7 "Có vẻ thang máy cần thứ gì đó để hoạt động, như thẻ nhân viên chẳng hạn."
        num7 "Chúng ta đi tìm thôi."
        hide num7 with dissolve
    
        show screen elevator_panel zorder 1
        show screen elevator_inside_door
        hide screen elevator_panel_idle
    else:
        play sound "elevator working.mp3"
        hide screen elevator_panel
        show screen elevator_panel_idle
        hide screen elevator_inside_door
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_arrow with dissolve
        show screen elevator_arrow with dissolve
        hide screen elevator_num with dissolve
        hide screen elevator_arrow with dissolve
        hide screen elevator_panel_idle
        stop sound fadeout 4.0
        show black with Fade(1.0, 0.5, 1.0)
        jump ending_elevator
    while True:
        pause
    

label ending_elevator:
    show screen ending_demo with fade
    pause 3.0
    hide screen ending_demo with fade
    $ renpy.full_restart()

label inside_elevator:
    play sound "elevator open - close.mp3"
    hide screen elevatorDoor
    hide screen go_back_to_the_fork_of_lobby
    pause 3.0
    hide screen elevatorDoor_idle
    scene elevator inside with fade
    show screen elevator_panel zorder 1
    show screen elevator_inside_door
    show screen elevator_num
    while True:
        pause