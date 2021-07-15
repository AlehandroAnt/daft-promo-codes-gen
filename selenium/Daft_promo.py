import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

cookie = [
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'lptracker_visitor_id', 'path': '/',
     'secure': False, 'value': '19719'},
    {'domain': '.join2duft.ru', 'expiry': 1685184188, 'httpOnly': False, 'name': '_ga_Q6QBD75DX0', 'path': '/',
     'secure': False, 'value': 'GS1.1.1622112160.1.1.1622112188.32'},
    {'domain': '.join2duft.ru', 'httpOnly': False, 'name': 'BITRIX_SM_SOUND_LOGIN_PLAYED', 'path': '/', 'secure': False,
     'value': 'Y'},
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'lp_tracker_id', 'path': '/',
     'secure': False, 'value': '14837'},
    {'domain': 'join2duft.ru', 'httpOnly': False, 'name': 'modal18', 'path': '/', 'secure': False, 'value': 'success'},
    {'domain': '.join2duft.ru', 'expiry': 1622113988, 'httpOnly': False, 'name': '_ym_visorc', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': 'w'},
    {'domain': 'join2duft.ru', 'expiry': 1622198589, 'httpOnly': False, 'name': 'lptracker_view_id', 'path': '/',
     'secure': False, 'value': ''},
    {'domain': '.join2duft.ru', 'expiry': 1653648161, 'httpOnly': False, 'name': '_ym_d', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '1622112161'},
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'OAuth_utm', 'path': '/',
     'secure': False, 'value': '1'},
    {'domain': 'join2duft.ru', 'expiry': 1937472161, 'httpOnly': False, 'name': 'BX_USER_ID', 'path': '/',
     'secure': False, 'value': '3b5a2dea89d6cdd322eef9c0a5fd1413'},
    {'domain': '.join2duft.ru', 'expiry': 1685184188, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
     'value': 'GA1.1.1048101137.1622112161'},
    {'domain': '.join2duft.ru', 'expiry': 1653648161, 'httpOnly': False, 'name': '_ym_uid', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '1622112161110391121'},
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'OAuth', 'path': '/', 'secure': False,
     'value': '319006689'},
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'ip', 'path': '/', 'secure': False,
     'value': ''}, {'domain': '.join2duft.ru', 'expiry': 1622184162, 'httpOnly': False, 'name': '_ym_isad', 'path': '/',
                    'sameSite': 'None', 'secure': True, 'value': '2'},
    {'domain': 'join2duft.ru', 'expiry': 1751712189, 'httpOnly': False, 'name': 'wr_visit_id', 'path': '/',
     'secure': False, 'value': '381238724'},
    {'domain': '.join2duft.ru', 'expiry': 1622198571, 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/',
     'secure': False, 'value': 'iXGB4Aln0H75gJNqGy4mzekdvr0QdkRq'}]


def generator():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    promocode_first = 'pher-'
    promocode_gen = ''
    promocode_second = '-omone'
    promocode = ''
    for i in range(13):
        promocode_gen += random.choice(chars)
    promocode = promocode_first + promocode_gen + promocode_second
    return promocode


def start():
    n = 0
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://join2duft.ru/catalog/')
    for i in cookie:
        driver.add_cookie(i)
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    enter_promo_link = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[1]/a')
    enter_promo_link.click()
    time.sleep(2)
    while True:
        enter_promo = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/div/input')
        enter_promo.click()
        enter_promo.clear()
        enter_promo.send_keys(generator())
        enter_promo.send_keys(Keys.ENTER)
        time.sleep(7)
        close_window = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]')
        time.sleep(1)
        close_window.click()
        n += 1
        print('Цикл: ', n)

start()
