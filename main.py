#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:57:56 2024

@author: viktor_john
"""



from kivy.app import App
from kivy.lang import Builder



class QR_Code_Reader(App):
    
    def build(self):
        return Builder.load_string(
"""
#: import ZBarCam kivy_garden.zbarcam.ZBarCam
BoxLayout:
    orientation: "vertical"
    ZBarCam:
        id:qrcam
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: " ".join([str(symbol) for symbol in qrcam.symbols])
        
        
"""
)

    
if __name__ == "__main__":
    QR_Code_Reader().run()
