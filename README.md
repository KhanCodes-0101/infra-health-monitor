# IT Infrastructure Health Monitor #

A Python-based project that monitors system resource usage, checks website availability, and records infrastructure incidents.

## Features

- **CPU Monitoring:** Checks CPU usage.
- **Memory Monitoring:** Tracks memory usage.
- **Disk Monitoring:** Checks disk usage.
- **Website Availability:** Checks whether a website is reachable.
- **Incident Logging:** Records warnings and critical incidents in a JSON file.
- **Incident Report:** Displays recorded incidents in the terminal.
- **Desktop GUI:** Provides a simple interface built with Tkinter to view system usage and check website availability.

## Technologies Used

- Python
- psutil
- Requests
- JSON
- Tkinter

## Project Structure

```text
infra-health-monitor/
├── main.py
├── gui.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/infra-health-monitor.git
   ```

2. Open the project folder:

   ```bash
   cd infra-health-monitor
   ```

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

**Terminal version**

```bash
python main.py
```

**Desktop GUI**

```bash
python gui.py
```

## How It Works

The application checks CPU, memory, and disk usage and classifies resource usage as NORMAL, WARNING, or CRITICAL based on predefined thresholds. It also checks website availability and records detected incidents with timestamps.

The terminal version displays an incident report using saved records. The GUI displays system usage and provides a button to check website availability.

## Learning Outcomes

- Working with Python libraries
- Monitoring system resources
- Making HTTP requests
- Reading and writing JSON data
- Handling exceptions

## Author

Developed as a Python project to explore IT infrastructure monitoring and incident logging.
