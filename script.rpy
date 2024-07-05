

label resources:
    default Parametrs_Name = ["Еда", "Медикаменты", "Материалы", "Топливо", "Люди", "Болеющие", "Умерло", "Настроение жителей", "Репутация"]
    default Parametrs_Num =  [  100,      50,           100,          0,      120,       0,        0,            50,                  0]

# Определение персонажей игры.
define GG = Character('Казума', color="#c8ffc8")             # ГГ

# имена записаны как Фамилия - Имя
define FCh1 = Character('Кавасаки Айамэ', color="#953fab")  # сестра Кена (фиолетовые волосы)
define FCh2 = Character('Мацуда Акане', color="#ad0e0e")    # красноволосая хулиганка
define FCh3 = Character('Фудзивара Чика', color="#d1ce6d")  # подруга детства (блондинка жизнерадостная)
define FCh4 = Character('Оосава Эйко', color="#5b9ab3")     # Мед сестра (да такое тут тоже есть)
define FCh5 = Character('Ёсикава Кацуми', color="#b8794f")   # Учитель (а где остальные?)
define FCh6 = Character('Ооцука Касуми', color="#b851a6")   # Девочка которая сидит в библиотеке
define FCh7 = Character('NoName NoName', color="#5e0b0b")   # Девочка что из клуба отдыха

define MCh1 = Character('Курода Изаму', color="#d68315")     # Спортивный парень с оранж-ы волосами
define MCh2 = Character('Хакамада Хикару', color="#0f1b4d")  # друг гг не примечательный (хиккан)
define MCh3 = Character('Маруяма Кен', color="#581a82")      # временный лидер друг гг (очень умный)

define Ch1 = Character('Какой-то качок ', color="#184d70")
define Ch2 = Character('Мальчик 1', color="#2765f5")
define Ch2_1 = Character('Мальчик 2', color="#2765f5")
define Ch3 = Character('Девочка 1', color="#c925db")
define Ch3_1 = Character('Девочка 2', color="#c925db")


default tt = Tooltip("")

define FCh_relationship = [0,0,0,0,0,0]
define MCh_relationship = [0,0,0]

define tmp_Inventory_Items = [0,0,0,0]
define city_block_1 = [1000, 200, 250, 20]
define shop_block_1 = [2000, 400, 1100, 450]

# 1 - вышка. 2 - забор. 3 - огород
define buildings_stage = [0,0,0]
define buildings_stage_max = [1,2,2]
define buildings_in_process = False

define buildings_res_1 = 150 # Материалы
define buildings_res_2 = 200 # материалы
define buildings_res_3 = [200,50] # материалы и еда


# Начало игры:
label start:
    menu prolog:
        "Пропустить пролог?"
        "Да":
            play music "audio/music/Machine_Girl_Peace_of_Mind.mp3" volume 0.10 fadein 2 noloop
            call screen school_hub
        "Нет":
            "В разработке"
            play music "audio/music/Machine_Girl_Peace_of_Mind.mp3" volume 0.10 fadein 2 noloop
            call screen school_hub

    #call minigame_2_label
    #jump start_minigame
    #call screen school_hub
