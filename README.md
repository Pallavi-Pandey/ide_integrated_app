# Flask Integrated IDE

A custom-built, full-stack online IDE powered by Python and Flask, allowing for server-side code execution.

## Project Structure

- `app.py`: Flask backend logic for executing code via the `subprocess` module.
- `templates/`: HTML templates for the frontend interface.

## Key Features
- **Server-side Execution**: Code is executed on the hosting server, providing more control over the runtime environment.
- **Real-time Feedback**: Seamlessly communicates with the backend to display output.

## Getting Started

1.  **Install Flask**:
    ```bash
    pip install flask flask-socketio
    ```
2.  **Run the Server**:
    ```bash
    python app.py
    ```