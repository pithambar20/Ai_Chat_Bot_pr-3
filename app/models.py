from groq import Groq

client = Groq(
    api_key="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"
)

def get_completion_from_groq(message):
    # synchronous call
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,  # IMPORTANT
        stop=None
    )

    ai_message = ""
    if completion.choices and len(completion.choices) > 0:
        ai_message = completion.choices[0].message.content
        print(ai_message)

    return ai_message

# get_completion_from_groq("bsdk")


