from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button


# RGB Color
Window.clearcolor =(1,0,0,0)

class MainApp(App):
    def build(self):
        label = Label(text='This is Batman',
                      font_size='28sp',
                      bold=True,
                      italic=True
                      )
        return label

        button = Button(text='Print',
                        size_hint=(0.2,0.1),
                        font_size='20sp',
                        pos_hint={'center_x': 0.5, 'center_y': 0.2},
                        on_press=self.print_press,
                        on_release=self.print_release,
                        )
        return button

    def print_press(self,obj):
        print('Button has been pressed')

    def print_release(self,obj):
        print('Button has been released')


MainApp().run()
