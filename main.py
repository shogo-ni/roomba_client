#-*- coding: utf-8 -*-
import socket
import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior

from kivy.properties import StringProperty, ListProperty
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.utils import platform


class TextWidget(Widget):
    text = StringProperty()  # add a property
    color = ListProperty([1,1,1,1])
    debug = StringProperty()
    command = StringProperty()

    # socket client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.0.129'  #rosnet
    # host = '10.181.61.198'  #eduroam
    port = 12000
    def connect_to_server(self):
        self.s.connect((self.host, self.port))
        data = self.s.recv(1024).decode()
        self.debug = 'Success to Connect with Roomba!'
        print(self.debug)
        
    # GUI main
    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'Waiting ...'

    def buttonClicked1(self):  # when you click the button
        self.text = 'Spin Left'
        self.color = [0,1,0,1]
        self.command = 'left'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Spin Left'

    def buttonRelease1(self):
        self.text = 'Waiting ...'
        self.color = [1,1,1,1]
        self.command = 'break'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Break'

    def buttonClicked2(self):
        self.text = 'Forward'
        self.color = [0,1,0,1]
        self.command = 'forward'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Spin Left'

    def buttonRelease2(self):
        self.text = 'Waiting ...'
        self.color = [1,1,1,1]
        self.command = 'f_break'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Break'
 
    def buttonClicked3(self):
        self.text = 'Backward'
        self.color = [0,1,0,1]
        self.command = 'backward'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Spin Left'
  
    def buttonRelease3(self):
        self.text = 'Waiting ...'
        self.color = [1,1,1,1]
        self.command = 'b_break'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Break'

    def buttonClicked4(self):
        self.text = 'Spin Right'
        self.color = [0,1,0,1]
        self.command = 'right'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Spin Left'

    def buttonRelease4(self):
        self.text = 'Waiting ...'
        self.color = [1,1,1,1]
        self.command = 'break'
        if self.debug == '':
            pass
        else:
            self.s.send(self.command.encode())
            self.debug = 'Send a command: Break'

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'Remote Roomba'

if __name__ == '__main__':
    TestApp().run()

