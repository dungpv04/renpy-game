init:
    # Làm mờ hình nề

    # Hiệu ứng chớp mắt chậm (màn hình đen xuất hiện chậm dần)
    transform slow_blink:
        alpha 1
        pause 0.8
        linear 0.8 alpha 0
        pause 0.5
        linear 1.2 alpha 1
        pause 1
        linear 0.8 alpha 0
        pause 0.5
        linear 1.2 alpha 1

    # Background trôi nổi như mất phương hướng
    transform floating:
        xoffset -5 yoffset -5
        ease 1.5 xoffset 5 yoffset 5
        ease 1.5 xoffset -5 yoffset -5
        repeat 5

init python:
    die_text = "Đã chết."
    if _preferences.language == "english":
        die_text = "You died."

screen start_door_scr():
    vbox:
        xpos 625
        ypos 380
        imagebutton auto "start door_%s.png" action Jump("exit_start_room")

label exit_start_room:
    hide screen start_door_scr
    play sound "footsteps.mp3"
    scene hospital stairway with fade
    show num7 uwu with dissolve:
        yalign 0.3
        xalign 0.4
    num7 "Oaaa, có tận 2 đường luôn này!"
    num7 "Tầng này có vẻ khá đáng sợ đấy, nhỉ? Cơ mà dưới cầu thang cũng rất tối nha~!"
    num7 "Bạn muốn đi đâu? Khám phá tầng này hay đi xuống cầu thang?"
    num7 "Vì tôi là một hệ thống đáng yêu và tận tâm nên tôi ủng hộ bất kỳ lựa chọn nào của bạn!"
    hide num7 with dissolve
    show screen goToLobbyListener as go_to_lobby_arrow with dissolve
    show screen goToStairwayListener as go_to_stairway_arrow
    while True:
        pause

define num7 = Character("07", color="#3bfb01")

transform rotate_image:
    rotate 120

label get_to_work:
    mc "{i}HAHA DẬY LÀM VIỆC NÀO!!!{/i}"
    show num7 uwu with dissolve
    num7 "Rất tốt, 07 vô cùng hân hạnh khi được phục vụ kí chủ~"
    "Bạn đứng dậy rời khỏi giường, mang tâm trạng thấp thỏm đi theo chỉ dẫn của hệ thống."
    scene start_room with fade
    show screen start_door_scr
    while True:
        pause
    
label get_to_work_repeat:
    scene hospital stairway with fade
    show screen goToLobbyListener as go_to_lobby_arrow with dissolve
    show screen goToStairwayListener as go_to_stairway_arrow 
    window hide
    while True:
        pause

label go_to_lobby:
    play sound "footsteps.mp3"
    hide screen go_to_lobby_arrow
    hide screen go_to_stairway_arrow
    jump scene3
    
label go_to_stairway:
    "Coming soon..."
    while True:
        pause
screen goToLobbyListener():
    vbox:
        xpos 250
        ypos 600
        imagebutton auto "arrow_%s.png" action Jump("go_to_lobby")

screen goToStairwayListener():
    vbox:
        xpos 1200
        ypos 400
        imagebutton auto "arrow_%s.png" action Jump("go_to_stairway") at rotate_image

image blink_anim:
    Solid("#000")
    alpha 0
    linear 0.1 alpha 1
    pause 1.0
    linear 0.1 alpha 0

transform ship_sway:
    ypos -10 #You'll have to play around with these values and see what works for the images you've got and the effect you want.
    linear 0.5 ypos -15
    linear 0.5 ypos -10
    repeat #This is what makes it loop

label give_up:
    show num7 angry with dissolve
    num7 "Tốt thôi, tôi sẽ không quan tâm bạn nữa."
    hide num7 with dissolve
    "Một lúc sau, xung quanh lại trở nên yên ắng, có lẽ 07 đã rời đi thật rồi."
    "Bạn đã tự an ủi mình rằng đây chỉ là giấc mơ thôi và dần dần chìm vào giấc ngủ."
    show black with fade
    "Chỉ cần ngủ một giấc, và khi thức dậy mọi thứ sẽ trở về lúc ban đầu."
    hide black with fade
    "Nhưng dần dần bạn cảm thấy rất khó thở."
    show blink_anim
    """Bạn muốn vùng vẫy để thoát ra nhưng không tài nào cử động được.
    Đến cả việc mở mắt cũng rất khó khăn, dường như có thứ gì đó đang đè nặng và bóp chặt cơ thể bạn.
    Từng giây trôi qua, bạn cảm giác được sự sống đang dần bị rút cạn."""
   
    scene ceil at floating with fade:
        blur 10
    show black:
        alpha 0.25
    show blink_anim
    pause 1
    scene ceil at floating with fade:
        blur 20
    show black:
        alpha 0.5
    show blink_anim
    pause 1
    scene ceil at floating with fade:
        blur 40
    show black:
        alpha 1
    show blink_anim
    pause 1
    mc "Đây... chắc chắn là nhân vật phụ sống không quá ba dòng trong tiểu thuyết..."

    if gender == "Nam" or gender == "Male":
        mc "Bố mẹ......Chị ơi...Con..xin lỗi...."
    else:
        mc "Bố mẹ......Em trai...Con..xin lỗi...."
    
    show screen game_over_text with fade
    pause 3
    hide screen game_over_text
    jump scene2_respawn
    
    while True:
        pause


screen game_over_text():
    text "[die_text]" color "#ff0000" size 50 xalign 0.5 yalign 0.5

label scene2_respawn:
    scene ceil with fade
    show num7 fool:
        yalign 0.3
        xalign 0.4
    menu:
        "HAHA DẬY LÀM VIỆC NÀO !!!":
            jump get_to_work


        "Tôi cóc quan tâm !!!":
            jump give_up

label scene2:

    "Không biết bạn đã bất tỉnh bao lâu..."
    scene ceil with fade
    play music "shadow_in_the_mist.mp3" loop
    "Khi tỉnh lại đập vào mắt bạn là một căn phòng xa lạ, dường như là một bệnh viện bỏ hoang từ rất lâu rồi..."
    "Xung quanh tĩnh lặng đến quỷ dị, bạn dường như rùng mình bởi mùi ẩm mốc và thoang thoảng mùi hoại tử vấn vương trong không khí..."
    play sound "rat_sound.mp3"
    "Ánh đèn chập chờn và tiếng những con chuột cống kêu lên lúc xa lúc gần khiến bạn bất an vô cùng..."

    mc "Chuyện quái gì vậy, đây là đâu?"
    mc "Mình... Xuyên không rồi sao???"
    mc "Không không không không không, thế thì ảo ma quá rồi!"
    mc "Chắc ai đó đã đột nhập vào nhà và bắt cóc mình, rồi thực hiện chương trình thử thách lòng gan dạ!"

    mc "Đúng đúng! Chắc chắn là như vậy, haha..."
    mc "..."

    play sound "beep beep.mp3"
    "Tit tit tit"
    
    "?" "Đang tải dữ liệu..."

    stop sound
    mc "!!!!!!!!!!AAAAAAAAAAAAA"

    "Khi không gian đang tĩnh lặng đến mức có thể nghe thấy tiếng kim rơi, bỗng nhiên có một âm thanh điện tử máy móc vang lên khiến bạn sợ đến mức hét toáng lên."

    "?" "Update phiên bản thành công."
    show num7 uwu with dissolve:
        yalign 0.3
        xalign 0.4
    "?" "Xin chào kí chủ, tôi là Hệ Thống mang số hiệu 07. Vô cùng hân hạnh được đồng hành cùng bạn~"

    mc "..."
    mc "Đây là flycam công nghệ mới hả?"
    mc "Trời ơi mình chưa từng thấy cái này bao giờ luôn, hiện đại thật đó."
    mc "Mà này, camera ở đâu vậy? Tuy tôi chỉ là một streamer nhỏ bé, nhưng thuê tôi tham gia quay chương trình thử thách cũng phải trả tiền phí hình ảnh và cachet đầy đủ cho tôi đấy nhé!"

    num7 "..."

    mc "Các bạn định bắt tôi đi làm không công sao, không được đâu! Tôi không thể hít khí trời uống nước lã mà sống được! Các người có còn lương tâm không vậy?!!"

    num7 "Tôi--"

    mc "Được được được, tôi sẽ giảm 10%% cho các cậu. Haizzz, số tôi khổ quá đi mà!"

    show num7 panic with dissolve
    num7 "Không..."

    mc "ĐỪNG MÀ! Thôi được rồi, chỉ cần một nửa so với giá thị trường là được!! Không thể ít hơn được nữa!!!"

    show num7 angry with dissolve
    with Shake((0, 0, 0, 0), 0.3, dist=30)
    num7 "AAAAAAAAAAAAAAAAAA"
    num7 "BẠN CÓ THÔI NGAY KHÔNG HẢ!!! CÁI THÓI XẤU THÍCH NHẢY VÀO MIỆNG KHÔNG ĐỂ NGƯỜI TA NÓI HẾT CÂU NÀY LÀ DI TRUYỀN TỪ AI VẬY?????"

    mc "...Xin lỗi..."

    num7 "Hứ!!"
    num7 "Thứ nhất, đây không phải phim trường, cũng không phải đang quay chương trình thử thách hay troll gì đó đâu."
    with Shake((0, 0, 0, 0), 0.3, dist=30)
    num7 "Thứ hai, tôi không phải người keo kiệt muốn trâu đi cày mà không cho trâu ăn. Tôi nhất định sẽ không bạc đãi bạn."
    with Shake((0, 0, 0, 0), 0.3, dist=30)
    num7 "Và thứ ba, TÔI KHÔNG PHẢI FLYCAM! TÔI LÀ 07!!!!!!"
    with Shake((0, 0, 0, 0), 0.3, dist=30)

    mc "Tôi hiểu rồi, vậy bây giờ tôi phải làm gì? Đây là đâu?"

    show num7 uwu with dissolve
    num7 "Đây là thế giới trong game 'No escape' mà bạn đã chơi."

    mc "!!!!"

    num7 "Chắc bạn cũng đã nghe qua rằng đây là tựa game mới ra mắt có tích hợp tính năng AI khiến các NPC trong trò chơi có tri giác và có thể tự suy nghĩ, hành động theo ý muốn của mình đúng không?"
    num7 "Đây là một bước tiến mới trong công nghệ. Tuy nhiên, chính vì trí tuệ AI tự phát mà thế giới này đã xuất hiện một số bug khiến cho quỹ đạo thế giới dần mất kiểm soát."
    num7 "Các kết cục ban đầu và quy tắc thế giới được lập trình sẵn dần dần bị sụp đổ, dường như nó muốn tách ra làm một thế giới riêng biệt không chịu sự kiểm soát của lập trình nữa."

    mc "Oaaa..."
    mc "Oh..."
    mc "Tôi có thể về nhà không, tôi vẫn chưa ấn nút nồi cơm..."

    num7 "Không cần thiết, trước khi đưa bạn đến đây tôi đã tiện thể giúp bạn rồi."

    mc "Nhưng mà nếu tôi đi lâu như thế gia đình tôi sẽ rất lo lắ-"

    num7 "Không sao, khi bạn bước vào thế giới này thì ở bên ngoài thời gian của bạn đã được đóng băng lại rồi. Bạn có thể ở lại đây bao lâu cũng được~"

    mc "Nhưn-"

    show num7 angry with dissolve
    num7 "Không có nhưng nhị gì hết!"

    mc "...Tôi có thể ngất được không?"

    show num7 fool with dissolve
    num7 "Cũng được thôi, nhưng tôi nói trước cho bạn biết thế giới này không an toàn đâu."
    num7 "Vì đây là game kinh dị, nên có thể một lát nữa sẽ có một gã kì quặc nào đó nhảy ra muốn dùng dao giải phẫu bạn đó nha~~"
    menu:
        "HAHA DẬY LÀM VIỆC NÀO !!!":
            jump get_to_work


        "Tôi cóc quan tâm !!!":
            jump give_up

    return
