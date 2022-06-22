import re
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from pytube import YouTube
from kivymd.uix.card import MDCard
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.uix.image import AsyncImage
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
KV = '''
MDScreen:
    MDCard:
        size_hint_x:.9
        size_hint_y:.4
        pos_hint: {"center_x": .5, "center_y": .5}
    MDTextField:
        id:yttxt
        text:''
        hint_text: "Youtube Link"
        pos_hint: {"center_x": .5, "center_y": .5}        
        size_hint_x:.8

    MDRectangleFlatButton:
        text: "CONVERT"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        pos_hint: {"center_x": .5, "center_y": .4}
        on_press:app.redex(yttxt.text)
    AsyncImage:
        id:img
        size_hint:[0.9,0.2]
        
        source:''
    
    

    MDLabel:
        id:lb
        text:''
        font_size:20
        pos_hint:{"center_x":0.5,"center_y":0.7}
        size_hint:[0.9,0.2]
    MDLabel:
        name:"lbl"
        id:lbl
        text:'Youtube downloader'
        font_size:50
        pos_hint:{"center_x":.7, "center_y":.9}


'''



class TestCard(MDApp):
    def build(self):
        return Builder.load_string(KV)


    def data(self,thumb, title):
        if thumb and title is not None:
            self.root.ids.lb.text = title
            self.root.ids.img.source = thumb

        else:
            print('unscuess')
    


    def redex(self, url):
        pattern = "(http(s|):\/\/|)(www.|)youtube.(com|nl)\/watch\?v\=([a-zA-Z0-9-_=]+)"
        if(re.search(pattern, url)):
            yt = YouTube(url)
            self.data(yt.thumbnail_url, yt.title)
        else:
            print('un')

TestCard().run()


    def onprogress(self,stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 
        liveprogress = (int)(bytes_downloaded / total_size * 100)
        live = "downloading... {pro}".format(pro = liveprogress)
        print(live)
    
    def oncomplete(self,stream, chunk):
        print("downloaded...")
    