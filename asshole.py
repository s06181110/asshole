import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_p
import sys

from person import Person
from trump import Card

def add_cards(player, deck): #プレイヤーにカード振り分け
    for i in range(52): #トランプを配る
        player[i%len(player)].cards.append(deck.pop(0))
    
    for i in range(len(player)): #全員の手札の確認
        player[i].cards = sorted(player[i].cards, key=lambda u: u.number)
        hands_open(player[i])

def hands_open(player): #ターミナル場で手札を表示
    print('=================')
    print(player.name, 'の手札')
    for i in range(len(player.cards)):
        print(player.cards[i].mark, player.cards[i].number)  

def show_hand(screen, player): #グラフィックスでカードを表示
    card_width = 600/len(player.cards)
    pos_x = 0
    for i in range(len(player.cards)):
        player.cards[i].x = pos_x
        if player.cards[i].clickcount == 1: #クリックの回数でカード位置を変更する
            player.cards[i].y = 450
        else:
            player.cards[i].y = 500
        screen.blit(player.cards[i].img, (player.cards[i].x, player.cards[i].y))
        pos_x += card_width

def show_field(screen, field):
    card_width = 500/len(field) #カードの幅
    pos = 50
    for i in range(len(field)):
        field[i].y = 100
        field[i].x = pos
        screen.blit(field[i].img, (field[i].x, field[i].y))
        pos += card_width

def select_card(mouse_x, mouse_y, player, field, turn): #手札を上にあげる関数
    card_width = 600/len(player.cards) #カードの幅
    point1 = 0 #始点
    point2 = card_width #終点
    for i in range(len(player.cards)):
        if point1 < mouse_x < point2 and mouse_y >= 500: #左から何番目のカードが押されたか
            if player.cards[i].clickcount == 0:          #押されていなかった場合
                player.cards_up.append(player.cards[i])
                player.cards_up = list(set(player.cards_up)) #同じオブジェクトを保存しないように
                player.cards[i].clickcount = 1
            else:                                        #2回目のクリックの場合             
                turn = put_card(field, player, turn)
        elif mouse_y <= 450:
            player.cards[i].clickcount = 0
            player.cards_up.clear()
        point1 = point2
        point2 += card_width
    return turn

def put_card(field, player, turn):
    tmp = []
    if put_judge(field, player):
        turn += 1
        field.clear() #初期化
        for i in range(len(player.cards)):   #手札からフィールドへ移行させる
            if player.cards[i].clickcount == 1:
                field.append(player.cards[i])
            else:
                tmp.append(player.cards[i])
        player.cards = tmp
        player.cards_up.clear()
    hands_open(player)
    return turn

def put_judge(field, p):
    #fieldが2の場合はあらかじめ流すものとして考える
    for i in range(len(p.cards_up)-1): #プレイヤがあげている数字は合っているか
        if p.cards_up[i].number != p.cards_up[i+1].number:
            return False
    print("1")
    if len(field) == 0: #場に何もないなら出せる
        return True
    print("2")
    if not len(p.cards_up) == len(field): #枚数が合わない
        return False
    print("3")
    if p.cards_up[0].number <= field[0].number: #fieldとの数字を比べる
        if p.cards_up[0].number == 1 or p.cards_up[0].number == 2:
            return True
        else:
            return False
    print("4")
    return True

def turn_overcheck(persons, turn):
    if turn == len(persons):
        turn = 0
    return turn 

def main():
#====ゲーム前の初期設定=================

    deck = Card.make_dack()
    persons = Person.start_phase()
    add_cards(persons, deck)
    field = [] #トランプを出す場

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("大富豪")
    pygame.display.update()
    end_game = False
    turn = 0


#=====ゲーム表示================

    while not end_game:
        screen.fill((0, 255, 0))

        turn = turn_overcheck(persons, turn)
        player = persons[turn]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                end_game = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                turn = select_card(x, y, player, field, turn)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    turn += 1
                    field.clear()
        
        show_hand(screen, player)
        if len(field) != 0:
            show_field(screen, field)
            if field[0].number == 2:
                turn -= 1
                field.clear()
        
        pygame.display.flip()
    sys.exit(0)



if __name__ == '__main__':
    main()