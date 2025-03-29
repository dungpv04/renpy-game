define man = Character("[man_name]")
define doctor = Character("Winter")
define isBoardInspecting = False
define isFirstTimeVisit = True
define isFirstTimeApproachDoor = True
define have_key = False
define current_text = ""

label scene3:
    scene hospital lobby with fade

    if isFirstTimeVisit:
        "?"  "Này nhóc kia !!!"
        mc "??!!!"
        with Shake((0, 0, 0, 0), 0.3, dist=30)
        show num7 panic with dissolve:
            xalign 0.4
            yalign 0.3
        num7 "?????!!!!!!!!!!"
        hide num7 with dissolve

        "Không gian yên ắng bỗng chốc có người cất tiếng khiến bạn và 07 giật thót, có vẻ như giọng nói phát ra từ cánh cửa sắt đằng kia."
        $ isFirstTimeVisit = False
    show screen boardInspect as board_inspect_img
    show screen doorOpen as door_open_img
    show screen goBackToStair as go_back_to_stair
    show screen goToMirrorRoom as go_to_mirror_room
    show screen goToTheForkOfLobby as go_to_the_fork_of_lobby
    while True:
        pause

label scene3_repeat:
    play sound "footsteps.mp3"
    scene hospital lobby with fade
    show screen boardInspect as board_inspect_img
    show screen doorOpen as door_open_img
    show screen goBackToStair as go_back_to_stair
    show screen goToMirrorRoom as go_to_mirror_room
    show screen goToTheForkOfLobby as go_to_the_fork_of_lobby
    while True:
        pause

label board_inspect:
    hide screen board_inspect_img
    hide screen door_open_img
    hide screen go_back_to_stair
    hide screen go_to_mirror_room
    hide screen go_to_the_fork_of_lobby
    scene board inspect with dissolve

    show screen default_board

    show screen informPaperInspect as inform_paper_inspect zorder 2
    show screen honorPaperInspect as honor_paper_inspect zorder 1
    show screen rulePaperInspect as rule_paper_inspect zorder 0
    show screen backButton as back_btn
    window hide
    while True:
        pause    

label on_back_button:
    hide screen inform_paper_inspect
    hide screen honor_paper_inspect
    hide screen rule_paper_inspect
    hide screen back_btn
    hide screen default_board
    jump scene3_repeat

label on_inform_paper_inspect:
    $ current_text = inform_text
    show screen board_paper_content zorder 10 with dissolve
    while True:
        pause

label on_rule_paper_inspect:
    $ current_text = rules_text
    show screen board_paper_content zorder 10 with dissolve
    while True:
        pause
label on_honor_paper_inspect:
    $ current_text = honor_text
    show screen board_paper_content zorder 10 with dissolve
    while True:
        pause

label on_back_to_stair:
    play sound "footsteps.mp3"
    hide screen board_inspect_img
    hide screen door_open_img
    hide screen go_back_to_stair
    hide screen go_to_mirror_room
    hide screen go_to_the_fork_of_lobby
    jump get_to_work_repeat



screen backButton():
    vbox:
        xpos 40
        ypos 40
        imagebutton auto "back_%s.svg" action Jump("on_back_button")

screen rulePaperInspect():
    vbox:
        xpos 136
        ypos 100
        imagebutton auto "rule_paper_%s.png" action Call("on_rule_paper_inspect")

screen informPaperInspect():
    vbox:
        xpos 600
        ypos 127
        imagebutton: 
            auto "inform_paper_%s.png" action Call("on_inform_paper_inspect")
        xmaximum 500

screen honorPaperInspect():
    vbox:
        xpos 646
        ypos 55
        imagebutton: 
            auto "honor_paper_%s.png" action Call("on_honor_paper_inspect")

screen default_board():
    vbox:
        xpos 136
        ypos 100
        add "rule_paper_idle.png"

    vbox:
        xpos 600
        ypos 127
        add "inform_paper_idle.png"

    vbox:
        xpos 646
        ypos 55
        add "honor_paper_idle.png"


screen boardInspect():
    vbox:
        xpos 412
        ypos 300
        imagebutton auto "board_%s.png" action Call("board_inspect")

screen doorOpen():
    vbox:
        xpos 0
        ypos 0
        imagebutton: 
            auto "door_%s.png" action Jump("approach_door")
            xmaximum 500
            ymaximum 900

transform rotateArrow:
    rotate 210
screen goBackToStair():
    vbox:
        xpos 650
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("on_back_to_stair") at rotateArrow

transform rotateArrow2:
    rotate 90
screen goToMirrorRoom():
    vbox:
        xpos 1150
        ypos 400
        imagebutton:
            auto "arrow_%s.png" action Jump("on_mirror_room") at rotateArrow2

transform rotateArrow3:
    rotate 30
screen goToTheForkOfLobby():
    vbox:
        xpos 650
        ypos 440
        imagebutton:
            auto "arrow_%s.png" action Jump("fork_of_lobby") at rotateArrow3

label approach_door:
    if not have_key:
        hide screen board_inspect_img
        hide screen door_open_img
        hide screen go_back_to_stair
        hide screen go_to_mirror_room
        hide screen go_to_the_fork_of_lobby
        scene prison_door with fade
        if isFirstTimeApproachDoor:
            $ isFirstTimeApproachDoor = False
            "Đối diện bạn là một cánh cửa sắt như nhà giam tù nhân bị khóa, phía lỗ bên trên tối om chỉ xuất hiện một đôi mắt khiến bạn không nhìn rõ diện mạo người bên trong."
            "Khi tiếp xúc gần có thể cảm nhận mùi rất khó ngửi, có vẻ nhiều ngày rồi anh ta không tắm."

            show man eyes normal with dissolve:
                ypos 150
                xpos 710
            show man eyes laughing with dissolve
            man "Chân của anh đây sắp rụng ra rồi, nhóc có thể giúp anh lấy kim chỉ được không?"
            show man eyes normal with dissolve

            show num7 angry at left with dissolve:
                yalign 0.1
            num7 "Oa, trông ông anh này thật khả nghi, chắc chắn là có ý đồ khác!"
            hide num7 with dissolve

            mc "Sao anh không tự đi lấy đi?"

            show man eyes laughing with dissolve
            man "Cửa bị khóa rồi, anh không ra được. Nhóc giúp anh đi mà~"
            show man eyes normal with dissolve
            menu:
                "Bỏ đi":
                    jump leave_man
        else:
            show man eyes normal:
                xpos 710
                ypos 150
            show man eyes laughing with dissolve
            man "Nhóc đã tìm thấy kim chỉ chưa ?"
            show man eyes normal with dissolve
            if not have_needle:
                menu:
                    "Chưa tìm thấy":
                        jump scene3_repeat
            else:
                menu:
                    "Giao kim chỉ":
                        jump help_man

                    "Chưa tìm thấy":
                        jump scene3_repeat 

    while True:
        "..."
        pause
        

label leave_man:
    show man eyes laughing with dissolve
    man "Ấy đừng đi mà! Không phải nhóc đang muốn tìm cách vào cái phòng kia sao?"
    show man eyes normal with dissolve
    mc "Sao anh biết?"

    show man eyes laughing with dissolve
    man "Nãy giờ thấy nhóc loanh quanh đây tìm cái gì đó rồi lại nghiên cứu cánh cửa đằng kia, anh đây có chìa khóa đó~"
    show man eyes normal with dissolve

    show num7 fool at left with dissolve:
        yalign 0.1
    num7 "Hình như tôi thấy anh ta rất đáng tin đó, hay là bạn giúp người ta đi, dù sao cũng chỉ là lấy kim chỉ thôi mà."
    hide num7 with dissolve
    mc "....Thôi được rồi."
    jump scene3_repeat

label help_man:
    "Bạn tìm được kim chỉ và đưa cho người đàn ông."
    show man eyes laughing with dissolve
    man "Haha cảm ơn nhóc nhé."

    mc "Đưa chìa khóa cho tôi."
    man "Đây đây, làm gì mà nóng vội thế~"

    window hide
    play sound "man give key.mp3"
    show man_hand with dissolve:
        xpos 500
        ypos 300
    pause 2
    
    menu:
        "Lấy chìa khóa":
            scene prison_door:
                blur 20.0
            show man eyes laughing:
                xpos 710
                ypos 150
                blur 20.0
            show man_hand:
                xpos 500
                ypos 300
                blur 20.0
            show key at fly_up:
                xalign 0.5
                yalign 0.5
            pause 2


    hide man_hand
    hide key

    $ have_key = True

    scene prison_door
    show man eyes laughing:
        xpos 710
        ypos 150

    mc "Nhân tiện thì làm cách nào mà anh có chìa khóa phòng đó vậy, không phải anh bị nhốt ở đây à?"
    man "Của tên bác sĩ đó làm rơi đấy, anh định giấu đi trả thù hắn."

    mc "Ồ."
    man "Nói cho nhóc biết, hắn thật sự là một tên điên cuồng giải phẫu."
    man "Lần trước hắn đến đây mượn cơ thể anh đây để nghiên cứu, xong việc lại nhốt anh trong căn phòng này mà quên luôn."

    man "Đến lúc nhớ ra hắn còn chê anh bốc mùi không muốn đụng đến nữa, tên khốn kiếp OCD @#$#@%%^!$"

    mc "Ahaha..."
    man "Dù sao cũng cảm ơn nhóc nhé."

    jump scene3_repeat


