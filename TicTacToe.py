from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from kivy.uix.layout import Layout
from random import randint
class TicTacToe (App):
   table = []
   choices =["X","O"]
   game_over = False
   combo = [
        [0,1,2], [3,4,5], [6,7,8], # Horizontal
        [0,3,6], [1,4,7], [2,5,8], # Vertical
        [0,4,8], [2,4,6]           # Diagonal
    ]
   def build(self):
      Config.set('graphics', 'width', '450')
      Config.set('graphics', 'height', '450')
      Config.set('graphics','resizable', False)
      self.layout = StackLayout()
      for i in range(9):
         bt = Button(text ='', font_size=120, width=150, height=150, size_hint=(None, None), id=str(i))
         bt.bind(on_release = self.btn_pressed)
         self.table.append(bt)
         self.layout.add_widget(bt)
      return self.layout

   def btn_pressed (self,button):
      print(int(button.id))
      print (len(button.text.strip()))
      if len(button.text.strip()) < 1:
         button.text = "X"
         ##self.checkgameover()
         ##if gameover == False:



   def checkgameover (self,button):
      #แนวนอน
      if self.table.index(0)== self.table.index(1)==self.table.index(2) and self.table.index(0)!= "":
         if self.table.index(0)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')

      if self.table.index(3)== self.table.index(4)==self.table.index(5) and self.table.index(3)!= "":
         if self.table.index(3)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')

      if self.table.index(6)== self.table.index(7)==self.table.index(8) and self.table.index(6)!= "":
         if self.table.index(6)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')
      #แนวตั้ง
      if self.table.index(0)== self.table.index(3)==self.table.index(6) and self.table.index(0)!= "":
         if self.table.index(0)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')

      if self.table.index(1)== self.table.index(4)==self.table.index(7) and self.table.index(1)!= "":
         if self.table.index(1)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')
      if self.table.index(2)== self.table.index(5)==self.table.index(8) and self.table.index(8)!= "":
         if self.table.index(0)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')
      #แนวทะแยง
      if self.table.index(0)== self.table.index(4)==self.table.index(8) and self.table.index(0)!= "":
         if self.table.index(0)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')
      if self.table.index(0)== self.table.index(1)==self.table.index(2) and self.table.index(0)!= "":
         if self.table.index(0)== "X":
            print ('You win ! <3')
         else:
            print('Bot win, Pls try again ! :)')
   def bot_play (self,button):
      r = randint(0,9)









if __name__=='__main__':
   TicTacToe().run()
