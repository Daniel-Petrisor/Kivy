from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='This is Batman',
                      font_size='28sp',
                      bold=True,
                      italic=True
                      )
        return label


MainApp().run()
