class person_class:
    def __init__(self, name = 'guest'):
        self.name = name
        self.cards = []
        self.cards_up = []
        self.turn = False
    
    def start_phase():
        print('大富豪を始めます')
        #開発中は２人で固定
        #while True:
        #    person_num = int(input('プレイヤーの人数を入力(2~4):'))
        person_num = 2
        #    if 2 <= person_num and person_num <=4:
        #        break
        player = []
        for i in range(person_num):
            #name = Player(input('Playerの名前を入力'))
            #player.append(name)
            player.append(person_class())
        
        return player

