class Enemy :
    life=5
    def attack(self):
        print('ouch!')
        self.life-=1

    def check_life(self):
        if self.life <=0 :
            print('I am Dead')
        else:
            print(str(self.life)+"life left")

enemy1=Enemy()
enemy1.attack()
enemy1.check_life()
