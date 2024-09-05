from typing import List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_chatgpt(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return (response.choices[0].message.content)


prompt_role = '''Você é um assistente para jornalistas.
Sua tarefa é escrever artigos, baseados em FATOS que forem fornecidos para você.
Você deve respeitar as instruções: o TOM, o TAMANHO e o ESTILO.'''


def assist_journalist(facts: List[str], tone: str, length_words: int, style: str):
    facts = ", ".join(facts)

    prompt = f'''{prompt_role} \nFACTS: {facts} \nTONE: {tone}
        \nLENGTH: {length_words} words\nSTYLE: {style}'''

    return ask_chatgpt([{"role": "user", "content": prompt}])


print(
    assist_journalist(
        ["O céu é azul", "A grama é verde"], "informal", 100, "blogpost"
    )
)
