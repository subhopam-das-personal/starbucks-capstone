# my_package/printer.py

def print_comment(comment):
    """
    Prints a heading with a specific format.
    
    Parameters:
    - comment: str, the comment text to print.
    """
    line_length = 30
    print(f"{'▬' * line_length} {comment} {'▬' * line_length}")

def print_done():
    """
    Prints a celebration message indicating job completion.
    """
    celebration_message = "Celebration: your job completed"
    emojis = "🎉" * 26
    print(f"{celebration_message} {emojis}")