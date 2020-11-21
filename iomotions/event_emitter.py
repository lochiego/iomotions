from enum import Enum, auto
import socket

class Protocol(Enum):
	TCP = auto()
	UDP = auto()
		

class EventEmitter:

	def __init__(self, ip='localhost', port=8089, protocol=Protocol.TCP):
		self.ip = ip
		self.port = port
		self.protocol = protocol
		
	def _send_event_tcp(self, event: str):
		ip = self.ip
		port = self.port
		
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(1.25)
			sock.connect((ip, port))
			sock.send(bytes(event, 'utf-8'))
		except ConnectionRefusedError:
			print(f"Could not connect to iMotions running at {ip} port {port}")
		except socket.timeout:
			print(f'iMotions not listening on {ip}')
		except socket.error:
			print(f'Problem sending event to {ip}')


	def _send_event_udp(self, event: str):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(1.25)
		sock.sendto(bytes(event, 'utf-8'), (self.ip, self.port))

	def _send_event(self, event: str):
		if self.protocol == Protocol.TCP:
			self._send_event_tcp(event)
		else:
			self._send_event_udp(event)
			