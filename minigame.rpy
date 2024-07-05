
#----------------------Миниигра во время тренировок в зале

label minigame_1_label:
    scene gym_job_1 with fade
    $ cont = 0
    $ arr_keys = ["z", "x", "c"]    #Клавишы которые игрок должен нажимать
    call qte_setup(1.0, 1.0, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup
    $ scene_count = 0
    $ minigame1_count = 0   #Сколько ударов сделано
    while cont == 1:
        if scene_count == 0:
            scene gym_job_3
            $ scene_count = 1
        elif scene_count == 1:
            scene gym_job_2
            $ scene_count = 0
        play sound "audio/sounds/light_punch.wav"
        call qte_setup(1.0,1.0, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup_1
        $ minigame1_count += 1

    play sound "audio/sounds/game_over_yea.mp3"
    "{b}Тренировка окончена{/b}"
    "Ударов было сделано [minigame1_count]"
    return

label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen minigame_1_screen

    $ cont = _return

    return


screen minigame_1_screen:
    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    key trigger_key action ( Return(1) )
    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement
        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"

