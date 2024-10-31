import copy

from gpt.gpt_instructions import INSTRUCTIONS_CHATBOT
from gpt.gpt_interface import query_gpt


def generate_messages(user_instructions: str, message_history: list[dict[str, str]] | None) -> list[dict[str, str]]:
    if not message_history:
        input_messages = [
            {"role": "system", "content": user_instructions},
            {"role": "user", "content": "Generate an opening message."}
        ]

        client_input, _ = query_gpt(messages=input_messages)

        output_messages = [
            {"role": "system", "content": INSTRUCTIONS_CHATBOT},
            {"role": "user", "content": client_input}
        ]
    else:
        message_history_inverted = _invert_roles(copy.deepcopy(message_history))
        input_messages = [{"role": "system", "content": user_instructions}] + message_history_inverted[1:] + [{"role": "user", "content": "Generate your next message"}]

        client_input, _ = query_gpt(messages=input_messages)

        output_messages = [{"role": "system", "content": INSTRUCTIONS_CHATBOT}] + message_history[1:] + [{"role": "user", "content": client_input}]

    # print(f"USER: {client_input}")
    return output_messages


def _invert_roles(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    for message in messages:
        if message["role"] == "user":
            message["role"] = "assistant"
        elif message["role"] == "assistant":
            message["role"] = "user"
    
    return messages