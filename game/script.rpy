define mc = Character("[player_name]", color="#00BFFF")
define anon = Character("[anon_name]", color="#FF4500")
define gender = True
define goNextScene = False
define player_name = None

init python:

    male = "Nam"
    female = "Nữ"
    anon_name = "Nặc danh"
    man_name = "Người đàn ông sau cánh cửa"
    women_name = "Người phụ nữ trong gương"

    if _preferences.language == "english":
        male = "Male"
        female = "Female"
        anon_name = "Anonymous"
        man_name = "Man behind the door"
        women_name = "Women in the mirror"
    
    gender = male


    def dismiss_callback():
        renpy.play("dialog_change.mp3")
        return True

    config.say_allow_dismiss = dismiss_callback

screen gender_selection():
    modal True  # Ngăn chặn tương tác bên ngoài màn hình này
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)

        vbox:
            text "Chọn giới tính:" size 30

            # Combo box bằng cách hiển thị danh sách lựa chọn
            textbutton "[male]" action SetVariable("gender", male)
            textbutton "[female]" action SetVariable("gender", female)

            text "Giới tính bạn chọn: [gender]"

label onPcClick:
    hide screen PC_IDLE
    scene pc desktop with Dissolve(1.0)
    play sound "mail_sound.mp3"
    pause 3.0
    scene mailbox with dissolve
    pause 1.0
    scene mail with dissolve
    pause 1.0
    anon "Chào đại thần, em đã là fan của ngài rất lâu rồi."
    anon "Vậy nên em rất muốn đại thần chơi thử game mới này."
    anon "Đường link tải game em để ở đây nhé, hi vọng sớm được thấy đại thần chơi game này trên stream!"
    anon "Yêu đại thần rất nhiều <3"

    "Sau khi đọc qua mô tả trò chơi và kiểm tra đường link an toàn, bạn đã yên tâm bấm tải game."

    mc "Có vẻ như là cái game mới nổi gần đây, nghe nói rất thú vị."
    mc "Xem lượt đánh giá cũng rất tích cực."

    mc "(Tuy rằng muốn để dành stream lần đầu cho mọi người cùng xem, 
        nhưng tự nhiên mình có chút háo hức. Chắc mình sẽ ngó qua một chút...)"

    "Sau khi thanh tải hoàn thành, bạn vô cùng phấn khích và nhanh chóng bấm vào icon game."

    hide screen PC_IDLE
    scene black with fade
    stop music fadeout 1.0
    "Màn hình tối đen, xong bỗng chốc xung quanh trở nên hỗn loạn."
    "Đầu của bạn cảm thấy choáng vô cùng."
    
    mc "****"
    
    "Trước khi hoàn toàn mất ý thức, bạn chỉ có thể kịp chửi thề một câu."
    jump scene2
    return

screen pcListener():
    vbox:
        xpos 85
        ypos -33
        imagebutton auto "pc_%s.png" action Jump("onPcClick")

label start:
    stop music fadeout 1.0
    "Sau khi nhập tên và chọn giới tính, ấn enter để bắt đầu chơi"
    $ player_name = ""
    show screen gender_selection
    $ player_name = renpy.input("Nhập tên của bạn:", default="")
    while not player_name:

        $ player_name = player_name.strip()

        if not player_name:
            $renpy.notify("Tên nhân vật không được để trống !") 
            $ player_name = renpy.input("Nhập tên của bạn:", default="")

    hide screen gender_selection
    "Chào [player_name], chào mừng bạn đến với trò chơi!"
    "Bạn đã chọn giới tính [gender]."
    play music "begin_music.mp3"
    scene bedroom with fade
    show pc:
        xpos 85
        ypos -33
    mc "(Dạo này chán quá, không biết gần đây có gì mới mẻ không. 
        Tuy rằng hôm qua stream đến nửa đêm rất mệt, nhưng mà không làm việc 
        thì tiền cũng không thể tự mọc chân chạy vào túi mình được.)"

    "Bạn chán chường vừa gục ra bàn vừa lướt diễn đàn bằng máy tính."
    "Lúc sắp ngủ gật tới nơi thì đột nhiên có thông báo từ hộp thư điện tử."
    show screen pcListener as PC_IDLE
    window hide
    while True:
        pause
    