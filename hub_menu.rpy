

# ______________________________________________ Главный хаб
screen school_hub:
    # Экран школы
    imagemap:
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        add im.Scale('gui/frame_2.webp', 800, 50) xpos 600 ypos 0

        text "{size=24}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % WeekDays[WeekDayNumber] xpos 1605 ypos 45
        text "{size=24}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1800 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % Mouth[MouthDaysNum] xpos 1605 ypos 70


        add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 610 ypos 0
        text "{size=20}{color=#ffffff}: %i {/color}{/size}" %Parametrs_Num[0] xpos 660 ypos 10
        add im.Scale('icon/medical-pack-alt.webp', 45, 45) xpos 750 ypos 0
        text "{size=20}{color=#ffffff}: [Parametrs_Num[1]] {/color}{/size}" xpos 800 ypos 10
        add im.Scale('icon/half-log.webp', 45, 45) xpos 870 ypos 0
        text "{size=20}{color=#ffffff}: [Parametrs_Num[2]] {/color}{/size}" xpos 920 ypos 10
        add im.Scale('icon/oil-drum.webp', 45, 45) xpos 990 ypos 0
        text "{size=20}{color=#ffffff}: [Parametrs_Num[3]] {/color}{/size}" xpos 1040 ypos 10
        add im.Scale('icon/person.png', 45, 45) xpos 1100 ypos 0
        text "{size=20}{color=#ffffff}: [Parametrs_Num[4]] {/color}{/size}" xpos 1150 ypos 10
        add im.Scale('icon/person-in-bed_hover.png', 45, 45) xpos 1225 ypos 0
        text "{size=20}{color=#ffffff}: [Parametrs_Num[5]] {/color}{/size}" xpos 1280 ypos 10

        if Hours >= 6 and Hours < 16:
                idle 'morning_school'
        if Hours >= 16 and Hours < 20:
                idle 'evening_school'
        if Hours >= 20 and Hours < 25:
                idle 'night_school'
    # Кнопки
    vbox xalign 0.03 yalign 0.05 spacing 5:
        # Кнопка перехода
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('time_schoolhub')
        imagebutton:
            idle im.Scale('icon/backpack.png', 100, 100)
            hover im.Scale('icon/backpack_hover.webp', 100, 100)
            action Jump('GG_character_open')
        imagebutton:
            idle im.Scale('icon/checklist.png', 100, 100)
            hover im.Scale('icon/checklist_hover.webp', 100, 100)
            action Jump('tasks_label_open')

# Меню перехода
label hub_choose_label:
    scene darkscreen
    menu Chose_3:
        "Куда хотите попасть?"
        "Библиотека":
            call screen Library_screen
        "Тренировочный зал":
            call screen Gym_screen
        "В главный кабинет":
            call screen Main_office_screen
        "Комната отдыха":
            call screen restroom_screen
        "Отправиться на вылазку":
            if Hours >= 23:
                "Слишком поздно для вылазок"
                call screen school_hub
                
            if GG_skill_2 == True:
                $ Minutes += 30
            else:
                $ Hours += 1
            stop music fadeout 1.0
            call screen city_hub  
        "Хаб":
            call screen school_hub


# ______________________________________________ Спотривный зал
screen Gym_screen:
    imagemap:
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{size=24}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % WeekDays[WeekDayNumber] xpos 1605 ypos 45
        text "{size=24}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1800 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % Mouth[MouthDaysNum] xpos 1605 ypos 70

        if Hours >= 6 and Hours < 16:
            idle 'gym_1'
            hover 'gym_1_hover'
            hotspot (1166, 453, 178, 282) action Jump('talk_gym_1')
            hotspot (312, 245, 125, 390) action Jump('talk_gym_2')
        if Hours >= 16 and Hours < 20:
            idle 'gym_2'
            hover 'gym_2_hover'
            hotspot (1448, 400, 265, 419) action Jump('talk_gym_3')
        if Hours >= 20 and Hours < 25:
            idle 'gym_3'

    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('time_schoolhub')


# ______________________________________________ Главный оффис
screen Main_office_screen:
    imagemap:
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{size=24}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % WeekDays[WeekDayNumber] xpos 1605 ypos 45
        text "{size=24}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1800 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % Mouth[MouthDaysNum] xpos 1605 ypos 70

        if Hours >= 6 and Hours < 16:
                idle 'main_office_1'
                hover 'main_office_1_hover'
                hotspot (899, 445, 148, 136) action Jump('talk_main_office_1')
        if Hours >= 16 and Hours < 20:
                idle 'main_office_2'
                hover 'main_office_2_hover'
                hotspot (899, 445, 148, 136) action Jump('talk_main_office_1')
                hotspot (1321, 490, 289, 453) action Jump('talk_main_office_3')
        if Hours >= 20 and Hours < 25:
                idle 'main_office_3'

    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('time_schoolhub')


# ______________________________________________ библиотека
screen Library_screen:
    imagemap:
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{size=24}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % WeekDays[WeekDayNumber] xpos 1605 ypos 45
        text "{size=24}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1800 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % Mouth[MouthDaysNum] xpos 1605 ypos 70

        if Hours >= 6 and Hours < 16:
                idle 'library_1'
                hover 'library_1_hover'
                hotspot (2, 640, 290, 380) action Jump('talk_library_1')
                hotspot (1655, 474, 224, 126) action Jump('talk_library_2')
        if Hours >= 16 and Hours < 20:
                idle 'library_2'
                hover 'library_2_hover'
                hotspot (2, 640, 290, 380) action Jump('talk_library_1')
        if Hours >= 20 and Hours < 25:
                idle 'library_3'

    vbox xalign 0.03 yalign 0.05 spacing 5:
        # Кнопка перехода
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('time_schoolhub')


# ______________________________________________ Комната отдыха
screen restroom_screen:
    imagemap:
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{size=24}{color=#ffffff}[Days] день {/color}{/size}" xpos 1610 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % WeekDays[WeekDayNumber] xpos 1605 ypos 45
        text "{size=24}{color=#ffffff}[Hours]:[MinutesStr]{/color}{/size}" xpos 1800 ypos 15
        text "{size=24}{color=#ffffff} %s {/color}{/size}" % Mouth[MouthDaysNum] xpos 1605 ypos 70

        if Hours >= 6 and Hours < 16:
                idle 'restroom_1'
                hover 'restroom_1_hover'
                hotspot (1341, 552, 190, 333) action Jump('talk_restroom_1')
                hotspot (1079, 403, 125, 209) action Jump('talk_restroom_2')
                hotspot (150, 680, 606, 352) action Jump('talk_restroom_3')
        if Hours >= 16 and Hours < 20:
                idle 'restroom_2'
                hover 'restroom_2_hover'
                hotspot (1341, 552, 190, 333) action Jump('talk_restroom_1')
                hotspot (150, 680, 606, 352) action Jump('talk_restroom_3')
        if Hours >= 20 and Hours < 25:
                idle 'restroom_3'

    vbox xalign 0.03 yalign 0.05 spacing 5:
        # Кнопка перехода
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('time_schoolhub')



label return_home_late:
    hide screen healthbar
    hide screen staminabar
    hide screen staminabar_2
    hide screen infectionbar
    hide screen back_data
    python:
        # Складываем добытые вещи в хранилище
        for i in range(len(GG_Inventory_Items)):
            Parametrs_Num[i] += GG_Inventory_Items[i]
            GG_Inventory_Items[i] = 0
    call screen school_hub
