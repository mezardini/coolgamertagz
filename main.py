from fastapi import FastAPI, Body, Depends, HTTPException
import openai
from pydantic import BaseModel
import environ
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
env = environ.Env()
environ.Env.read_env()

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()

GamerTag = models.GamerTag
User = models.User


def create_gamertag(db: Session, tag: str, prompt: str):
    tag = GamerTag(tag=tag, prompt=prompt)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Create a .env file and set your "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
OPENAI_API_KEY = env("OPENAI_API_KEY")

# Initialize the OpenAI API client
openai.api_key = OPENAI_API_KEY


class OpenAIRequest(BaseModel):
    prompt: str


class OpenAIResponse(BaseModel):
    choices: list


@app.post("/create-gamer-tag/")
def CreateGamerTag(request: OpenAIRequest, user_prompt: str):
    try:
        # Send a request to the OpenAI API
        tag_creation_prompt = f"I want to create a cool gamer tag, here are some details: {user_prompt}. I want only the tag as response."
        response = openai.Completion.create(
            engine="davinci-002",  # Use the appropriate GPT-3 engine
            prompt=tag_creation_prompt,
            max_tokens=20,  # Set the maximum number of tokens for the response
            n=1,  # Set the number of completions to generate
            stop=None,  # Set stop criteria if needed
        )

        # Extract the generated text from the response
        generated_text = response.choices[0].text.strip()
        create_tag = create_gamertag(generated_text, tag_creation_prompt)

        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create-user/")
def create_user_endpoint(
    name: str,
    email: str,
    db: Session = Depends(get_session),
):
    user = create_user(name=name, email=email)

    return user.name


@app.get("/")
def getHello(session: Session = Depends(get_session)):

    return 'Hello'
