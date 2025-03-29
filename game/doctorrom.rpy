define item_done_count = 0
define is_firstime_enter_doc_room = True
define is_desktop_touched = False
default show_paper = True
default show_jar = True
default show_book = True
default show_desktop = True
default show_door = True
define player_title = "cậu"

init python:
    def item_dragged(drags, drop):
        if not drop:
            if drags[0].drag_name == "papers":
                drags[0].snap(80,550, 0.5)
            elif drags[0].drag_name == "jars":
                drags[0].snap(830,645, 0.5)
            elif drags[0].drag_name == "books":
                drags[0].snap(950,680, 0.5)
            return

        if drags[0].drag_name == "papers": 
            if drop.drag_name == "papers":
                items_group.remove(paper_drag)
                items_group.add(paper_done)
                store.item_done_count+=1
                store.show_paper = False
                if item_done_count == 3:
                    return True
            else:
                drags[0].snap(80,550, 0.5)
                
        if drags[0].drag_name == "jars":
            if drop.drag_name == "jars":
                items_group.remove(jar_drag)
                items_group.add(jar_done)
                store.item_done_count+=1
                store.show_jar = False
                if item_done_count == 3:
                    return True
            else:
                drags[0].snap(830,645, 0.5)

        if drags[0].drag_name == "books":
            if drop.drag_name == "books":
                items_group.remove(book_drag)
                items_group.add(book_done)
                store.item_done_count+=1
                store.show_book = False
                if item_done_count == 3:
                    return True
            else:
                drags[0].snap(950,680, 0.5)


screen doctorDesktop():
    vbox:
        xpos -50
        ypos 510
        imagebutton:
            auto "doctor room desktop_%s.png" action Jump("on_desktop")

screen doctorDoor():
    vbox:
        xpos 450
        ypos 162
        imagebutton:
            auto "doctor room door_%s.png" action Jump("on_door")

screen items:
    add items_group

label on_door:
    hide screen doctor_desktop
    hide screen doctor_door
    hide screen exit_doc_room

    "Có vẻ như cửa đã bị khóa từ bên trong...."
    mc "Không thấy rồi, có vẻ như anh ta không để nó trong phòng."
    num7 "Vậy chúng ta đổi chỗ khác tìm thôi."
    show screen go_outside_doc_room as exit_doc_room

    hide screen paper_screen
    hide screen jar_screen
    hide screen book_screen
    hide screen doctor_door

    if item_done_count < 3:
        call screen items
    if item_done_count == 3:
        show screen tidy_pos_items as tidy_items

    while True:
        pause

label on_desktop:
    hide screen doctor_desktop
    hide screen doctor_door
    hide screen exit_doc_room

    "..."
    "Thẻ không có ở đây ...."
    $ is_desktop_touched = True
    hide screen items_default
    show screen doctorDoor as doctor_door
    show screen go_outside_doc_room as exit_doc_room
    hide screen doctor_desktop

    while True:
        pause

screen default_furniture():

    vbox:
        xpos -50
        ypos 510
        image "doctor room desktop_idle.png"

    
    vbox:
        xpos 450
        ypos 162
        image "doctor room door_idle.png"


screen tidy_pos_items():
    # VBox cho "papers on wall"
    vbox:
        xpos 0
        ypos 60
        image "papers on wall.png"

    # VBox cho "book on shell"
    vbox:
        xpos 1585
        ypos 50
        image "book on shell.png"

    # VBox cho "doctor jar_completed"
    vbox:
        xpos 1400
        ypos 260
        image "doctor jar_completed.png"

# Hiển thị màn hình chứa các VBox

transform go_back_to_the_fork_of_lobby_transform:
    rotate 200
screen go_outside_doc_room():
    vbox:
        xpos 570
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("on_exit_doc_room") at go_back_to_the_fork_of_lobby_transform


label on_exit_doc_room:
    hide screen exit_doc_room
    if show_book:
        show screen book_screen
    else:
        show screen book_done_screen

    if show_paper:
        show screen paper_screen
    else:
        show screen paper_done_screen

    if show_jar:
        show screen jar_screen
    else:
        show screen jar_done_screen

    hide screen default_furniture
    hide screen tidy_items
    hide screen doctor_desktop
    hide screen doctor_door

    hide screen book_done_screen
    hide screen jar_done_screen
    hide screen paper_done_screen

    hide screen book_screen
    hide screen jar_screen
    hide screen paper_screen

    jump encounter_doctor

screen winter_hand_sugery_scr():
    vbox:
        xalign 1.0
        yalign 0
        add "winter_hand_sugery"

screen ending_1():
    text "Ending 1/??: Kiệt tác hoàn hảo" color "#ff0000" size 50 xalign 0.5 yalign 0.5

label encounter_doctor:
    hide screen book_done_screen
    hide screen jar_done_screen
    hide screen paper_done_screen
    scene docroom ceil with fade
    show winter look down at right
    play sound "appear.mp3"
    with Shake((0, 0, 0, 0), 0.3, dist=30)
    pause 1.0
    show winter smile at right

    if gender == "Nam" or gender == "Male":
        $ player_title = "cậu"
    else:
        $ player_title = "cô"

    "?" "Ồ, xem ta bắt được con chuột nhắt nào đó này."
    show winter_hand at right with dissolve
    if item_done_count ==3:
        "Ngay khi bàn tay anh ta chuẩn bị nắm cổ bạn thì đột nhiên dừng lại."
        pause 1.0
        show winter look up with dissolve
        pause 1.0
        show winter suprise with dissolve
        "?" "[player_title]... đã làm điều này? Hmm... Không ngờ [player_title] có mắt thẩm mỹ đấy."
        "Anh ta bước chậm quanh căn phòng, ánh mắt lướt qua từng chi tiết đã được sắp xếp lại. Cuối cùng, anh quay lại nhìn bạn, nụ cười không còn đáng sợ như trước."
        pause 1.0
        show winter smile with dissolve
        hide winter_hand with dissolve
        "?" "Ta rất muốn xem bên trong [player_title] như thế nào... Nhưng có lẽ... hôm nay ta sẽ tha cho [player_title]. Coi như... cảm ơn vì sự giúp đỡ."
        doctor "Ta là Winter, bác sĩ Giải phẫu học."
        hide winter with dissolve
        show num7 panic with dissolve:
            xalign 0.4
            yalign 0.3
        num7 "Hú hồn, lúc nãy anh ta định bóp cổ bạn đấy."

        mc "Tôi cũng thấy rồi, cảm giác như vừa trở về từ cõi chết."
        jump negotiation_with_winter
    else:
        "Chưa kịp để bạn phản ứng, bàn tay to lớn túm chặt lấy cổ bạn khiến bạn dần mất đi ý thức."
        scene black with fade
        "Trong cơn mơ màng, bạn cảm thấy hắn muốn mang bạn đi đâu đó. Tiếng cười trầm thấp quỷ dị khiến bạn sởn gai ốc, nhưng không thể kháng cự."
        window auto
        scene doctor room sugery with Fade(0.5, 2.0, 0.5):
            blur 20
        "Không biết qua bao lâu, bạn dần dần tỉnh lại. Ánh đèn từ trần nhà rọi thẳng vào mặt khiến bạn khó chịu, cả chân tay cũng bị chói chặt không thể cử động"
        scene doctor room sugery with Fade(0.5, 1.0, 0.5):
            blur 6
        scene mc hand with Fade(0.5, 0.5, 0.5):
            blur 10
        scene mc hand with Fade(0.5, 0.5, 0.5)

        "?" "Hm, ngươi tỉnh rồi?"
        scene doctor room sugery with Dissolve(1.0)
        show winter sugery at right with dissolve
        pause 1.0
        "?" "Sẽ hơi khó khăn đây, nhưng không sao."
        show screen winter_hand_sugery_scr with dissolve 
        "?" "Rất nhanh thôi ngươi sẽ trở thành một trong những kiệt tác xinh đẹp trong bộ sưu tập của ta~"
        hide screen winter_hand_sugery_scr
        window hide
        show black with Fade(1.0, 1.0, 1.0)
        show screen ending_1 with fade
        pause 2.0
        hide screen ending_1 with fade
        $ renpy.full_restart()

label negotiation_with_winter:
    hide num7 with dissolve
    show winter look down at right with dissolve
    mc "Tôi là [player_name]"
    mc "Xin lỗi vì tự ý vào phòng của anh, nhưng tôi thật sự cần thẻ nhân viên của anh để sử dụng thang máy. Anh có thể cho tôi mượn được không?"

    show winter smile with dissolve
    doctor "Lúc nãy nể tình [player_title] giúp ta dọn dẹp phòng nên ta đã tha cho [player_title] một mạng rồi."
    doctor "Giờ muốn nhờ vả ta, [player_title] có định sẽ trả một cái giá khác không?"
    show winter look down with dissolve
    menu:
        "...Tôi xin lỗi":
            mc "...Tôi xin lỗi."
            jump physical_test
        "A-Anh muốn làm gì!!?":
            mc "A-Anh muốn làm gì!!?"
            jump physical_test

label physical_test:
    show winter smile with dissolve
    doctor "Chỉ là nghiên cứu ngoài da thôi."
    show black with fade
    "Sau khi bị ép làm vài phương pháp vật lí và bị Winter sờ nắn các khớp xương, cuối cùng anh ta cũng chịu quẹt thẻ cho bạn dùng thang máy."
    hide black with fade
    doctor "Chào nhé, lần sau gặp lại hãy để ta được sử dụng dao trên cơ thể [player_title]."
    mc "...Tôi không thèm hi vọng gặp lại anh đâu!"
    $ have_card = True
    jump on_go_to_doctor_room

screen back_to_fork_of_lobby():
    vbox:
        xpos 570
        ypos 700
        imagebutton:
            auto "arrow_%s.png" action Jump("back_to_fork_of_lobby_label") at go_back_to_the_fork_of_lobby_transform

screen docroom_entrance():
    vbox:
        xpos 540
        ypos 170
        imagebutton:
            auto "docroom entrance_%s.png" action Jump("entry_docroom")

screen docroom_entrance_idle():
    vbox:
        xpos 540
        ypos 170
        add "docroom entrance_idle.png"

screen door_lock():
    vbox:
        xpos 450
        ypos 130
        imagebutton:
            auto "docroom_door_lock_%s.png" action Jump("unlock_door")

label unlock_door:
    hide screen door_lock
    show docroom_door_lock_idle:
        xpos 450
        ypos 130
    "Cần có chìa khóa để mở"
    if have_key:
        menu:
            "Quay lại":
                jump on_go_to_doctor_room

            "Sử dụng chìa khóa":
                hide docroom_door_lock_idle
                play sound "confirm_button_click.mp3"
                show docroom_door_unlock with dissolve:
                    xpos 450
                    ypos 130
                pause 2
                jump on_enter_doctor_room
    else:
        menu:
            "Quay lại":
                jump on_go_to_doctor_room
    while True:
        pause

label entry_docroom:
    if is_firstime_enter_doc_room:
        hide screen back_to_fork_of_lobby
        hide screen docroom_entrance
        scene docroom entrance zoom in with dissolve
        show screen door_lock
    else:
        hide screen back_to_fork_of_lobby
        hide screen docroom_entrance
        show screen docroom_entrance_idle
        "..."
        show screen back_to_fork_of_lobby
        show screen docroom_entrance
        hide screen docroom_entrance_idle
    while True:
        pause

label back_to_fork_of_lobby_label:
    hide screen back_to_fork_of_lobby
    hide screen docroom_entrance
    jump fork_of_lobby

label on_go_to_doctor_room:
    play sound "footsteps.mp3"
    hide screen go_back_to_lobby
    hide screen on_go_to_elevator
    hide screen go_to_doctor_room
    scene doctor_room_entry with fade
    show screen back_to_fork_of_lobby
    show screen docroom_entrance
    while True:
        pause



label on_enter_doctor_room:
    scene doctor room with Fade(1, 1, 1)
    show screen default_furniture

    show screen paper_screen
    show screen jar_screen
    show screen book_screen

    if is_firstime_enter_doc_room:
        "Phòng làm việc của bác sĩ nằm ở một góc khuất trên tầng, không gian u tối và đầy rẫy dụng cụ y khoa. Cửa phòng mở ra, đập vào mặt bạn là một căn phòng bừa bộn với tài liệu và đồ đạc vương vãi."
        num7 "Bừa thật đấy, thế mà ban nãy gã kia nói anh ta bị OCD làm tôi cứ tưởng..."
        mc "Tìm đồ đã rồi tính sau."
        $ is_firstime_enter_doc_room = False

    show screen doctorDesktop as doctor_desktop zorder 0
    show screen go_outside_doc_room as exit_doc_room
    
    
    while True:
        pause
define paper_drag = Drag(d="doctor room paper_idle.png", drag_name="papers", idle_child="doctor room paper_idle.png", hover_child="doctor room paper_hover.png", dragged=item_dragged, xpos=80,ypos=550)
define jar_drag = Drag(d="doctor jar_idle.png", drag_name="jars", xpos=830, ypos=645, idle_child="doctor jar_idle.png", hover_child="doctor jar_hover.png", dragged=item_dragged)
define book_drag = Drag(d="book_idle.png", drag_name="books", xpos=950, ypos=680, idle_child="book_idle.png", hover_child="book_hover.png", dragged=item_dragged)
define paper_drop = Drag(d=Solid("#00000000", xysize=(250, 150)),drag_name="papers",xpos=0,ypos=60,draggable=False)
define jar_drop = Drag(d=Solid("#00000000", xysize=(150, 250)),drag_name="jars",xpos=1400,ypos=260,draggable=False)
define book_drop = Drag(d=Solid("#00000000", xysize=(350, 800)),drag_name="books",xpos=1585,ypos=50,draggable=False)
define items_group = DragGroup(paper_drag, jar_drag, book_drag, paper_drop, jar_drop, book_drop)

define paper_done = Drag(d="papers on wall.png",drag_name="papers",xpos=0,ypos=60,draggable=False,idle_child="papers on wall.png")
define jar_done = Drag(d="doctor jar_completed.png",drag_name="jars",xpos=1400,ypos=260,draggable=False,idle_child="doctor jar_completed.png")
define book_done = Drag(d="book on shell.png",drag_name="books",xpos=1585,ypos=50,draggable=False,idle_child="book on shell.png")


screen paper_screen():
    vbox:
        xpos 80
        ypos 550
        image "doctor room paper_idle.png"

screen jar_screen():
    vbox:
        xpos 830
        ypos 645
        image "doctor jar_idle.png"

screen book_screen():
    vbox:
        xpos 950
        ypos 680
        image "book_idle.png"

screen paper_done_screen():
    vbox:
        xpos 0
        ypos 60
        image "papers on wall.png"

screen jar_done_screen():
    vbox:
        xpos 1400
        ypos 260
        image "doctor jar_completed.png"

screen book_done_screen():
    vbox:
        xpos 1585
        ypos 50
        image "book on shell.png"
