from openai import OpenAI
client = OpenAI()
import ast
api_key="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"
def gpt(txt):
    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": f"{txt}"}
        ]
        )
        x=ast.literal_eval(response.choices[0].message.content)
        res=x['response']
        return str(res)
    except Exception as e:
        return f"error code {e}"