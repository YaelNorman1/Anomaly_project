def get_quantity_query(user_id: int, category: str):
    return f"""
        SELECT {category}
        FROM user_statistics
        WHERE userId = {user_id} 
    """
