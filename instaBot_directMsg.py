import pyautogui as pg
import webbrowser as web
import time


def chooseUserToMsg(name):
    pg.write(name)
    time.sleep(2)
    # press on the user
    pg.press('tab')
    pg.press('enter')
    time.sleep(1)


def sendNewMessage(name, msg):
    # new message fetcher
    time.sleep(1)
    pg.click(520, 200)

    time.sleep(2)
    chooseUserToMsg(name)

    # next button
    pg.click(850, 220)
    time.sleep(2)

    pg.write(msg)
    time.sleep(1)
    pg.press('enter')


def sendMultipleNewMessage(names, msg):
    # new message fetcher
    time.sleep(1)
    pg.click(520, 200)

    time.sleep(2)
    for name in names:
        chooseUserToMsg(name)

    # next button
    pg.click(850, 220)
    time.sleep(5)

    pg.write(msg)
    time.sleep(1)
    pg.press('enter')

if __name__ == '__main__':

    # login to instagram
    username = '<your username>'
    password = '<your password>'

    web.open('https://www.instagram.com/')
    time.sleep(3)

    pg.press('tab')
    pg.write(username)
    pg.press('tab')
    pg.write(password)
    time.sleep(1)

    pg.press('enter')
    time.sleep(10)

    # direct message fitcher
    pg.click(950, 140)
    time.sleep(2)

    # you can choose one from methods
    # send multi messages to some users:
    users = ['user1', 'user2', 'user3']
    sendMultipleNewMessage(users, '<your message>')

    # or send message to one user:
    sendNewMessage('<username>', '<your message>')



