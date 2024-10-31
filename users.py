from dataclasses import dataclass
import math

from gpt.gpt_instructions import INSTRUCTIONS_HELPFUL_CLIENT, INSTRUCTIONS_LOST_CLIENT, INSTRUCTIONS_UNHELPFUL_CLIENT


@dataclass
class User:
    id: int
    name: str
    instructions: str | None = None


def create_users(user_count: int) -> list[User]:
    users = [User(id=i, name=f"user_{i}") for i in range(user_count)]
    for user in users:
        if user.id < math.floor(user_count / 5):
            user.instructions = INSTRUCTIONS_UNHELPFUL_CLIENT
        elif user.id < math.floor(2 * user_count / 5):
            user.instructions = INSTRUCTIONS_LOST_CLIENT
        else:
            user.instructions = INSTRUCTIONS_HELPFUL_CLIENT

    return users


if __name__ == "__main__":
    users = create_users(10)
    for user in users:
        print(user)
