
def show_messages(messages):
    """prints messages"""
    for message in messages:
        msg = f"{message}"
        print(msg)


unsent_messages = ['message1', 'message2', 'message3']
show_messages(unsent_messages)
