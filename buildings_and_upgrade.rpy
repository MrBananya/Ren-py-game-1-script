
# -------------------------------- экран постройки
screen build_update_screen:
    imagemap:
        idle 'game_menu_2'

        text "{size=36}{color=#ffffff}Текущие ресурсы {/color}{/size}" xpos 720 ypos 40

        add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 610 ypos 100
        text "{size=20}{color=#ffffff}: %i {/color}{/size}" %Parametrs_Num[0] xpos 660 ypos 110
        add im.Scale('icon/medical-pack-alt.webp', 45, 45) xpos 750 ypos 100
        text "{size=20}{color=#ffffff}: [Parametrs_Num[1]] {/color}{/size}" xpos 800 ypos 110
        add im.Scale('icon/half-log.webp', 45, 45) xpos 870 ypos 100
        text "{size=20}{color=#ffffff}: [Parametrs_Num[2]] {/color}{/size}" xpos 920 ypos 110
        add im.Scale('icon/oil-drum.webp', 45, 45) xpos 990 ypos 100
        text "{size=20}{color=#ffffff}: [Parametrs_Num[3]] {/color}{/size}" xpos 1040 ypos 110
        add im.Scale('icon/person.png', 45, 45) xpos 1100 ypos 100
        text "{size=20}{color=#ffffff}: [Parametrs_Num[4]] {/color}{/size}" xpos 1150 ypos 110
        add im.Scale('icon/person.png', 45, 45) xpos 1200 ypos 100
        text "{size=20}{color=#ffffff}: [Parametrs_Num[5]] {/color}{/size}" xpos 1250 ypos 110

#---------------------------------- 1 постройка - вышка

        text "{size=24}{color=#ffffff}Построить сторожевую вышку {/color}{/size}" xpos 150 ypos 250
        add im.Scale('bg/bg_school/tower_upgrade.webp', 300, 150) xpos 150 ypos 300
        text "{size=24}{color=#ffffff}Уменьшает шанс ночной атаки {/color}{/size}" xpos 150 ypos 480
        text "{size=24}{color=#ffffff} Нужно ресурсов {/color}{/size}" xpos 150 ypos 550
        text "{size=24}{color=#ffffff} Уровень постройки %s {/color}{/size}" % buildings_stage[0] xpos 150 ypos 510

        if buildings_stage[0] == buildings_stage_max[0]:
            text "{size=24}{color=#ffffff} Max lvl {/color}{/size}" xpos 200 ypos 600
        else:
            add im.Scale('icon/half-log.webp', 45, 45) xpos 150 ypos 600
            text "{size=24}{color=#ffffff} %i {/color}{/size}" %buildings_res_1 xpos 200 ypos 600
            text "{size=24}{color=#ffffff} Нужно человек для здания 5 {/color}{/size}"  xpos 150 ypos 650

    textbutton "Прокачать" action Jump("buildings_label_1") xpos 300 ypos 600


#--------------------------------2 постройка - забор/стена
    text "{size=24}{color=#ffffff}Построить забор {/color}{/size}" xpos 700 ypos 250
    add im.Scale('bg/bg_school/gate_upgrade_1.webp', 300, 150) xpos 700 ypos 300
    text "{size=24}{color=#ffffff}Улучшает защиту базы {/color}{/size}" xpos 700 ypos 480
    text "{size=24}{color=#ffffff} Нужно ресурсов {/color}{/size}" xpos 700 ypos 550
    text "{size=24}{color=#ffffff} Уровень постройки %s {/color}{/size}" % buildings_stage[1] xpos 700 ypos 510

    if buildings_stage[1] == buildings_stage_max[1]:
        text "{size=24}{color=#ffffff} Max lvl {/color}{/size}" xpos 700 ypos 600
    else:
        add im.Scale('icon/half-log.webp', 45, 45) xpos 650 ypos 600
        text "{size=24}{color=#ffffff} %i {/color}{/size}" %buildings_res_2 xpos 700 ypos 600
        text "{size=24}{color=#ffffff} Нужно человек для здания 10 {/color}{/size}"  xpos 650 ypos 650

    textbutton "Прокачать" action Jump("buildings_label_2") xpos 800 ypos 600


    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/sideswipe.png', 100, 100)
            hover im.Scale('icon/sideswipe_hover.png', 100, 100)
            action Jump('main_office_job')

#--------------------------------3 постройка - сад
    text "{size=24}{color=#ffffff}Построить сад на крыше {/color}{/size}" xpos 1200 ypos 250
    add im.Scale('bg/bg_school/garden_upgrade.webp', 300, 150) xpos 1200 ypos 300
    text "{size=24}{color=#ffffff}Позволяет выращивать еду прямо на базе {/color}{/size}" xpos 1200 ypos 480
    text "{size=24}{color=#ffffff} Нужно ресурсов {/color}{/size}" xpos 1200 ypos 550
    text "{size=24}{color=#ffffff} Уровень постройки %s {/color}{/size}" % buildings_stage[2] xpos 1200 ypos 510

    if buildings_stage[2] == buildings_stage_max[2]:
        text "{size=24}{color=#ffffff} Max lvl {/color}{/size}" xpos 1200 ypos 600
    else:
        add im.Scale('icon/half-log.webp', 45, 45) xpos 1160 ypos 600
        add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 1160 ypos 650

        text "{size=24}{color=#ffffff} %i {/color}{/size}" %buildings_res_3[0] xpos 1200 ypos 600
        text "{size=24}{color=#ffffff} %i {/color}{/size}" %buildings_res_3[1] xpos 1200 ypos 650

        text "{size=24}{color=#ffffff} Нужно человек для здания 20 {/color}{/size}"  xpos 1200 ypos 700

    textbutton "Прокачать" action Jump("buildings_label_3") xpos 1300 ypos 600


    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/sideswipe.png', 100, 100)
            hover im.Scale('icon/sideswipe_hover.png', 100, 100)
            action Jump('main_office_job')

label buildings_label_1:
    if buildings_in_process == True:
        MCh3 "Прости, но руки пока что заняты. Подожди пару дней"
        call screen build_update_screen
    if Parametrs_Num[2] >= buildings_res_1 and buildings_stage[0] != buildings_stage_max[0] :
        $ Parametrs_Num[2] -= buildings_res_1
        $ buildings_res_1 = (buildings_res_1/2)+buildings_res_1
        $ buildings_stage[0] += 1
        $ buildings_in_process = True
        $ buildings_time = 3
        MCh3 "Твоя постройка завершится через [buildings_time] дня"
        call screen build_update_screen
    elif Parametrs_Num[2] < buildings_res_1:
        "Не хватает ресурсов"
        call screen build_update_screen
    elif buildings_stage[0] == buildings_stage_max[0]:
        MCh3 "Больше эту постройку улучшить нельзя"
    call screen build_update_screen

label buildings_label_2:
    if buildings_in_process == True:
        MCh3 "Прости, но руки пока что заняты. Подожди пару дней"
        call screen build_update_screen
    if Parametrs_Num[2] >= buildings_res_2 and buildings_stage[1] != buildings_stage_max[1] :
        $ Parametrs_Num[2] -= buildings_res_2
        $ buildings_res_2 = (buildings_res_2/2)+buildings_res_2
        $ buildings_stage[1] += 1
        $ buildings_in_process = True
        $ buildings_time = 3
        MCh3 "Твоя постройка завершится через [buildings_time] дня"
        call screen build_update_screen
    elif Parametrs_Num[2] < buildings_res_2:
        "Не хватает ресурсов"
        call screen build_update_screen
    elif buildings_stage[1] == buildings_stage_max[1]:
        MCh3 "Больше эту постройку улучшить нельзя"
    call screen build_update_screen

label buildings_label_3:
    if buildings_in_process == True:
        MCh3 "Прости, но руки пока что заняты. Подожди пару дней"
        call screen build_update_screen
    if Parametrs_Num[2] >= buildings_res_3[0] and Parametrs_Num[0] >= buildings_res_3[1] and buildings_stage[2] != buildings_stage_max[2] :
        $ Parametrs_Num[2] -= buildings_res_3[0]
        $ Parametrs_Num[0] -= buildings_res_3[1]
        $ buildings_res_3[0] = ((buildings_res_3[0])/2)+buildings_res_3[0]
        $ buildings_res_3[1] = ((buildings_res_3[1])/2)+buildings_res_3[1]
        $ buildings_stage[2] += 1
        $ buildings_in_process = True
        $ buildings_time = 3
        MCh3 "Твоя постройка завершится через [buildings_time] дня"
        call screen build_update_screen
    elif Parametrs_Num[2] < buildings_res_3[0] or Parametrs_Num[0] < buildings_res_3[1]:
        "Не хватает ресурсов"
        call screen build_update_screen
    elif buildings_stage[2] == buildings_stage_max[2]:
        MCh3 "Больше эту постройку улучшить нельзя"
    call screen build_update_screen
