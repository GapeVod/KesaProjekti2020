def show_messages(unsent_messages, sent_messages):
    """prints messages"""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def send_messages(sent_messages):
    """send messagoos"""
    print(f"\nThese messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)





unsent_messages = ['message1', 'message2', 'message3']
sent_messages = []
show_messages(unsent_messages[:], sent_messages)
send_messages(sent_messages)
print(unsent_messages)
