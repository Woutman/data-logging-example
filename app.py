import copy

from openai.types import CompletionUsage

from users import create_users, User
from gpt_interface import query_gpt
from gpt_instructions import INSTRUCTIONS_CHATBOT


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
        message_history_inverted = invert_roles(copy.deepcopy(message_history))
        input_messages = [{"role": "system", "content": user_instructions}] + message_history_inverted[1:] + [{"role": "user", "content": "Generate your next message"}]

        client_input, _ = query_gpt(messages=input_messages)

        output_messages = [{"role": "system", "content": INSTRUCTIONS_CHATBOT}] + message_history[1:] + [{"role": "user", "content": client_input}]

    print(f"USER: {client_input}")
    return output_messages


def invert_roles(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    for message in messages:
        if message["role"] == "user":
            message["role"] = "assistant"
        elif message["role"] == "assistant":
            message["role"] = "user"
    
    return messages


def simulate_conversation(user: User) -> tuple[list[dict[str, str]], list[CompletionUsage]]:
    if not user.instructions:
        raise ValueError("User has no instructions assigned.")
    
    usages = list()
    message_history = list()
    gpt_output = ""
    i = 0
    unending_conversation_cutoff = 5
    while gpt_output != "DONE" and i < unending_conversation_cutoff:
        message_history = generate_messages(user_instructions=user.instructions, message_history=message_history)

        gpt_output, usage = query_gpt(messages=message_history)
        print(f"GPT:  {gpt_output}")
        usages.append(usage)

        message_history.append({"role": "assistant", "content": gpt_output})
        i += 1
    
    return message_history, usages


def main():
    user_count = 10
    users = create_users(user_count)
    simulate_conversation(users[0])


if __name__ == "__main__":
    main()
