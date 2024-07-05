# определения переменных для счета времени/даты
label calendar:
    default Year = 2016
    default Mouth = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
                    "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    default MouthDays = [31, 28,31,30,31,30,31,31,30,31,30,31]
    default MouthDaysNum = 3 # Номер месяца Mouth[MouthDaysNum] или MouthDays[MouthDaysNum]
    default WeekDays = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Восресенье"]
    default WeekDayNumber = 0 # Номер недели
    default Days = 1 # Какой сечайс день
    default Hours = 6 # сколько часов
    default Minutes = 30 # сколько минут
    default MinutesStr = "%d" % Minutes # полсьл вывод в виде 12:00 например. Иначе было бы 12:0
    default Totaly_Days = 0 # Сколько прошло в сумме дней

    default buildings_time = 0 # Время постройки здания

define type_of_screen = 0
define tmp_pn = 0

#Считаем время
label time_schoolhub:
    scene darkscreen
    # Меню для выбора работы с временем
    menu awaiting:
        "Сколько хотите ждать?"
        "Назад":
            call GG_character_update from _call_GG_character_update
        "30 мин":
            $ Minutes += 30
            call GG_character_update from _call_GG_character_update_1
        "1 час":
            $ Hours += 1
            call GG_character_update from _call_GG_character_update_2
        "Ждать до вечера":
            if Hours < 16 and Hours >= 6:
                    $ Hours = 16
                    $ Minutes = 0
            call GG_character_update from _call_GG_character_update_3
        "Перейти к следующему дню":
            $ Hours = 24
            call GG_character_update from _call_GG_character_update_4
    # Считаем минуты
    if Minutes >= 60:
        $ Minutes -= 60
        $ Hours += 1
    # Считаем часы. Обновляем время для нового дня
    if Hours > 23:

        $ day_event = renpy.random.randint(1,50)
        if day_event < 11 and buildings_stage[0] >= 1 and buildings_stage[1] >= 1:
            "Ночью было нападение зомби"
            "Благодаря укреплениям удалось минимизировать ущерб. Были потрачены материалы и медикаменты, а так же пару раненых"
            $ Parametrs_Num[1] -= renpy.random.randint(1,2)
            $ Parametrs_Num[2] -= renpy.random.randint(1,8)
            $ day_event = renpy.random.randint(1,2)
            $ Parametrs_Num[4] -= day_event
            $ Parametrs_Num[5] += day_event
        if day_event < 11 and ((buildings_stage[0] >= 0 and buildings_stage[1] >= 1) or  (buildings_stage[0] >= 1 and buildings_stage[1] >= 0)):
            "Ночью было нападение зомби"
            "Наших укреплений еле хватило чтобы отбить атаку. Были потрачены материалы и медикаменты, а так же пару раненых"
            $ Parametrs_Num[1] -= renpy.random.randint(1,5)
            $ Parametrs_Num[2] -= renpy.random.randint(1,8)
            $ day_event = renpy.random.randint(1,5)
            $ Parametrs_Num[4] -= day_event
            $ Parametrs_Num[5] += day_event
        if day_event < 11 and buildings_stage[0] == 0 and buildings_stage[1] == 0:
            "Ночью было нападение зомби"
            "Мы понесли значительные потери из-за отсутствия обороны. Были потрачены материалы и медикаменты, а так же пару раненых"
            $ Parametrs_Num[1] -= renpy.random.randint(5,10)
            $ Parametrs_Num[2] -= renpy.random.randint(5,16)
            $ day_event = renpy.random.randint(3,8)
            $ Parametrs_Num[4] -= day_event
            $ Parametrs_Num[5] += day_event
        if Parametrs_Num[0] <= 0:
            "У нас закончилась еда. Нужно найти еще, иначе мы долго не протянем"
        if Parametrs_Num[1] <= 0:
            "У нас закончились медикаменты. Нужно найти еще, иначе мы не сможел лечить больных"

        python:
            type_of_screen = renpy.random.randint(0,1) # Для разныйх вариаций комнат
        $ Hours = 6
        $ Days += 1
        $ WeekDayNumber += 1
        $ Minutes = 0
        $ Totaly_Days += 1 # Подсчет сколько дней всего прошло

        # Вычитане ресурсов. Ежедневные расходы
        $ tmp_pn = 0
        # Подсчет еды и лекарств и ресурсов
        if buildings_stage[2] == 1 and Parametrs_Num[4] > 20:
            $ Parametrs_Num[0] += 10
        elif buildings_stage[2] == 2 and Parametrs_Num[4] > 20:
            $ Parametrs_Num[0] += 20
        $ Parametrs_Num[0] -= (Parametrs_Num[4] * 0.3)
        $ Parametrs_Num[0] -= (Parametrs_Num[5] * 0.3)
        $ Parametrs_Num[1] -= renpy.random.randint(0, 2)
        $ Parametrs_Num[2] -= renpy.random.randint(0, 2)
        $ Parametrs_Num[3] -= 1

        # Время постройки
        if buildings_time != 0:
            $ buildings_time -= 1
        if buildings_time == 0:
            $ buildings_in_process = False

        if Parametrs_Num[3] < 0:
            $ Parametrs_Num[3] = 0

        # если нет еды или медикаментов, то люди будут болеть
        if Parametrs_Num[0] <= 0 or Parametrs_Num[1] <= 0:
            python:
                tmp_pn += renpy.random.randint(0,5)
                Parametrs_Num[5] += tmp_pn
                Parametrs_Num[4] -= tmp_pn
                Parametrs_Num[0] = 0
                Parametrs_Num[1] = 0
        $ tmp_pn = 0

        # Если больных будет много, то они начнут умирать
        if Parametrs_Num[5] >= 15:
            python:
                tmp_pn += renpy.random.randint(0,6)
                Parametrs_Num[6] += tmp_pn
                Parametrs_Num[5] -= tmp_pn
        $ tmp_pn = 0

        # Если есть еда и меедикоменты, то люди будут выздоравливать
        if Parametrs_Num[0] > 0 and Parametrs_Num[1] > 0:
            python:
                tmp_pn += renpy.random.randint(0,3)
                if Parametrs_Num[5] != 0 or Parametrs_Num[5] > 0:
                    if tmp_pn > Parametrs_Num[5]:
                        tmp_pn = 1
                    Parametrs_Num[1] -= tmp_pn
                    Parametrs_Num[5] -= tmp_pn
                    Parametrs_Num[4] += tmp_pn
        if Parametrs_Num[4] < 10:
            "Вас было слишком мало чтобы противостоять мертвецам"
            "Эта база была обречена на смерть"
            return

    if WeekDayNumber > 6:
        $ WeekDayNumber = 0
    if Days > MouthDays[MouthDaysNum]:
        $ MouthDaysNum += 1
        $ Days = 1
    if MouthDaysNum > 11:
        $ MouthDaysNum = 0
        $ Year += 1
    if Minutes < 10:
        $ MinutesStr = "0%d" % Minutes
    else:
        $ MinutesStr = "%d" % Minutes

    # Эвенты после завершения дня
    scene morning_school with fade
    
    call screen school_hub

# Отдых - город/тц
label time2:
    $ Hours += 1
    if Minutes >= 60:
        $ Minutes -= 60
        $ Hours += 1
    if Minutes < 10:
        $ MinutesStr = "0%d" % Minutes
    else:
        $ MinutesStr = "%d" % Minutes
    if Hours >= 23:
        "Слишком поздно, нужно возвращатся"
        jump return_home_late
    return

# Трата времени на действия
label time3:
    if GG_skill_2 == True:
        $ Minutes += 20
    else:
        $ Minutes += 30
        
    if Minutes >= 60:
        $ Minutes -= 60
        $ Hours += 1
    if Minutes < 10:
        $ MinutesStr = "0%d" % Minutes
    else:
        $ MinutesStr = "%d" % Minutes
    if Hours >= 23:
        "Слишком поздно, нужно возвращатся"
        jump return_home_late
    return
