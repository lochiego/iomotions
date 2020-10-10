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
        print(f"Could not connect to iMotions running at {ip} port {EVENT_RECEIVING_PORT}")
    except socket.timeout:
        print(f'iMotions not listening on {ip}')
    except socket.error:
        print(f'Problem sending event to {ip}')
