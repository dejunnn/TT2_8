import json
import sqlite3
from collections import namedtuple
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Integer, String

from app import models

# global
BASE_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = Path(BASE_DIR, "data")


def connect_DB(db_name: str = "expenses.db") -> SQLAlchemy:
    """Connect to the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


class GetExpenses:
    """Insert business expense created from frontend into Expense table.

    Args:
        db ([type]): [description]

    Returns:
        [type]: [description]
    """

    def __init__(
        self, json_d: Union[Dict[str, Any], str], db_name: str
    ) -> None:
        """Takes in a json object and inserts it into the database.
        Assumes that frontend will pass me in a json_dict or a json_file.

        Args:
            json_d (Dict[str, Any]): [description]
        """
        if not isinstance(json_d, dict):
            with open(json_d) as f:
                self.json_d = json.load(f)
        else:
            self.json_d = json_d

        self.db_name = db_name

        self.conn, self.cursor = connect_DB()

        self.debug = True

    def insert_expense(self):
        """Insert business expense created from frontend into Expense table.

        Args:
            project_id ([type]): [description]
        """

        if self.debug:
            # Insert a row of data
            insert_exp = f'INSERT INTO {self.db_name} \
                            (project_id, category_id, name, description, amount, created_at, created_by, updated_at, updated_by) \
                            VALUES \
                            ({self.json_d["id"]}, {self.json_d["project_id"]}, \
                            {self.json_d["category_id"]},{self.json_d["name"]},\
                            {self.json_d["description"]},{self.json_d["amount"]},\
                            {self.json_d["created_at"]}, {self.json_d["created_by"]},\
                            {self.json_d["updated_at"]}, {self.json_d["updated_by"]}) \
                            ON DUPLICATE KEY UPDATE amount={self.json_d["amount"]}\
                             * from expenses'

            self.cursor.execute(insert_exp)
            self.conn.commit()  # Save (commit) the changes
            expense = models.Expenses(**self.json_d)
            self.close_connection()
            return expense.to_dict()

    def return_expense(self) -> List[float]:
        """Returns the expense from the database.

        Args:
            project_id ([type]): [description]
        """
        select_exp = (
            f'SELECT * FROM {self.db} WHERE project_id={self.json_d["id"]}'
        )
        self.cursor.execute(select_exp)

        # [(record 1), (record 2), (record 3)]
        record_list = self.cursor.fetchall()
        expense_list = [record_tup[5] for record_tup in record_list]

        return expense_list

    def delete_expense(self):
        """Deletes the expense from the database.

        Args:
            project_id ([type]): [description]
        """
        if self.debug:
            # Insert a row of data
            delete_exp = f'INSERT INTO {self.db_name} \
                            (project_id, category_id, name, description, amount, created_at, created_by, updated_at, updated_by) \
                            VALUES \
                            ({self.json_d["id"]}, {self.json_d["project_id"]}, \
                            {self.json_d["category_id"]},{self.json_d["name"]},\
                            {self.json_d["description"]},{self.json_d["amount"]},\
                            {self.json_d["created_at"]}, {self.json_d["created_by"]},\
                            {self.json_d["updated_at"]}, {self.json_d["updated_by"]}) \
                            ON DUPLICATE KEY UPDATE amount={self.json_d["amount"]}\
                             * from expenses'

            self.cursor.execute(delete_exp)
            self.conn.commit()  # Save (commit) the changes
            expense = models.Expenses(**self.json_d)
            self.close_connection()
            return expense.to_dict()

    def close_connection(self):
        """Close the connection to the database."""
        self.conn.close()


get = GetExpenses(json_d=Path(DATA_DIR, "expense.json"), db_name="Expense")

insert_expense = get.insert_expense()
return_expense = get.return_expense()
delete_expense = get.delete_expense()
