# socket_client.py
# networking only
import socket
import threading

_socket = None
_thread = None
_last_message = None
_running = False


def start_client(host, port):
    global _thread, _running

    if _thread and _thread.is_alive():
        return

    _running = True
    _thread = threading.Thread(
        target=_socket_worker,
        args=(host, port),
        daemon=True
    )
    _thread.start()


def stop_client():
    global _running, _socket

    _running = False
    if _socket:
        try:
            _socket.shutdown(socket.SHUT_RDWR)
            _socket.close()
        except:
            pass
        _socket = None


def _socket_worker(host, port):
    global _socket, _last_message, _running

    try:
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _socket.connect((host, port))

        while _running:
            data = _socket.recv(1024)
            if not data:
                break
            _last_message = data.decode("utf-8")

    except Exception as e:
        _last_message = f"Socket error: {e}"

    finally:
        _running = False
        if _socket:
            _socket.close()
            _socket = None


def pop_message():
    global _last_message
    msg = _last_message
    _last_message = None
    return msg
