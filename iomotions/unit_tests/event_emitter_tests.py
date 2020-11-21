#from unittest import TestCase, TestSuite, TestLoader, TextTestRunner, mock
import unittest
from unittest.mock import Mock, patch
from ..event_emitter import EventEmitter, Protocol, socket

class TestEventHandlerSetup(unittest.TestCase):

    def test_constructor(self):
        self.assertIsNotNone(EventEmitter)

    def test_default_network_interaction(self):
        emitter = EventEmitter()
        self.assertEqual(emitter.ip, 'localhost')
        self.assertEqual(emitter.port, 8089)
        self.assertEqual(emitter.protocol, Protocol.TCP)

    def test_constructor_overrides(self):
        emitter = EventEmitter(ip="192.168.0.1", port=8412, protocol=Protocol.UDP)
        self.assertEqual(emitter.ip, "192.168.0.1")
        self.assertEqual(emitter.port, 8412)
        self.assertEqual(emitter.protocol, Protocol.UDP)

class TestSendBehavior(unittest.TestCase):

    @patch.object(socket, 'socket')
    def test_send_tcp(self, mock_socket):
        mock_sock = Mock()
        mock_socket.return_value = mock_sock

        emitter = EventEmitter()
        emitter._send_event('garbage')
        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_sock.connect.assert_called()
        mock_sock.send.assert_called()

    @patch('socket.socket')
    def test_send_udp(self, mock_socket):
        mock_sock = Mock()
        mock_socket.return_value = mock_sock
        
        emitter = EventEmitter(ip="192.168.0.1", port=8412, protocol=Protocol.UDP)
        emitter._send_event('garbage')
        mock_socket.assert_called_with(socket.AF_INET, socket.SOCK_DGRAM)
        mock_sock.sendto.assert_called_with(bytes('garbage', 'utf-8'), ("192.168.0.1", 8412))

constructor_suite = unittest.TestLoader().loadTestsFromTestCase(TestEventHandlerSetup)
send_suite = unittest.TestLoader().loadTestsFromTestCase(TestSendBehavior)

test_suite = unittest.TestSuite([constructor_suite, send_suite])
unittest.TextTestRunner(verbosity=2).run(test_suite)
