import screen_data
import pygame
import time
import lan.send
import lan.recive
import random
import socket
import sys
from threading import Thread
import lan.guest
from lan.download_protocol import get_local_address


writer = screen_data.screen_data(90)
writer2 = screen_data.screen_data(45)



def display(screen, words, level, writer=writer):
    level *= 200
    try:
        pygame.draw.rect(screen, (255, 255, 255), [100, level+20, 600, 100], width=5, border_radius=10)
    except TypeError:
        pygame.draw.rect(screen, (255, 255, 255), [100, level+20, 600, 100], 5)


    writer.print_words(screen, (255, 255, 255), words, (110, level+17))


def thread_with_return(port, results):
    results[0] = lan.send.send(port)

def get_connection(screen):
    screen.fill((0, 0, 0))
    address = get_local_address()
    port = random.randrange(1024, 65535)
    display(screen, '   back', 0)
    display(screen, 'waiting for player', 1, writer2)
    display(screen, 'your address:\n' + str(address), 2, writer2)
    display(screen, 'your port:\n' + str(port), 3, writer2)
    pygame.display.flip()
    results = [None]
    thread = Thread(target=thread_with_return, args=(port, results), daemon=True)
    thread.start()
    while thread.is_alive():
        events = pygame.event.get()
        sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in events]) else None
        if any([check_if_in([100, 20, 600, 100], event.pos) for event in events if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1]):
            fake = lan.recive.recive(get_local_address(), port)
            thread.join()
            print(results)
            results[0].close()
            fake.close()
            del results
            del fake
            return run(screen)

    return results[0]


def check_if_in(rect, location):
    w1 = rect[0]
    h1 = rect[1]
    w2 = rect[0] + rect[2]
    h2 = rect[1] + rect[3]
    if w1 <= location[0] <= w2 and h1 <= location[1] <= h2:
        return True


def run(screen):
    screen.fill((0, 0, 0))
    display(screen, '   quit', 0)
    display(screen, ' new game', 1)
    display(screen, ' join game', 2)
    pygame.display.flip()
    has_clicked = False
    while not has_clicked:
        events = pygame.event.get()
        sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in events]) else None
        events = [x for x in events if x.type == pygame.MOUSEBUTTONDOWN and x.button == 1]

        for event in events:
            loc = [100, 20, 600, 100]
            loc2 = [100, 220, 600, 100]
            loc3 = [100, 420, 600, 100]
            if check_if_in(loc2, event.pos):
                return get_connection(screen)
            elif check_if_in(loc3, event.pos):
                return run_as_guest(screen)
            elif check_if_in(loc, event.pos):
                sys.exit()




def get_adr_and_port(screen):
    screen.fill((0, 0, 0))
    address = '192.168.' # 1
    port = '' # 2
    selected = None
    enabled_keys = [pygame.K_PERIOD, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                     pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
                                     pygame.K_BACKSPACE]
    key_reference = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\b']

    while True:
        display(screen, '   back', 0)
        display(screen, 'enter address:\n'+address, 1, writer2)
        display(screen, 'enter port:\n'+port, 2, writer2)
        display(screen, '   done', 3, writer)
        pygame.display.flip()
        events = pygame.event.get()
        sys.exit() if any([event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_c and event.mod == pygame.KMOD_LCTRL) for event in events]) else None
        mouse_events = [x for x in events if x.type == pygame.MOUSEBUTTONDOWN and x.button == 1]
        key_events = [x for x in events if x.type == pygame.KEYDOWN and x.key in enabled_keys]
        all_out = False
        for m_event in mouse_events:
            if check_if_in([100, 620, 600, 100], m_event.pos):
                return address, port

            if check_if_in([100, 220, 600, 100], m_event.pos):
                selected = 1
                all_out = False

            elif check_if_in([100, 420, 600, 100], m_event.pos):
                selected = 2
                all_out = False
            elif check_if_in([100, 20, 600, 100], m_event.pos):
                return run(screen)
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
    display(screen, '   That is invalid', 0, writer2)
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
                    if 11 <= len(address) <= 15:
                        if address[:8] == '192.168.':
                            is_okay = True
                        else:
                            address, port = fail(screen)
                    else:
                        address, port = fail(screen)
                else:
                    address, port = fail(screen)
        try:
            double_socket = lan.recive.recive(address, port)
            valid_address = True
        except ConnectionRefusedError:
            screen.fill((0, 0, 0))
            display(screen, 'That is invalid (CRE)', 0, writer2)
            pygame.display.flip()
            time.sleep(1.5)
    g = lan.guest.guest(double_socket, screen)
    g.loop()
