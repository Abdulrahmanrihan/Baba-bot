from mistralai import Mistral
import os

client = Mistral(api_key=os.environ.get['MISTRAL API KEY'])

class DadBot:
    def __init__(self, id, query):
        self.id = id
        self.user_query = query

    def send_query(self):
        chat_response = client.agents.complete(
            agent_id=self.id,
            messages=[{"role": "user", "content": self.user_query}],
        )
        output = chat_response.choices[0].message.content
        return output
