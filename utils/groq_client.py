import os
from typing import Optional

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def get_groq_api_key() -> Optional[str]:
    return os.getenv("GROQ_API_KEY")


def get_default_model() -> str:
    return os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")


def get_groq_client() -> Optional[Groq]:
    api_key = get_groq_api_key()
    if not api_key:
        return None
    return Groq(api_key=api_key)


def groq_chat_completion(
    user_prompt: str,
    system_prompt: str,
    model: Optional[str] = None,
    temperature: float = 0.3,
) -> str:
    client = get_groq_client()
    if client is None:
        raise ValueError("GROQ_API_KEY is missing. Add it to the .env file.")

    response = client.chat.completions.create(
        model=model or get_default_model(),
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content or ""
