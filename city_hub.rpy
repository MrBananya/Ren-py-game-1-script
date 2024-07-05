
# ______________________________________________ Хаб города
screen city_hub:
    # Экран города
    imagemap:
        idle im.Scale('city_map_v2.webp', 1920, 1080)
        hover im.Scale('city_map_v2_hover.webp', 1920, 1080)
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{color=#ffffff}[Days] день {/color} " xpos 1600 ypos 10
        text "{color=#ffffff} %s {/color}" % WeekDays[WeekDayNumber] xpos 1600 ypos 44
        text "{color=#ffffff}[Hours]:[MinutesStr]{/color}" xpos 1800 ypos 10
        hotspot (45, 536, 128, 124) action Jump('forest') hovered tt.Action("Лес")           #Локация лес
        hotspot (462, 680, 121, 111) action Jump('back_to_hub') hovered tt.Action("База") # На базу
        hotspot (706, 742, 116, 116) action Jump('houses') hovered tt.Action("Жилая зона")        # Дома
        hotspot (881, 740, 104, 106) action Jump('shops') hovered tt.Action("Комерческая зона")        # Рынок

        text "{size=40}{color=#0f1b4d} %s {/color}{/size}" %  tt.value xpos 50 ypos 50



# Инвентарь который показывается во время вылазок
screen back_data:
    add im.Scale('gui/frame_2.webp', 800, 50) xpos 600 ypos 0
    add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
    text "{color=#ffffff}[Days] день {/color} " xpos 1600 ypos 10
    text "{color=#ffffff} %s {/color}" % WeekDays[WeekDayNumber] xpos 1600 ypos 44
    text "{color=#ffffff}[Hours]:[MinutesStr]{/color}" xpos 1800 ypos 10

    add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 610 ypos 0
    text "{size=20}{color=#ffffff}: %i {/color}{/size}" %GG_Inventory_Items[0] xpos 660 ypos 10
    add im.Scale('icon/medical-pack-alt.webp', 45, 45) xpos 750 ypos 0
    text "{size=20}{color=#ffffff}: [GG_Inventory_Items[1]] {/color}{/size}" xpos 800 ypos 10
    add im.Scale('icon/half-log.webp', 45, 45) xpos 870 ypos 0
    text "{size=20}{color=#ffffff}: [GG_Inventory_Items[2]] {/color}{/size}" xpos 920 ypos 10

#-----------------------Назад в mainhub
label back_to_hub:
    hide screen staminabar_2
    $tmp = renpy.random.randint(1,2)
    if tmp == 1:
        play music "audio/music/Machine_Girl_Peace_of_Mind.mp3" volume 0.10 fadein 1.0 noloop
    else:
        play music "audio/music/Machine_Girl_Heaven_Central_Authority_(Mikey's Theme).mp3" volume 0.10 fadein 1.0 noloop
    jump return_home_late
    call screen school_hub

#-----------------------Лутинг в жилой зоне
label houses:

    show screen back_data
    show screen staminabar_2

    if Hours >= 6 and Hours < 16:
        scene city_1_street_1
    if Hours >= 16 and Hours < 20:
        scene city_1_street_2
    if Hours >= 20 and Hours < 25:
        scene city_1_street_3

    menu houses_job:
        "Заняться поисками ресурсов":
            if GG_Stamina[0] <= 0:
                "Нужно отдохнуть"
                jump houses
            $ GG_Stamina[0] -= 5
            $ tmp0  = renpy.random.randint(1,11)

            if tmp0 < 6:
                "Вы нашли немного припасов"
                python:
                    for i in range(4):
                        tmp_Inventory_Items[i] = renpy.random.randint(5, 15)
                        if city_block_1[i] > tmp_Inventory_Items[i]:
                            GG_Inventory_Items[i] += tmp_Inventory_Items[i]
                            city_block_1[i] -= tmp_Inventory_Items[i]
                        else:
                            "Кажется в этой области больше не осталось ресурсов"

                call time3 from _call_time3
                jump houses

            elif tmp0 > 5 and tmp0 < 9:
                "Во время поиска припасов на вас напали"

                jump battle_label

            elif tmp0 == 9:
                "Вы наткнулись на закрытый ящик"
                if GG_city_lockpick == False:
                    GG "Нужно будет найти способ как это открыть"
                    $ tasks[3]['state'] = 1
                    $ GG_city_lockpick = True
                    jump houses
                elif GG_city_lockpick == True:
                    "Хотите попробовать открыть? Имеется [lockpick] отмычек"
                    menu open_chest:
                        "Да":
                            if lockpick == 0:
                                "У вас нету отмычек"
                                jump houses
                            else:
                                $ tmp0  = renpy.random.randint(1,100)
                                if tmp0 < 11:
                                    "Взлом прошел успешно"
                                    "Вы нашли еду и медикаменты"
                                    python:
                                        for i in range(2):
                                            tmp_Inventory_Items[i] = renpy.random.randint(10, 20)
                                            GG_Inventory_Items[i] += tmp_Inventory_Items[i]
                                            city_block_1[i] -= tmp_Inventory_Items[i]
                                    jump houses
                                else:
                                    $ tmp0  = renpy.random.randint(1,50)
                                    if tmp0 < 26:
                                        "Замок не взломан"
                                        "Попробовать еще раз? Имеется [lockpick] отмычек"
                                        jump open_chest
                                    else:
                                        "Вы сломали отмычку"
                                        $ lockpick -= 1
                                        "Попробовать еще раз? Имеется [lockpick] отмычек"
                                        jump open_chest


                        "Нет":
                            jump houses
                    jump houses

            elif tmp0 == 10:
                "Блуждая по городу тебе попались люди"
                $ Parametrs_Num[4] += renpy.random.randint(1, 2)
                jump houses

            else:
                "Поиски не увенчались успехом"
                call time3 from _call_time3_1
                jump houses

        "Вернутья на карту":
            call screen city_hub

        "Отдохнуть":
            call GG_rest_outside from _call_GG_rest_outside

            "Вы потратили время на отдых"
            call time2 from _call_time2
            jump houses


#-----------------------лутинг в торговой зоне
label shops:

    show screen back_data
    show screen staminabar_2

    if Hours >= 6 and Hours < 16:
        scene city_1_shops_1
    if Hours >= 16 and Hours < 20:
        scene city_1_shops_2
    if Hours >= 20 and Hours < 25:
        scene city_1_shops_3

    menu shop_job:
        "Заняться поисками ресурсов":
            if GG_Stamina[0] <= 0:
                "Нужно отдохнуть"
                jump shops
            $ GG_Stamina[0] -= 5
            $ tmp0  = renpy.random.randint(1,11)

            if tmp0 < 6:
                "Вы нашли немного припасов"
                python:
                    for i in range(4):
                        tmp_Inventory_Items[i] = renpy.random.randint(5, 15)
                        if shop_block_1[i] > tmp_Inventory_Items[i]:
                            GG_Inventory_Items[i] += tmp_Inventory_Items[i]
                            shop_block_1[i] -= tmp_Inventory_Items[i]
                        else:
                            "Кажется в этой области больше не осталось ресурсов"

                call time3 from _call_time3_2
                jump shops

            elif tmp0 > 5 and tmp0 < 9:
                "Во время поиска припасов на вас напали"
                jump battle_label

            elif tmp0 == 9:
                "Вы наткнулись на закрытый ящик"
                if GG_city_lockpick == False:
                    GG "Нужно будет найти способ как это открыть"
                    $ tasks[3]['state'] = 1
                    $ GG_city_lockpick = True
                    jump shops
                elif GG_city_lockpick == True:
                    "Хотите попробовать открыть?"
                    menu open_chest_2:
                        "Да":
                            if lockpick == 0:
                                "У вас нету отмычек"
                                jump shops
                            else:
                                $ tmp0  = renpy.random.randint(1,100)
                                if tmp0 < 11:
                                    "Взлом прошел успешно"
                                    "Вы нашли еду и медикаменты"
                                    python:
                                        for i in range(2):
                                            tmp_Inventory_Items[i] = renpy.random.randint(10, 20)
                                            GG_Inventory_Items[i] += tmp_Inventory_Items[i]
                                            shop_block_1[i] -= tmp_Inventory_Items[i]
                                    jump shops
                                else:
                                    $ tmp0  = renpy.random.randint(1,50)
                                    if tmp0 < 26:
                                        "Замок не взломан"
                                        "Попробовать еще раз?"
                                        jump open_chest_2
                                    else:
                                        "Вы сломали отмычку"
                                        $ lockpick -= 1
                                        "Попробовать еще раз?"
                                        jump open_chest_2

                        "Нет":
                            jump shops
                    jump shops

            elif tmp0 == 10:
                "Блуждая по городу тебе попались люди"
                $ Parametrs_Num[4] += renpy.random.randint(1, 2)
                jump shops

            else:
                "Поиски не увенчались успехом"
                call time3 from _call_time3_3
                jump shops

        "Вернутья на карту":
            call screen city_hub

        "Отдохнуть":
            call GG_rest_outside from _call_GG_rest_outside_1

            "Вы потратили время на отдых"
            call time2 from _call_time2_1
            jump shops



#-----------------------Назад в mainhub
label forest:
    if Hours >= 6 and Hours < 16:
        scene forest_1
    if Hours >= 16 and Hours < 20:
        scene forest_2
    if Hours >= 20 and Hours < 25:
        scene forest_3


    show screen back_data
    show screen staminabar_2
    menu forest_harvest:
        "Поиск еды":
            if GG_Stamina[0] <= 0:
                "Нужно отдохнуть"
                jump forest
            $ GG_Stamina[0] -= 5
            $ tmp0  = renpy.random.randint(0,3)

            if tmp0 == 0:

                if GG_forest_book_read == False:
                    "Вы нашли ягодный куст, но вам не знакомы эти ягоды. Вы решили, что лучше не рисковать и оставили их"
                    $ tmp_show = renpy.random.randint(1, 5)
                    $ GG_Inventory_Items[0] += tmp_show
                            # Для активации здания при поиске грибов
                    if GG_forest_visited == False:
                        GG "Надо будет посмотреть в библиотеке какую-нибудь книгу по растениям."
                        $ GG_forest_visited = True
                        $ tasks[1]['state'] = 1
                if GG_forest_book_read == True:
                    "Вы нашли куст с ягодами и собрали все что смогли"
                    $ tmp_show = renpy.random.randint(2, 10)

                    #Плюс к еде от навыка
                    if GG_skill_4 == True:
                        $ tmp_show += renpy.random.randint(2, 10)
                    $ GG_Inventory_Items[0] += tmp_show

            elif tmp0 == 1:

                if GG_forest_book_read == False:
                    "На поляне росли грибы. Большинство вам не знакомо. Вы собрали только те что знаете"
                    $ tmp_show = renpy.random.randint(1, 5)
                    $ GG_Inventory_Items[0] += tmp_show
                            # Для активации здания при поиске грибов
                    if GG_forest_visited == False:
                        GG "Надо будет посмотреть в библиотеке какую-нибудь книгу по растениям"
                        $ GG_forest_visited = True
                        $ tasks[1]['state'] = 1
                if GG_forest_book_read == True:
                    "Вы наткнулись на поляну с грибами и собрали съедобную часть"
                    $ tmp_show = renpy.random.randint(2, 10)

                    #Плюс к еде от навыка
                    if GG_skill_4 == True:
                        $ tmp_show += renpy.random.randint(2, 10)
                    $ GG_Inventory_Items[0] += tmp_show

            else:
                "Вы ничего не нашли"

            call time3 from _call_time3_4
            jump forest
        "Поиск материалов":

            if GG_Stamina[0] <= 0:
                "Нужно отдохнуть"
                jump forest
            $ GG_Stamina[0] -= 5

            $ tmp0  = renpy.random.randint(0,2)
            if tmp0 == 0:
                "Вы нашли немного материалов для строительства"
                $ tmp_show = renpy.random.randint(1, 3)
                $ GG_Inventory_Items[2] += tmp_show
            elif tmp0 == 1:
                if GG_forest_book_read == True:
                    "Вы нашли лекарственные травы"
                    $ tmp_show = renpy.random.randint(1, 5)
                    $ GG_Inventory_Items[1] += tmp_show
                else:
                    "Из-за незнании многих трав вы собрали все что смогли"
                    $ tmp_show = renpy.random.randint(1, 2)
                    $ GG_Inventory_Items[1] += tmp_show
                    if GG_forest_visited == False:
                        GG "Надо будет посмотреть в библиотеке какую-нибудь книгу по растениям"
                        $ GG_forest_visited = True
                        $ tasks[1]['state'] = 1

            else:
                "Ваши поиски не увенчались успехом"
            call time3 from _call_time3_5
            jump forest
        "Отдохнуть":
            $ tmp0 = renpy.random.randint(0,10)
            if tmp0 == 0:
                "Во время отдыха тебя покусал ежик. Обидно :( "
            call GG_rest_outside from _call_GG_rest_outside_2
            "Вы потратили время на отдых"
            call time2 from _call_time2_2
            jump forest
        "Открыть карту":
            hide screen back_data
            call screen city_hub


#screen fight_city:
