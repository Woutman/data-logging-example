from openai.types import CompletionUsage

from users import create_users, User
from gpt.gpt_interface import query_gpt
from messages import generate_messages
from loggers import log_data


@log_data
def simulate_conversation(user: User) -> tuple[list[dict[str, str]], list[CompletionUsage]]:
    if not user.instructions:
        raise ValueError("User has no instructions assigned.")
    
    usages = list()
    message_history = list()
    unending_conversation_cutoff = 5
    for _ in range(unending_conversation_cutoff):
        message_history = generate_messages(user_instructions=user.instructions, message_history=message_history)

        gpt_output, usage = query_gpt(messages=message_history)
        # print(f"GPT:  {gpt_output}")
        usages.append(usage)

        message_history.append({"role": "assistant", "content": gpt_output})
        
        if gpt_output == "DONE":
            break
    
    return message_history, usages


if __name__ == "__main__":
    import random

    user_count = 10
    users = create_users(user_count)

    num_simulations = 100
    for _ in range(num_simulations):
        user = users[random.randint(0, user_count - 1)]
        simulate_conversation(user=user)
