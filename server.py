import socket
import threading
import time
import tkinter as tk
from tkinter import ttk

import pyaudio

import constants
from constants import bcolors, \
    audio_format, channels, rate, chunk_size


class Server:

    def __init__(self):
        self.server_audio = pyaudio.PyAudio()

        self.playing_stream = self.server_audio.open(
            format=audio_format, channels=channels, rate=rate, output=True,
            frames_per_buffer=chunk_size
        )

        self.recording_stream = self.server_audio.open(
            format=audio_format, channels=channels, rate=rate, input=True,
            frames_per_buffer=chunk_size
        )

        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        self.port = None

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.default_port = 6000
        self.server_started = False

        self.handle_client = None
        self.client = None
        self.receive_from_client_thread = None
        self.send_to_client_thread = None

        self.variables = constants.GuiVariables()

        self.popup = None

    def accept(self):
        self.server_socket.send(constants.ACCEPT)
        self.server_started = True
        self.popup.destroy()

    def decline(self):
        self.server_socket.send(constants.DECLINE)
        self.popup.destroy()

    def raise_popup(self, msg):
        self.popup = tk.Tk()
        self.popup.wm_title("New connection")
        label = ttk.Label(self.popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        accept_button = ttk.Button(self.popup, text="Accept", command=self.accept)
        accept_button.pack()
        decline_button = ttk.Button(self.popup, text="Decline", command=self.decline)
        decline_button.pack()
        button_close = tk.Button(self.popup, text="Close", command=self.decline)
        button_close.pack(fill='x')
        self.popup.mainloop()

    def start_server(self):
        if self.input_port_is_valid():
            self.open_connections()
        else:
            print(bcolors.FAIL + "Couldn't bind to that port. Searching for free port" + bcolors.ENDC)
            self.variables.port.set(self.default_port)
            time.sleep(2)
            self.start_server()

        self.accept_connection()

    def open_connections(self):
        self.variables.server_status.set("Połączony")
        print(bcolors.WARNING + bcolors.UNDERLINE + f"Połączono\n" + bcolors.ENDC +
              bcolors.BOLD + f"IP: {self.ip}\nPort: {self.port}" + bcolors.ENDC)

    def input_port_is_valid(self):
        if self.variables.port.get():
            self.port = self.variables.port.get()
            return True
        else:
            print(bcolors.FAIL + "The entered port is invalid. Try again" + bcolors.ENDC)
            return False

    def accept_connection(self):
        self.server_socket.listen(100)

        print(bcolors.OKGREEN + "Accepting new connections on:" + bcolors.ENDC)
        print(bcolors.BOLD + "IP: " + self.ip + bcolors.ENDC)
        print(bcolors.BOLD + "Port: " + str(self.port) + bcolors.ENDC)

        client, addr = self.server_socket.accept()
        if addr:
            inviting_message = client.recv(100)
            if inviting_message == constants.INVITE:
                self.raise_popup(f"{addr} is calling")

        if self.server_started:
            self.variables.connected_to.set(addr)
            self.handle_client = threading.Thread(target=self.handle_client, args=(client, addr,)).start()
        else:
            self.accept_connection()

    def handle_client(self):
        print(bcolors.OKBLUE + "Handling new connection" + bcolors.ENDC)
        self.receive_from_client_thread = threading.Thread(target=self.receive).start()
        self.send_to_client_thread = threading.Thread(target=self.send).start()

    def receive(self):
        while 1:
            if self.server_started:
                data = self.client.recv(20000)
                self.playing_stream.write(data)

    def send(self):
        while 1:
            if self.server_started:
                send_data = self.recording_stream.read(20000, exception_on_overflow=False)
                self.client.send(send_data)
                time.sleep(0.01)

    def disconnect_server(self):
        self.server_socket.close()
        print(bcolors.FAIL + "Server disconnected" + bcolors.ENDC)
        self.variables.connected_to.set("Not connected")
        self.server_started = False
