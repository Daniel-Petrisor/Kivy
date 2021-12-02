from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


# RGB Color
Window.clearcolor =(1,0,0,0)
Window.size = (500, 600)

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=40,
                            spacing=10,
                            padding=10,
                           )

        btn1 = Button(text='Button 1.1',
                      size_hint=(None,None),
                      width=100, height=40,
                      )
        btn2 = Button(text='Button 1.2')

        btn3 = Button(text='Button 2.1',
                      size_hint=(None, None),
                      width=100, height=40,
                      )
        btn4 = Button(text='Button 2.2')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout



MainApp().run()