import socket
import os

def send_request(server_address, port, request):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_address, port))
        client_socket.sendall(request.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Server answer: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

def add_files_to_server(directory, server_address, port):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as f:
                content = f.read()
            send_request(server_address, port, f"ADD_FILE {content}")

def search_in_server(server_address, port, word):
    send_request(server_address, port, f"SEARCH {word}")

if __name__ == "__main__":
    add_files_to_server("pos", "127.0.0.1", 8080)
    print("All files uploaded.")

    search_in_server("127.0.0.1", 8080, "character")
