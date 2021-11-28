from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage

# RGB Color
Window.clearcolor =(1,0,0,0)
Window.size = (400, 600)

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                           spacing=10,
                           padding=40,
                           )

        label = Label(text='This is Batman',
                      font_size='28sp',
                      bold=True,
                      italic=True
                      )
        #return label

        button = Button(text='Print',
                        pos_hint={'center_x': 0.5, 'center_y': 0.2},
                        size_hint=(None,None),
                        width=100,
                        height=50,
                        font_size='20sp',
                        on_press=self.print_press,
                        on_release=self.print_release,
                        #size_hint=(0.2, 0.1),
                        )
        #return button

        img = Image(source='img/cute.png')
        #img_async = AsyncImage(source='https://cdn141.picsart.com/261930348032212.png?to=crop&type=webp&r=1000x1000&q=95')
        # return img_async

        layout.add_widget(label)
        layout.add_widget(img)
        layout.add_widget(button)

        return layout

    def print_press(self,obj):
        print('Button has been pressed')

    def print_release(self,obj):
        print('Button has been released')


MainApp().run()
