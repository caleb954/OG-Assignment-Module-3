
import socket
import json

HOST = "127.0.0.1"
PORT = 65433


def request_student(student_id):
    """Send a student ID to the server and display its response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(5)
            client.connect((HOST, PORT))
            client.sendall(student_id.encode("utf-8"))

            response = client.recv(4096)
            result = json.loads(response.decode("utf-8"))

        print("\n--- STUDENT LOOKUP RESULT ---")

        if result["status"] == "success":
            student = result["data"]
            print(f"Name:   {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Year:   {student['year']}")
        else:
            print(f"Error: {result['message']}")

    except ConnectionRefusedError:
        print("Cannot connect. Start server.py first.")
    except (OSError, json.JSONDecodeError, KeyError) as error:
        print(f"Communication error: {error}")


if __name__ == "__main__":
    print("STUDENT RECORDS CLIENT")

    while True:
        student_id = input(
            "\nEnter student ID (DS001, DS002, DS003) "
            "or 'exit': "
        ).strip()

        if student_id.lower() == "exit":
            print("Client closed.")
            break

        if student_id:
            request_student(student_id)

