import kivy
kivy.require('2.0.0')

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (400, 600)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Demo'
                        right_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 8
                    
                    Widget:

                    MDLabel:
                        text: 'Hello World'
                        halign: 'center'

                    MDBottomAppBar:
                        MDToolbar:
                            title: 'Help'
                            left_action_items: [["coffee", lambda x: nav_drawer.toggle_nav_drawer()]]
                            mode: 'end'
                            type: 'bottom'
                            icon: 'language-python'
                            on_action_button: 
    MDNavigationDrawer:
        id: nav_drawer

"""



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'LightBlue'
        screen = Builder.load_string(navigation_helper)
        return screen




MainApp().run()