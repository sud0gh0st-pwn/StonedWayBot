import sqlite3
from typing import Any, Dict, List, Tuple

class DBManager:
    def __init__(self, db_file: str) -> None:
        self.db_file = db_file

    def create_connection(self) -> sqlite3.Connection:
        """Create a database connection to the SQLite database specified by db_file."""
        try:
            return sqlite3.connect(self.db_file)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self, conn: sqlite3.Connection, table_name: str, columns: Dict[str, str]) -> None:
        """Create a table with the given name and columns."""
        columns_with_types = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        sql = f'''CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});'''
        try:
            if conn:
                conn.execute(sql)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table {table_name}: {e}")

    def insert_record(self, conn: sqlite3.Connection, table_name: str, columns: List[str], values: Tuple[Any, ...]) -> None:
        """Insert a record into the specified table."""
        placeholders = ', '.join(['?'] * len(values))
        columns_formatted = ', '.join(columns)
        sql = f'''INSERT INTO {table_name} ({columns_formatted}) VALUES({placeholders})'''
        try:
            if conn:
                conn.execute(sql, values)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting record into {table_name}: {e}")

    def remove_record(self, conn: sqlite3.Connection, table_name: str, condition: str) -> None:
        """Remove a record from the specified table based on a condition."""
        sql = f'''DELETE FROM {table_name} WHERE {condition}'''
        try:
            if conn:
                conn.execute(sql)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error removing record from {table_name}: {e}")

    def update_record(self, conn: sqlite3.Connection, table_name: str, updates: Dict[str, Any], condition: str) -> None:
        """Update a record in the specified table based on a condition."""
        updates_formatted = ', '.join([f"{col} = ?" for col in updates])
        values = list(updates.values())
        sql = f'''UPDATE {table_name} SET {updates_formatted} WHERE {condition}'''
        try:
            if conn:
                conn.execute(sql, values)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating record in {table_name}: {e}")

    @staticmethod
    def close_connection(conn: sqlite3.Connection) -> None:
        """Close the database connection."""
        try:
            if conn:
                conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")
