
import socket
import json

HOST = "127.0.0.1"
PORT = 65433

# LAYER 1: DATA ACCESS LAYER
STUDENT_RECORDS = {
    "DS001": {
        "name": "Alex Morgan",
        "course": "Data Science",
        "year": 2
    },
    "DS002": {
        "name": "Jamie Taylor",
        "course": "Computer Science",
        "year": 1
    },
    "DS003": {
        "name": "Sam Lee",
        "course": "Information Technology",
        "year": 3
    }
}


def find_student(student_id):
    """Retrieve a student record using its ID."""
    return STUDENT_RECORDS.get(student_id)


# LAYER 2: BUSINESS LOGIC LAYER
def process_request(student_id):
    """Validate the request and prepare the response."""
    student = find_student(student_id)

    if student is not None:
        return {
            "status": "success",
            "message": "Student record found.",
            "data": student
        }

    return {
        "status": "error",
        "message": f"No student found with ID {student_id}."
    }


# LAYER 3: PRESENTATION / NETWORK LAYER
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print("STUDENT RECORDS SERVER")
        print(f"Listening on {HOST}:{PORT}")
        print("Waiting for client requests...")

        try:
            while True:
                connection, address = server.accept()

                with connection:
                    print(f"\nClient connected: {address}")

                    request = connection.recv(1024)

                    if not request:
                        continue

                    student_id = request.decode("utf-8").strip()
                    print(f"Requested student ID: {student_id}")

                    response = process_request(student_id)
                    encoded_response = json.dumps(response).encode("utf-8")

                    connection.sendall(encoded_response)
                    print(f"Response status: {response['status']}")
                    print("Response sent successfully.")

        except KeyboardInterrupt:
            print("\nServer shutting down.")


if __name__ == "__main__":
    start_server()
