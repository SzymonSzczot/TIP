import json
import socket
import threading
import time

import pyaudio
import requests

from JoinMe_Client import constants
from JoinMe_Client.constants import audio_format, chunk_size, channels, rate, bcolors


class Client:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_audio = pyaudio.PyAudio()

        self.playing_stream = self.client_audio.open(
            format=audio_format, channels=channels, rate=rate, output=True,
            frames_per_buffer=chunk_size
        )

        self.recording_stream = self.client_audio.open(
            format=audio_format, channels=channels, rate=rate,
            input=True,
            frames_per_buffer=chunk_size
        )

        self.stop_threads = False
        self.receive_thread = None
        self.send_thread = None

        self.variables = constants.GuiVariables()

    def start_client(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if self.establish_connection():
                self.start_communication()
        except Exception:
            print("Couldn't connect to server")

    def establish_connection(self):
        ip = self.translate_name_to_ip()
        if ip:
            return self.connect(ip)
        else:
            return self.try_connecting_to_given_ip()

    def connect(self, target_ip):
        answer = self.handshake(target_ip)
        if answer == constants.ACCEPTED:
            self.variables.client_status.set("Client connected to " + target_ip)
            return True
        else:
            return False

    def try_connecting_to_given_ip(self):
        return self.connect(self.variables.ip.get())

    def translate_name_to_ip(self):
        response = requests.get("http://localhost:8000/contact", params={"ip": self.variables.ip.get()})
        response = json.loads(response.content)
        ip = response.get("ip")

        return ip

    def handshake(self, target_ip):
        target_port = int(self.variables.destinated_port.get())
        self.client_socket.connect((target_ip, target_port))
        self.client_socket.send(constants.INVITE)
        return self.client_socket.recv(100)

    def start_communication(self):
        self.receive_thread = threading.Thread(target=self.receive_server_data)
        self.send_thread = threading.Thread(target=self.send_data_to_server)

        print(bcolors.OKBLUE + "Connection established" + bcolors.ENDC)

        self.receive_thread.start()
        self.send_thread.start()

    def receive_server_data(self):
        while not self.stop_threads:
            self.receive_and_play()

    def receive_and_play(self):
        data = self.client_socket.recv(20000)
        self.playing_stream.write(data)

    def send_data_to_server(self):
        while not self.stop_threads:
            self.send_and_record()

    def send_and_record(self):
        data = self.recording_stream.read(20000)
        self.client_socket.send(data)
        time.sleep(0.01)

    def disconnect_client(self):
        self.client_socket.send(constants.CLOSE)
        self.client_socket.close()
        self.client_socket = None
        self.receive_thread.join()
        self.send_thread.join()
        print(bcolors.FAIL + "Client disconnected" + bcolors.ENDC)
