"""
Utilities for interfacing with iMotions.
"""

import socket

EVENT_RECEIVING_PORT = 8089
"""Event Receiving port for iMotions, which defaults to 8089."""

def send_event(ip, message):
    """Send an event packet over TCP to iMotions."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.25)
        sock.connect((ip, EVENT_RECEIVING_PORT))
        sock.send(bytes(message, 'utf-8'))
    except ConnectionRefusedError:
        print(f"Couldn't connect to iMotions. Is it running on {ip} port {EVENT_RECEIVING_PORT} with 'Enable event receiving' and 'Use TCP' enabled?")
    except socket.timeout:
        print(f'Timed out trying to reach iMotions on {ip}')
    except socket.error:
        print(f'Problem sending event to {ip}')

def start_scene_recording(ip, scene_name, scene_description = ''):
    send_event(ip, f'M;2;;;{scene_name};{scene_description};S;V\r\n')

def end_scene_recording(ip, scene_name):
    send_event(ip, f'M;2;;;{scene_name};;E;\r\n')
    pass