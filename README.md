# Basigo Vehicle Maintenance API

## Overview  
The **Basigo Vehicle Maintenance API** is a RESTful API that allows a bus company to log, track, update, and manage vehicle maintenance tasks. The system ensures better maintenance planning and compliance with regulatory standards.

## Setup Instructions  

### **Clone the Repository**  
Run the following command in your terminal:  
```sh
git clone https://github.com/ChristineAkinyi/basigo-vehicle-maintenance-api.git
cd basigo-vehicle-maintenance-api
```

### **Create and Activate a Virtual Environment**  
- On macOS/Linux (WSL):  
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ```
- On Windows (Command Prompt):  
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```

### **Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the Database (PostgreSQL)**  
Ensure PostgreSQL is installed and running. Then, create a database:  
```sql
CREATE DATABASE basigo_maintenance;
CREATE USER basigo_user WITH ENCRYPTED PASSWORD 'YourSecurePassword';
GRANT ALL PRIVILEGES ON DATABASE basigo_maintenance TO basigo_user;
```
Update `settings.py` with your database credentials.

### **5️⃣ Run Migrations**  
```sh
python manage.py makemigrations maintenance
python manage.py migrate
```

### **6️⃣ Start the Development Server**  
```sh
python manage.py runserver
```
Your API should now be running at:  
🔗 `http://127.0.0.1:8000/`

## API Endpoints  

| Method  | Endpoint                        | Description                                    |
|---------|---------------------------------|------------------------------------------------|
| `POST`  | `/tasks/create/`                | Create a new maintenance task                 
| `GET`   | `/tasks/`                        | Retrieve a list of all maintenance tasks      
| `GET`   | `/tasks/{id}/`                   | Retrieve details of a specific task by ID     
| `PATCH` | `/tasks/{id}/update/`            | Update an existing maintenance task           
| `DELETE`| `/tasks/{id}/delete/`            | Delete a maintenance task                 
## Example API Requests  

### **Create a New Maintenance Task** (`POST /tasks/create/`)  
**Request Body:**  
```json
{
  "vehicle_registration": "KAA123A",
  "task_type": "Oil Change",
  "description": "Changed engine oil."
}
```
**Response:**  
```json
{
  "id": 1,
  "vehicle_registration": "KAA123A",
  "task_type": "Oil Change",
  "description": "Changed engine oil.",
  "date_performed": "2025-03-11",
  "updated_at": "2025-03-11T10:00:00Z"
}
```

### **Retrieve All Maintenance Tasks** (`GET /tasks/`)  
**Response:**  
```json
[
  {
    "id": 1,
    "vehicle_registration": "KAA123A",
    "task_type": "Oil Change",
    "description": "Changed engine oil.",
    "date_performed": "2025-03-11"
  }
]
```

## How to Contribute  
1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push to the branch: `git push origin feature-branch`  
5. Open a pull request.


