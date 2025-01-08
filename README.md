# Movie Search Application 🎥🔍

## Description

The **Movie Search Application** is a tool for finding movies based on various criteria, such as keywords, genre, or release year. The application interacts with a database to provide quick and convenient results. 🍿✨

---

## Project Files 📂

### `main.py` 🚀
The main entry point of the application.
- Initializes the connection to the database.
- Sets up the interaction between the user and the database manager through a console interface.

### `userHand.py` 🧑‍💻
Module responsible for handling user input:
- Search for movies by keywords.
- Search by genre or release year.
- View a list of the most popular queries.

### `Const.py` 📜
Contains SQL queries used for database operations:
- Search for movies by year.
- Search by genre.
- Search by keywords.
- Save user queries and analyze popular searches.

### `db_manager.py` 🗄️
Class for managing database interactions:
- Connects to the database for read and write operations.
- Executes search queries.
- Saves user query data.
- Manages database connections.

---

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone <URL>
   ```

2. Install dependencies:
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

---

## Usage 🖥️

1. Run the application:
   ```bash
   python main.py
   ```

2. Follow the console prompts to search for movies.

---

## Features ✨

### 1. Keyword Search 🔑
- Enter a keyword to search for movies by title, actors, or language.

### 2. Search by Genre or Release Year 📅
- Choose to search by genre or year.
- Enter the desired genre or release year to get a list of movies.

### 3. List of Most Popular Queries 📊
- View the last 5 user queries.
- Discover the most popular query among users.

---

## Example Usage 📝

### Running the Program
```bash
python main.py
```

### Console Output
```
Commands
1. Search by Keyword
2. Search by Genre or Release Year
3. View Most Popular Queries
Exit

Enter your request!
```

### Search Result
```
Search Results:
- Movie Title 1
- Movie Title 2
```

---

## Requirements 📋
- Python 3.8+
- MySQL

---

## Authors 🧑‍🎨
Developer: **Vladyslav Habelko**

---

Enjoy your movie search experience! 🎬🍿