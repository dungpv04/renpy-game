define have_needle = False
transform fly_up:
    yoffset 500
    easein 1.0 yoffset 0

label on_box_open:
    if not have_needle:
        hide screen mirror_interaction_scr
        scene mirror big:
            blur 20.0
        show box
        call screen code_lock()
        show needle at fly_up:
            yalign 0.5
            xalign 0.5
        $ have_needle = True
        hide box
        call screen skip_click
    else:
        "..."
    while True:
        pause
    

# Màn hình nhập mật mã


screen translucent_bg:
    frame:
        background "#00000080"

screen skip_click():
    key "mouseup_1" action Jump("hide_box_item")

label hide_box_item:
    jump big_mirror

screen code_lock():
    default code = [0, 0, 0, 0]  # Mật khẩu mặc định

    vbox:
        xpos 40
        ypos 40
        imagebutton auto "back_%s.svg" action Jump("big_mirror")

    frame:
        padding (20, 20)
        background "#00000000"

        hbox:
            spacing 2
            xpos 620
            ypos 473
            # Hiển thị 4 ô số
            for i in range(4):
                frame:
                    background "#838f9a"
                    xsize 169 
                    ysize 124
                    xpadding 0.3
                    hbox:
                        textbutton str(code[i]) text_text_align 0.5 text_color "#000000" text_size 80 action [Play("sound", "box_number_click.mp3"), SetDict(code, i, (code[i] + 1) % 10)]

            # Nút xác nhận
        vbox:
            xalign 0.5 
            yalign 0.65
            imagebutton auto "box_confirm_button_%s.png" action Function(check_code, code)

        

# Xác định mật khẩu đúng
define correct_code = [1, 9, 8, 0]  # Mật khẩu: 1980

# Kiểm tra mật khẩu
init python:
    def check_code(code):
        renpy.play("confirm_button_click.mp3")  # Âm thanh đúng
        if code == correct_code:
            return True
        else:
            renpy.notify("Sai mật khẩu! Hãy thử lại.")

# Cảnh mở hộp khi nhập đúng mật khẩu