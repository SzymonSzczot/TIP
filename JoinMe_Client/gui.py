import threading
from tkinter import *
from tkinter import ttk

import requests

from client import Client
from constants import GuiVariables
from server import Server


class Gui:

    def __init__(self):
        self.root = Tk()
        self.server = None
        self.client = None

        self.server_thread = None
        self.client_thread = None
        self.stop_threads = False

        self.variables = GuiVariables()

    def run_server(self):
        self.server = Server()
        self.server.start_server()

    def run_client(self):
        self.client = Client()
        self.client.start_client()

    def server_start(self):
        self.server_thread = threading.Thread(target=self.run_server).start()

    def client_start(self):
        self.client_thread = threading.Thread(target=self.run_client).start()

    def disconnect(self):
        if self.server:
            self.server.disconnect_server()
        if self.client:
            self.client.disconnect_client()
            self.client = None

    def add_contact(self):
        ip = self.variables.ip.get()
        name = self.variables.port.get()
        requests.post("http://localhost:8000/add-contact", data={"name": name, "ip": ip})

    def gui(self):
        ip_label = ttk.Label(self.root, text="IP")
        ip_label.grid(column=0, row=2)
        port_label = ttk.Label(self.root, text="CLIENT NAME")
        port_label.grid(column=0, row=1)
        dst_port_label = ttk.Label(self.root, text="DESTINATED PORT")
        dst_port_label.grid(column=0, row=3)

        # SERVER STATUS
        status_lb = ttk.Entry(self.root, textvariable=self.variables.server_status, state=DISABLED)
        status_lb.grid(column=1, row=6)
        status_label = ttk.Label(self.root, text="SERVER STATUS")
        status_label.grid(column=0, row=6)

        # CLIENT STATUS
        status_lb = ttk.Entry(self.root, textvariable=self.variables.client_status, state=DISABLED)
        status_lb.grid(column=3, row=6, columnspan=5)
        status_label = ttk.Label(self.root, text="CLIENT STATUS")
        status_label.grid(column=2, row=6)

        # Connection
        connection_lb = ttk.Entry(self.root, textvariable=self.variables.connected_to, state=DISABLED)
        connection_lb.grid(column=1, row=7)
        connection_label = ttk.Label(self.root, text="Server connected to: ")
        connection_label.grid(column=0, row=7)

        # Disconnect
        disconnect_button = ttk.Button(self.root, text='Disconnect', command=self.disconnect)
        disconnect_button.grid(column=2, row=5, sticky=(N, W, E, S), padx=10)

        value = ttk.Entry(self.root, textvariable=self.variables.ip)
        value.grid(column=1, row=2, columnspan=4, sticky=(N, W, E, S))

        value = ttk.Entry(self.root, textvariable=self.variables.port)
        value.grid(column=1, row=1, columnspan=4, sticky=(N, W, E, S))

        value = ttk.Entry(self.root, textvariable=self.variables.destinated_port)
        value.grid(column=1, row=3, columnspan=4, sticky=(N, W, E, S))

        # BUTTON START SERVER
        edit_button = ttk.Button(self.root, text='Join network', command=self.server_start)
        edit_button.grid(column=1, row=4, sticky=(N, W, E, S), padx=10)

        # BUTTON START CLIENT
        save_button = ttk.Button(self.root, text='Connect', command=self.client_start)
        save_button.grid(column=1, row=5, sticky=(N, W, E, S), padx=10)

        send_button = ttk.Button(self.root, text='Add contact', command=self.add_contact)
        send_button.grid(column=1, row=10, sticky=(N, W, E, S), padx=10)

        self.root.mainloop()
