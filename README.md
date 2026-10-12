# Student Records Client-Server Application

## 1. Introduction

This project implements a simple client-server application using Python socket programming. The application allows a client to request student information from a server running on the same computer (localhost).

The client sends a student ID to the server, and the server processes the request, retrieves the corresponding student record, and returns the result to the client in JSON format.

## 2. Objectives

- To design and implement a client-server application.
- To demonstrate communication between client and server components.
- To implement a layered architecture.
- To demonstrate successful data exchange using TCP sockets.
- To handle valid and invalid student record requests.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Networking:** TCP sockets
- **Data Format:** JSON
- **Environment:** Localhost (`127.0.0.1`)
- **Version Control:** Git and GitHub

## 4. System Architecture

The application uses a layered architecture consisting of three logical layers.

### Layer 1: Data Access Layer

This layer stores the sample student records and retrieves student information using a student ID.

### Layer 2: Business Logic Layer

This layer processes the request, checks whether the requested student exists, and prepares an appropriate response.

### Layer 3: Presentation and Network Layer

This layer manages client-server communication through TCP sockets. The client sends a request, and the server returns a JSON response.

### Communication Flow

1. The client prompts the user to enter a student ID.
2. The client establishes a TCP connection to the server.
3. The client sends the student ID.
4. The server receives and processes the request.
5. The server retrieves the matching student record, if available.
6. The server sends a JSON response to the client.
7. The client displays the returned information or an error message.

## 5. Project Structure

```text
OG_Asigmnet module 3/
├── client.py
├── server.py
├── README.md
└── screenshots/
    ├── successful-lookup.png
    ├── invalid-lookup.png
    └── server-communication.png
```

## 6. Requirements

- Python 3 installed on the computer.
- A terminal or command prompt.
- Git installed for version control and GitHub submission.

No external Python packages are required because the application uses built-in Python libraries.

## 7. How to Run the Application

### Step 1: Open the project directory

Open a terminal and navigate to the project folder.

### Step 2: Start the server

Run the following command in the first terminal:

```bash
python server.py
```

The server starts listening on `127.0.0.1:65433` and waits for client connections.

### Step 3: Start the client

Open a second terminal in the same project directory and run:

```bash
python client.py
```

### Step 4: Test the application

Enter one of the available student IDs:

- `DS001`
- `DS002`
- `DS003`

The client should display the corresponding student information.

To test error handling, enter an unknown student ID such as `UNKNOWN`. The application should display an appropriate error message.

To exit the client, enter:

```text
exit
```

## 8. Testing and Results

The application can be tested using the following cases.

| Test Case              | Input          | Expected Result                         |
| ---------------------- | -------------- | --------------------------------------- |
| Valid student lookup   | `DS001`        | Student information is displayed.       |
| Valid student lookup   | `DS002`        | Student information is displayed.       |
| Valid student lookup   | `DS003`        | Student information is displayed.       |
| Invalid student lookup | `UNKNOWN`      | An error message is displayed.          |
| Server unavailable     | Any student ID | The client displays a connection error. |

The screenshots in the `screenshots/` directory provide visual evidence of the actual application execution and client-server communication.

## 9. Advantages of the System

- Demonstrates practical client-server communication.
- Uses TCP to provide reliable, ordered data delivery.
- Separates data retrieval and request processing into logical layers.
- Uses JSON for structured responses.
- Handles unknown student IDs and connection failures.
- Can be extended to use a database and support additional operations.

## 10. Limitations and Future Improvements

The current implementation stores sample student records in memory. The records are lost when the server program stops.

Possible improvements include:

- Integrating a database such as SQLite or MySQL.
- Adding authentication and access control.
- Supporting student registration, updating, and deletion.
- Improving input validation and network error handling.
- Extending the server to handle multiple clients concurrently.

## 11. Conclusion

The project demonstrates the implementation of a basic client-server application using Python TCP sockets on a localhost environment. It shows how a client sends a request, how the server processes that request through logical layers, and how the server returns a structured response.

The application fulfils the core practical objectives of demonstrating client-server interaction, layered architecture, and successful communication between system components.
