#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random


class Card:
    def __init__(self, mark, number):
        self.mark = mark
        self.number = number
        img_path = './trump/png/'+ mark + str(number) + '.png'
        img = pygame.image.load(img_path)
        self.img = pygame.transform.rotozoom(img, 0, 0.5)
        self.x = 0
        self.y = 500
        self.clickcount = 0

    def make_dack(): #トランプの情報を作成
        marks = ['c', 'd', 'h', 's']
        numbers = []
        for i in range(1, 14):
            numbers.append(i)

        deck = [] #トランプの全情報を格納
        for mark in range(4):
            for num in range(13):
                card = Card(marks[mark], numbers[num])
                deck.append(card)

        random.shuffle(deck) #全情報をシャッフル

        #情報のデバッグ用
        """ for i in range(len(deck)): # シャッフル確認
            print(deck[i].mark, deck[i].number)
                """
        return deck
