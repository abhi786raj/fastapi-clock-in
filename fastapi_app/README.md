# Clock-In Records API

## Description

This project is a RESTful API built with FastAPI to manage user clock-in records. It includes features for CRUD operations for clock-in records, allowing users to clock in, update, delete, and filter records based on specified criteria.

## Technologies Used

- **FastAPI** 0.95.1
- **Pydantic** 2.x
- **Motor** (for asynchronous MongoDB operations)
- **MongoDB**
- **Python** 3.11

## Setup

### Prerequisites

- Python 3.11
- MongoDB

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd your_repository
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Set up environment variables:**

   - Create a `.env` file in the project root and add your MongoDB URI:

     ```env
     MONGO_URI=your_mongodb_uri
     ```

7. **Run the development server:**

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Clock-In Records
- **Create Clock-In Record:** `POST /clock-in/`
- **Get Clock-In Record by ID:** `GET /clock-in/{id}/`
- **Update Clock-In Record:** `PUT /clock-in/{id}/`
- **Delete Clock-In Record:** `DELETE /clock-in/{id}/`
- **Filter Clock-In Records:** `GET /clock-in/filter`

## Testing

Run the tests using:

```bash
pytest
```

## Logging

API requests and errors are logged to the console for monitoring and debugging.

## Contributing

Feel free to contribute to this project. Create an issue or submit a pull request for any enhancements or bug fixes.
