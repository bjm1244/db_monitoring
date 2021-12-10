from django.db import connection


def show_variable_all():
    cursor = connection.cursor()
    cursor.execute("SHOW VARIABLES")
    rows = cursor.fetchall()
    result_data_list = []
    for row_idx, row in enumerate(rows):
        result_data_list.append({
            "variable_idx": row_idx,
            "variable_name": row[0],
            "value": row[1]
        })
    return result_data_list
