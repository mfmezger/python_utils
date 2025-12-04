"""Initialization of Google LLMs."""

import os
import textwrap

from google.genai.types import HarmBlockThreshold, HarmCategory
from google.oauth2 import service_account
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel, GoogleModelSettings
from pydantic_ai.providers.google import GoogleProvider


def _load_google_credentials() -> service_account.Credentials:
    """Load Google credentials from GOOGLE_APPLICATION_CREDENTIALS environment variable.

    Returns:
        google.oauth2.credentials.Credentials: The loaded credentials

    Raises:
        EnvironmentError: If GOOGLE_APPLICATION_CREDENTIALS is not set or invalid

    """
    credentials_path = os.getenv(key="GOOGLE_APPLICATION_CREDENTIALS")

    try:
        return service_account.Credentials.from_service_account_file(
            filename=credentials_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
    except Exception as e:
        msg = f"Failed to load Google Cloud credentials from '{credentials_path}'. Please ensure the file exists and is a valid service account JSON file. Error: {e}"
        raise OSError(msg)


def initialize_agent(
    prompt: str,
    output_model: type[BaseModel],
    temperature: float = 0.7,
    thinking_budget: int = 0,
    model_name: str = "gemini-2.5-flash",
    tools: list | None = None,
    retries: int = 5,
) -> Agent[str, BaseModel]:
    """Initialize a Pydantic AI agent with Google model.

    Args:
        prompt: System prompt for the agent
        output_model: Pydantic model for structured output
        temperature: Model temperature for randomness
        thinking_budget: Budget for thinking tokens
        model_name: Name of the Google model to use
        tools: List of tools to be used by the agent (default: None)
        retries: Number of retries for failed requests (default: 5)

    Returns:
        Configured Pydantic AI agent

    """
    if tools is None:
        tools = []

    credentials = _load_google_credentials()

    provider = GoogleProvider(credentials=credentials, location="europe-west1")
    model = GoogleModel(model_name=model_name, provider=provider)
    model_settings = GoogleModelSettings(
        temperature=temperature,
        google_thinking_config={"thinking_budget": thinking_budget},
        google_safety_settings=[
            {
                "category": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                "threshold": HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                "threshold": HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_HARASSMENT,
                "threshold": HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                "threshold": HarmBlockThreshold.BLOCK_NONE,
            },
            {
                "category": HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
                "threshold": HarmBlockThreshold.BLOCK_NONE,
            },
        ],
    )

    return Agent(
        model=model,
        output_type=output_model,
        instrument=True,
        model_settings=model_settings,
        retries=retries,
        system_prompt=textwrap.dedent(
            text=prompt,
        ),
        tools=tools,
    )
