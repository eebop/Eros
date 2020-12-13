import screen_data
import pygame
import time
import lan.send
import lan.recive
import random
import socket
import norm_keys_wrapper


writer = screen_data.screen_data(90)
writer2 = screen_data.screen_data(45)


def display(screen, words, level, writer=writer):
    level *= 200
    pygame.draw.rect(screen, (255, 255, 255), [100, level+20, 600, 100], width=5, border_radius=10)
    writer.print_words(screen, (255, 255, 255), words, (110, level+17))


def get_connection(screen):
    screen.fill((0, 0, 0))
    address = socket.gethostbyname(socket.gethostname())
    port = random.randrange(1024, 65535)
    display(screen, 'waiting for player', 0, writer2)
    display(screen, 'your address:\n' + str(address), 1, writer2)
    display(screen, 'your port:\n' + str(port), 2, writer2)
    pygame.display.flip()
    double_socket = lan.send.send(port)


def check_if_in(rect, location):
    w1 = rect[0]
    h1 = rect[1]
    w2 = rect[0] + rect[2]
    h2 = rect[1] + rect[3]
    if w1 <= location[0] <= w2 and h1 <= location[1] <= h2:
        return True


def run(screen):
    screen.fill((0, 0, 0))
    display(screen, ' new game', 0)
    display(screen, ' join game', 1)
    pygame.display.flip()
    has_clicked = False
    while not has_clicked:
        events = pygame.event.get()
        events = [x for x in events if x.type == pygame.MOUSEBUTTONDOWN and x.button == 1]

        for event in events:
            loc = [100, 20, 600, 100]
            loc2 = [100, 220, 600, 100]
            if check_if_in(loc, event.pos):
                has_clicked = 1
            elif check_if_in(loc2, event.pos):
                has_clicked = 2

    if has_clicked == 1:
        get_connection(screen)
        return True
    return False


def move_as_computer(events):
    return [0, 0, 0, 0]


def get_adr_and_port(screen):
    screen.fill((0, 0, 0))
    address = '' # 1
    port = '' # 2
    selected = None
    enabled_keys = [pygame.K_PERIOD, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                     pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                                     pygame.K_BACKSPACE]
    key_reference = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\b']

    while True:
        display(screen, 'enter address:\n'+address, 0, writer2)
        display(screen, 'enter port:\n'+port, 1, writer2)
        display(screen, '   Done', 2, writer)
        pygame.display.flip()
        events = pygame.event.get()
        mouse_events = [x for x in events if x.type == pygame.MOUSEBUTTONDOWN and x.button == 1]
        key_events = [x for x in events if x.type == pygame.KEYDOWN and x.key in enabled_keys and x.mod == 0]
        all_out = False
        for m_event in mouse_events:
            if check_if_in([100, 420, 600, 100], m_event.pos):
                return address, port

            if check_if_in([100, 20, 600, 100], m_event.pos):
                selected = 1
                all_out = False

            elif check_if_in([100, 220, 600, 100], m_event.pos):
                selected = 2
                all_out = False
            else:
                all_out = True
        if all_out:
            selected = None

        for key in key_events:
            act_key = key_reference[enabled_keys.index(key.key)]
            if selected == 1:
                if act_key != '\b':
                    address += act_key
                else:
                    address = address[:-1]
            if selected == 2:
                if act_key != '\b':
                    port += act_key
                else:
                    port = port[:-1]
        screen.fill((0, 0, 0))

def fail(screen):
    screen.fill((0, 0, 0))
    display(screen, '   that is invalid', 0, writer2)
    pygame.display.flip()
    time.sleep(1.5)
    return get_adr_and_port(screen)

def run_as_guest(screen):
    valid_address = False
    while not valid_address:
        address, port = get_adr_and_port(screen)
        is_okay = False
        while not is_okay:
            try:
                int(port)
            except ValueError as e:
                address, port = fail(screen)
            else:
                port = int(port)
                if 1024 <= port <= 65534:
                    '''if you change these lines (134-145) in a certain way, you will
                    be able to send over the internet. There is several other steps to do this
                    involving setting up your router. I strongly recomened against this,
                    because hackers will be able to edit the (insecure) pickle to execute
                    arbitrary code on you machine'''
                    if 11 <= len(address) <= 15:
                        if address[:8] == '192.168.':
                            is_okay = True
                        else:
                            address, port = fail(screen)
                    else:
                        address, port = fail(screen)
                else:
                    address, port = fail(screen)
        print('okay')
        try:
            double_socket = lan.recive.recive(address, port)
            valid_address = True
        except ConnectionRefusedError:
            screen.fill((0, 0, 0))
            display(screen, 'that is invalid (CRE)', 0, writer2)
            pygame.display.flip()
            time.sleep(1.5)
