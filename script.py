import re
import operator
from functools import partial

def run_user_query(dataset, sql_query):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        dataset (list): List of dictionaries representing the dataset.
        sql_query (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        # Parse the query
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", sql_query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        # Process SELECT clause
        select_items = [field.strip() for field in select_clause.split(',')]

        # Process WHERE clause
        conditions = where_clause.split('AND')
        # WARNING: This is vulnerable to code injection
        filter_conditions = lambda rec: eval(' and '.join(conditions), rec)
        # Process ORDER BY clause
        order_field = order_by_clause.strip()

        # Execute the query
        filtered_result = filter(filter_conditions, dataset)
        filtered_result = sorted(filtered_result, key=lambda x: x[order_field])
        filtered_result = [{field: record[field] for field in select_items} for record in filtered_result]

        return filtered_result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")