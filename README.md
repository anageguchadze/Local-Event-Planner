# Django Event Management Application

This project is a simple Django-based web application that allows users to manage events. Users can add new events, view a list of existing events, and see the details of each event.

## Features

- **View Events**: Display a list of all the events saved in the system.
- **Event Details**: View the details of a specific event, including title, description, date, and location.
- **Add Event**: Add new events to the system by providing a title, description, date, and location.

## Models

1. **Event**:
   - `title`: The name or title of the event (maximum 100 characters).
   - `description`: A brief description of the event (maximum 300 characters).
   - `date`: The date of the event (as a string, e.g., "2024-10-25").
   - `location`: The location where the event will take place.

## Installation and Setup

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment (recommended)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Local-Event-Planner
