# Dairy Farm Management System (LaitFerme)

This project is a Dairy Farm Management System built with a Django (Python) backend and a Vue.js (Vite) frontend. It uses Microsoft SQL Server as the database.

## Prerequisites

Before setting up the project, ensure you have the following installed on your machine:

- **Python** (3.8 or higher)
- **Node.js** (LTS version recommended) and **npm**
- **Microsoft SQL Server** (Express or Developer edition)
- **ODBC Driver 18 for SQL Server**

## Database Setup

1. Locate the SQL script `bdgestiondesvaches(1).sql` in the project root.
2. Open Microsoft SQL Server Management Studio (SSMS).
3. Connect to your local SQL Server instance.
4. Open the `bdgestiondesvaches(1).sql` file and execute it to create the database schema and tables.
   - *Note: Ensure the database name in the script matches what you intend to use (e.g., `LaitFerme`). If the script does not create the database itself, create a database named `LaitFerme` first.*

## Backend Setup (Django)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure Environment Variables and Database:
   - Ensure your `settings.py` is configured for your SQL Server instance.
   - For Windows Authentication (Trusted Connection), the `HOST` should be your server name (e.g., `localhost\MSSQLSERVER01`) and `extra_params` should include `Integrated Security=True`.
   - **Note on SQL Server v17/2025**: This project includes a patch (`patches.py`) to support newer SQL Server versions not yet officially recognized by `mssql-django`.

6. Initialize the Database:
   - **Crucial Step**: This project integrates with an existing legacy database (`LaitFerme`).
   - Run the SQL script `bdgestiondesvaches(1).sql` first to create the business tables.
   - Then, run migrations to create the Django system tables and User authentication table:
   ```bash
   python manage.py migrate
   ```
   - *Note: Business tables are set to `managed = False` in Django, so migrations will skip them.*

7. Run the Development Server:
   ```bash
   python manage.py runserver
   ```
   The backend API will be available at `http://127.0.0.1:8000/`.

## Frontend Setup (Vue.js + Vite)

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the Development Server:
   ```bash
   npm run dev
   ```
   The application will be accessible at `http://localhost:5173/`.

## Project Structure

- `backend/`: Django project code.
- `frontend/`: Vue.js + Vite application source code.
- `bdgestiondesvaches(1).sql`: Database initialization script.
