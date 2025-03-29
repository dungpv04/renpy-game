label fork_of_lobby:
    play sound "footsteps.mp3"
    hide screen go_back_to_the_fork_of_lobby
    hide screen elevator_door
    hide screen board_inspect_img
    hide screen door_open_img
    hide screen go_back_to_stair
    hide screen go_to_doctor_room
    hide screen go_to_the_fork_of_lobby
    hide screen go_to_mirror_room
    hide screen elevatorDoor_idle
    scene hospital lobby end with fade

    show screen goBackToLobby as go_back_to_lobby
    show screen goToElevator as on_go_to_elevator
    show screen goToDoctorRoom as go_to_doctor_room
    while True:
        pause

transform rotateArrowLobby:
    rotate 210
screen goBackToLobby():
    vbox:
        xpos 750
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("on_back_to_lobby") at rotateArrowLobby

transform rotateArrowElevator:
    rotate 110
screen goToElevator():
    vbox:
        xpos 1000
        ypos 300
        imagebutton:
            auto "arrow_%s.png" action Jump("on_go_to_elevator") at rotateArrowElevator

transform rotateArrowDocRoom:
    rotate 300
screen goToDoctorRoom():
    vbox:
        xpos 530
        ypos 300
        imagebutton:
            auto "arrow_%s.png" action Jump("on_go_to_doctor_room") at rotateArrowDocRoom

screen elevatorDoor():
    vbox:
        xpos 483
        ypos 120
        imagebutton:
            auto "elevator_door_%s.png" action Jump("inside_elevator")

screen elevatorDoor_idle():
    vbox:
        xpos 483
        ypos 120
        add "elevator_door_idle.png"

transform rotateArrowBackToForkLobby:
    rotate 200

screen goBackToTheForkOfLobby():
    vbox:
        xpos 740
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("fork_of_lobby") at rotateArrowBackToForkLobby

label on_go_to_elevator:
    play sound "footsteps.mp3"
    hide screen go_back_to_lobby
    hide screen on_go_to_elevator
    hide screen go_to_doctor_room
    scene elevator entrance with fade
    show screen elevatorDoor as elevator_door
    show screen elevatorDoor_idle
    show screen goBackToTheForkOfLobby as go_back_to_the_fork_of_lobby
    while True:
        pause

label on_back_to_lobby:
    play sound "footsteps.mp3"
    hide screen go_back_to_lobby
    hide screen on_go_to_elevator
    hide screen go_to_doctor_room
    hide screen elevatorDoor_idle
    jump scene3_repeat

