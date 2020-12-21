import json

from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy_garden.zbarcam import ZBarCam
from pyzbar.pyzbar import ZBarSymbol

# Remove the comment before apk build
#from android.permissions import request_permissions, Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA, Permission.INTERNET])

store = JsonStore('settings.json')

KV = '''
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
Screen:

    NavigationLayout:

        ScreenManager:
            id: manager

            MainScreen:
            SettingsScreen:
            InfoScreen

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'logo.png'

                MDLabel:
                    text: "KivyMD Bilerplate App"
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "V0.1.0"
                    font_style: 'Subtitle2'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:

                    MDList:
                        OneLineIconListItem:
                            text: 'Scanner'
                            on_press:
                                root.ids.nav_drawer.set_state("close") 
                                root.ids.manager.current = 'main'
                            IconLeftWidget:
                                icon: 'qrcode-scan'
                            
                        OneLineIconListItem:
                            text: 'Settings'
                            on_press:
                                root.ids.nav_drawer.set_state("close") 
                                root.ids.manager.current = 'settings'
                            IconLeftWidget:
                                icon: 'settings'
                            
                        OneLineIconListItem:
                            text: 'App Info'
                            on_press:
                                root.ids.nav_drawer.set_state("close")
                                root.ids.manager.current = 'info'
                            IconLeftWidget:
                                icon: 'information'
                            
                
<MainScreen>
    name: 'main'
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Boilerplate Scanner"
            elevation: 10
            left_action_items: [['menu', lambda x: root.parent.parent.children[0].set_state("open")]]
        
        BoxLayout:
            orientation: 'vertical'
            id: qrbox
            
            MDLabel:
                id: scannerlabel
                text: "Scan something"
                halign: "center"

    MDFloatingActionButton:
        id: scanneractionbutton
        icon: "qrcode-scan"
        elevation_normal: 10
        #user_font_size: "32sp"
        pos_hint: {"center_x": .5, "center_y": .1}
        md_bg_color: app.theme_cls.primary_color
        on_release:
            root.toggleQRscanner()


<SettingsScreen>
    switchTestMode: switchTestMode

    name: 'settings'
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Boilerplate Settings"
            elevation: 10
            left_action_items: [['menu', lambda x: root.parent.parent.children[0].set_state("open")]]
        
        MDGridLayout:
            cols: 2
            padding: dp(20)
            adaptive_height: True
            #md_bg_color: app.theme_cls.primary_color

            TwoLineListItem:
                text: "Setting"
                secondary_text: "Toggle switch"
                #halign: 'center'
                #pos_hint: {'center_x': .5, 'center_y': .5}

            MDSwitch:
                id: switchTestMode
                active: root.testModus


        Widget:

        MDGridLayout:
            cols: 2
            padding: dp(20)
            spacing: dp(20)
            adaptive_height: True
            #md_bg_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                text: "Save"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_color
                on_release: 
                    root.save_settings()
                    root.manager.current = 'main'

            MDRectangleFlatButton:
                text: "Cancel"
                on_release: 
                    root.manager.current = 'main'



<InfoScreen>
    name: 'info'
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: "Boilerplate- Info"
            elevation: 10
            left_action_items: [['menu', lambda x: root.parent.parent.children[0].set_state("open")]]
        
        BoxLayout:
            orientation: 'vertical'

            MDLabel:
                text: "Boilerplate Scanner App"
                halign: 'center'
                font_style: 'H5'
                height: self.texture_size[1]

            MDCard:
                orientation: "vertical"
                padding: "20dp"
                #size_hint: None, None
                #size: "280dp", "180dp"
                #pos_hint: {"center_x": .5, "center_y": .5}

                MDLabel:
                    text: "Version: V0.1.0"
                    height: self.texture_size[1]
                
                MDLabel:
                    text: "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
                    height: self.texture_size[1]

            ScrollView:

                MDList:

                    TwoLineIconListItem:
                        text: "Boilerplate Contact"
                        secondary_text: "foo@bar.com"

                        IconLeftWidget:
                            icon: "email"


<QrScanner>
    qrcontent: zbarcam

    id: zbarcam
    # optional, by default checks all types
    code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
    on_symbols: root.readqrcontent(zbarcam)
                            
'''

class MainScreen(Screen):
    __qrscanner = None
    __scannerOn = False

    def toggleQRscanner(self):
        if self.__scannerOn:
            self.stopQRscanner()
            self.__scannerOn = False
            self.ids.scanneractionbutton.icon = "qrcode-scan"
        else:
            self.startQRscanner()
            self.__scannerOn = True
            self.ids.scanneractionbutton.icon = "stop"

    def startQRscanner(self):
        if any(isinstance(i, QrScanner) for i in self.ids.qrbox.children):
            for child in self.ids.qrbox.children:
                if isinstance(child, QrScanner):
                    child.startqr(child)
                    self.ids.scannerlabel.text = "Boilerplate Scan"
        else:
            self.__qrscanner = QrScanner()
            self.__qrscanner.startqr(self.__qrscanner)
            self.ids.qrbox.add_widget(self.__qrscanner, index=1)
            self.ids.scannerlabel.text = "Boilerplate Scan"

    def stopQRscanner(self):
        self.__qrscanner.stopqr(self.__qrscanner)
        

class SettingsScreen(Screen):
    switchTestMode = ObjectProperty(active=True)
    testModus = BooleanProperty(store.get('mode')['dev'])

    def save_settings(self):
        print(self.switchTestMode.active)
        store.put('mode', dev=self.switchTestMode.active)
        print("saved settings")


class InfoScreen(Screen):
    pass


class QrScanner(ZBarCam):
    qrcontent = ObjectProperty(None)
    scannerResultText = ObjectProperty(None)


    def startqr(self, instance):
        self.start()
    
    def stopqr(self, instance):
        self.stop()

    def readqrcontent(self, instance):
        qrcontent = ', '.join([str(symbol.data) for symbol in self.qrcontent.symbols])
        qr_data = qrcontent[2:-1]

        self.parent.children[0].text = qr_data


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(InfoScreen(name='info'))


class BoilerplateApp(MDApp):
    global app_root

    def build(self):
        app_root = self.root
        return Builder.load_string(KV)

    def on_start(self):
        pass

BoilerplateApp().run()
