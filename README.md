# SWEN320 2024S Password Manager

Welcome to the SWEN320 2024S Password Manager, a Flask-based web application designed for securely managing passwords. This project focuses on demonstrating encryption, data storage, and retrieval using Python dictionaries, rather than traditional databases, to keep the architecture simple and understandable.

## Features

- Secure password storage in memory using Python dictionaries.
- Password encryption and decryption for added security.
- User registration and authentication system.
- Intuitive web interface for easy password management.

## Project Structure

Below is an outline of the key directories and files in this project:

## Getting Started

### Prerequisites

- Python 3.6 or newer.
- pip for managing Python packages.

### Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ellerAvery/swen320_2024S_password_manager_EllerSnipes.git
    cd swen320_2024S_password_manager_EllerSnipes
    ```

2. **Create and Activate a Virtual Environment**

    - macOS/Linux:

        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

    - Windows:

        ```cmd
        python -m venv .venv
        .\.venv\Scripts\activate
        ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```bash
    make run
    ```

    The application will be accessible at `http://127.0.0.1:5000`.

### Using the Makefile

The included Makefile simplifies common tasks:

- **Install Dependencies**: `make install`
- **Run the Application**: `make run`
- **Run Tests**: `make test`
- **Generate Coverage Report**: `make coverage`
- **Generate HTML Coverage Report**: `make coverage_html`

## Data Persistence and Privacy

This application uses Python dictionaries for data storage, meaning all information is stored in memory. To clear session data without restarting the app, consider using an Incognito Window or Private Browsing Mode. This approach is ideal for testing or demonstration purposes.

For production use, consider integrating a database or other persistent storage solution to ensure data integrity and availability.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Authors

- [Cole Snipes](https://www.linkedin.com/in/cole-snipes/)
- Avery Eller

#### Acknowledgements

Thank you to [Dr. Chang](https://www.linkedin.com/in/hungfuaaronchang/) and [Ethan Lohman](https://github.com/Ethan-Lohman) for their guidance and support throughout this project.
