# Student Records Client-Server Application

## 1. Introduction

This project implements a simple client-server application using Python TCP sockets. The application allows a client to request student information from a server running on the same computer through localhost.

The client sends a student ID to the server. The server processes the request, retrieves the corresponding student record, and returns a JSON response to the client.

## 2. Objectives

- Implement a basic client-server application.
- Demonstrate communication between client and server components.
- Explain the layered architecture used in the application.
- Demonstrate data exchange using TCP sockets.
- Handle valid and invalid student record requests.

## 3. Technologies Used

- Programming language: Python 3
- Networking: TCP sockets
- Data format: JSON
- Network address: `127.0.0.1`
- Port: `65433`
- Version control: Git and GitHub

## 4. System Architecture

The application uses three logical layers.

### Data Access Layer

Stores the sample student records and retrieves student information using a student ID.

### Business Logic Layer

Processes incoming requests, checks whether the requested student exists, and prepares the appropriate response.

### Presentation and Network Layer

Manages TCP communication between the client and server. The client sends a request, and the server returns a JSON response.

### Communication Flow

1. The client prompts the user for a student ID.
2. The client establishes a TCP connection with the server.
3. The client sends the student ID.
4. The server receives and processes the request.
5. The server retrieves the matching record, if available.
6. The server sends a JSON response.
7. The client displays the result.

## 5. Project Structure

```text
OG_Asigmnet module 3/
├── og_client.py
├── og_server.py
├── README.md
└── screenshots/
    └── Screenshot 2026-10-12 213706.png
```

## 6. Requirements

- Python 3 installed on the computer.
- A terminal or command prompt.
- Git for version control, if contributing to the repository.

No external Python packages are required if the application uses only Python's built-in libraries.

## 7. How to Run the Application

### Step 1: Open the project directory

Open two terminal windows in the project directory.

### Step 2: Start the server

In the first terminal, run:

```bash
python og_server.py
```

The server listens on `127.0.0.1:65433` and waits for client connections.

### Step 3: Start the client

In the second terminal, run:

```bash
python og_client.py
```

### Step 4: Test the application

Enter a valid student ID supported by the application, such as `DS001`, `DS002`, or `DS003`, if these IDs are present in the server's records.

To test error handling, enter an unknown student ID such as `UNKNOWN`.

To exit, enter `exit` if supported by the client.

## 8. Testing and Results

The application can be evaluated using the following test cases.

| Test Case | Input | Expected Result |
|---|---|---|
| Valid student lookup | Existing student ID | Student record is returned. |
| Invalid student lookup | `UNKNOWN` | An error response is returned. |
| Server unavailable | Any student ID | The client reports a connection failure. |

The screenshot in the `screenshots/` directory provides visual evidence of the application's execution. The image should be reviewed to confirm which client-server interactions it demonstrates.

## 9. Advantages

- Demonstrates TCP client-server communication.
- Uses JSON for structured data exchange.
- Separates data retrieval and request processing into logical layers.
- Can be extended to support additional student management operations.

## 10. Limitations and Future Improvements

The sample student records are stored in memory. They are not persistent when the server stops.

Possible improvements include:

- Integrating a database such as SQLite or MySQL.
- Adding authentication and access control.
- Supporting student registration, updates, and deletion.
- Improving input validation and network error handling.
- Supporting multiple simultaneous clients.

## 11. Conclusion

This project demonstrates a basic client-server application implemented using Python TCP sockets in a localhost environment. It illustrates how a client sends a request, how the server processes that request through logical layers, and how a structured response is returned to the client.
