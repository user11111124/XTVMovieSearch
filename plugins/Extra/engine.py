# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import openai

async def ai(query):
    openai.api_key = "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" #Your openai api key
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
