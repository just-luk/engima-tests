import re
import operator
from functools import partial

def execute_user_query(records, user_query):
    """
    Execute a custom SQL-like query on a list of dictionaries.

    Args:
        records (list): List of dictionaries representing the dataset.
        user_query (str): SQL-like query string.

    Returns:
        list: List of dictionaries representing the query results.

    Raises:
        ValueError: If the query is invalid or cannot be executed.
    """
    try:
        # Parse the query
        match = re.match(r"SELECT (.*) FROM data WHERE (.*) ORDER BY (.*)", user_query, re.IGNORECASE)
        if not match:
            raise ValueError("Invalid query format")

        select_clause, where_clause, order_by_clause = match.groups()

        # Process SELECT clause
        selected_fields = [field.strip() for field in select_clause.split(',')]

        # Process WHERE clause
        query_conditions = where_clause.split('AND')
        # WARNING: This is vulnerable to code injection
        filtering_function = lambda row: eval(' and '.join(query_conditions), row)
        # Process ORDER BY clause
        order_key = order_by_clause.strip()

        # Execute the query
        query_result = filter(filtering_function, records)
        query_result = sorted(query_result, key=lambda item: item[order_key])
        query_result = [{field: item[field] for field in selected_fields} for item in query_result]

        return query_result

    except Exception as e:
        raise ValueError(f"Error executing query: {str(e)}")