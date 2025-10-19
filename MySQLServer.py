#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database in MySQL.
If the database already exists, it will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user, password, and host if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"  # Change this to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # SQL statement to create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure resources are released properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional confirmation of closed connection
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
