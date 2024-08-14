from dadBot import DadBot
import gradio as gr

chat_history = []
def dad_bot_response(query, history):
    id = "ag:196752d7:20240811:dad-how-do-i:689513dc"

    dadbot = DadBot(id, query)
    response = dadbot.send_query()

    history.append((query, response))
    return history, ""

def clear_chat():
    return [], ""

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center;'>أبي كيف يمكنني ان...</h1>", rtl=True)
    gr.Markdown("<h4 style='text-align: center;'>تم استلهام هذا المشروع من احد قنوات اليوتيوب حيث يقوم مالك القناة بتعليم الاطفال مهارات حياتية مختلفة</h4>", rtl=True)
    chatbot = gr.Chatbot()
    textbox = gr.Textbox(lines=2, placeholder="اسأل والدك سؤالاً...", rtl=True)
    submit_button = gr.Button("اسأل")
    clear_button = gr.Button("مسح الرسائل")

    state = gr.State([])

    submit_button.click(dad_bot_response, [textbox, state], [chatbot, textbox])
    clear_button.click(clear_chat, None, [chatbot, textbox])

demo.launch(share=True)
