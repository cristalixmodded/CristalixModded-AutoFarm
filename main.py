from art import tprint
from time import sleep
from pyautogui import press, typewrite, leftClick
from win32gui import IsWindowVisible, GetWindowText, SetForegroundWindow, EnumWindows
from configparser import ConfigParser

tprint('AutoFarm')
config = ConfigParser()

def new_config():
    save = input('Сохранить конфигурацию? (да/нет): ')
    if save == 'да':
        save = True
    else:
        save = False
    
    global server_name 
    server_name = input('Введите название сервера (С уЧёТоМ рАсКлАдКи!): ')
    
    global user_nickname 
    user_nickname = input('Введите Ваш никнейм (С уЧёТоМ рАсКлАдКи!): ')
    
    global ores_warp 
    ores_warp = input('Введите название варпа с рудой: ')
    
    global ores_slot
    ores_slot = input('Введите номер слота в киркой: ')
    
    global mobs_warp 
    mobs_warp = input('Введите названия варпа с мобами:')
    
    global mobs_slot
    mobs_slot = input('Введите номер слота с мечом: ')
    
    global interval
    interval = input('Введите промежуток между подходам (в минутах): ')
    interval = int(interval) * 60
    
    if save:
        config.set('Config', 'save', str(save))
        config.set('Config', 'server_name', server_name)
        config.set('Config', 'user_nickname', user_nickname)
        config.set('Config', 'ores_warp', ores_warp)
        config.set('Config', 'ores_slot', ores_slot)
        config.set('Config', 'mobs_warp', mobs_warp)
        config.set('Config', 'mobs_slot', mobs_slot)
        config.set('Config', 'interval', str(interval))
        
        with open('config.ini', 'w') as config_file:
            config.write(config_file)

config.read_file(open(r'config.ini'))
save = eval(config.get('Config', 'save'))
if save:
    if input('Загрузить последнюю конфигурацию? (да/нет): ') == 'да':
        server_name = config.get('Config', 'server_name')
        user_nickname = config.get('Config', 'user_nickname')
        ores_warp = config.get('Config', 'ores_warp')
        ores_slot = config.get('Config', 'ores_slot')
        mobs_warp = config.get('Config', 'mobs_warp')
        mobs_slot = config.get('Config', 'mobs_slot')
        interval = config.get('Config', 'interval')
    else:
        new_config()
else:
    new_config()

def enum_handler(hwnd, ctx):
    if IsWindowVisible(hwnd):
        if f'Cristalix {server_name} » {user_nickname}' in GetWindowText(hwnd):
            SetForegroundWindow(hwnd)

def tp(name):
    for i in range(2):
        press('t')
        typewrite(name, interval=0.25)
        press('enter')

def click(slot, click_range, time_sleep):
    press(slot)
    for i in range(click_range):
        leftClick()
        sleep(time_sleep)

while True:
    for i in reversed(range(1, 11)):
        print('Фарм начнется через ' + str(i) + ' секунд.')
        sleep(1)
    
    EnumWindows(enum_handler, None)

    tp('/warp ' + ores_warp)
    click(ores_slot, 6, 3)
        
    tp('/warp ' + mobs_warp)
    click(mobs_slot, 12, 10)
    
    tp('/home')
    
    print('Фарм закончен.')
    sleep(interval)