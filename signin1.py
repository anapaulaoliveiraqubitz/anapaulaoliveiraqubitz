from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import requests

from kivy.network.urlrequest import UrlRequest
from functools import partial

class MainApp(App):
    def build(self):
        grid = GridLayout(cols=1)
        button1 = Button(text="Normal Resquest", on_realease = self.run_request)
        button2 = Button(text="Kivy URLRequest", on_release = self.run_UrlRequest)
        blank_button = Button("Click test")
        grid.add_widget(button1)
        grid.add_widget(button2)
        grid.add_widget(blank_button)
        return grid

    def run_request(self, **args):
        for i in range(1):
            i = requests.get("https://google.com")
            print(i)
    
    def run_UrlRequest(self, **args):
        for i in range(1):
            self.r = UrlRequest("", on_success=partial(self.label, i))

    def update_label(self, i, **args):
        print(i)

if __name__ == "__main__":
    test = MainApp()
    test.run()

