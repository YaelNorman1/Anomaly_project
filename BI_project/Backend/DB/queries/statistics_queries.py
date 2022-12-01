def get_quantity_query(user_id: int, category: str):
    return f"""
        SELECT {category}
        FROM statistics
        WHERE userId == {user_id}
    """
