import gradio as gr
import requests

def ask_solyn(prompt, dev_mode):
    response = requests.post("https://your-render-app.onrender.com/query", json={
        "question": prompt,
        "dev_mode": dev_mode
    })
    return response.json().get("answer", "Error")

gr.Interface(
    fn=ask_solyn,
    inputs=[gr.Textbox(label="Ask Solyn"), gr.Checkbox(label="Developer Mode")],
    outputs="text",
    title="Solyn UI",
    allow_flagging="never"
).launch(server_name="0.0.0.0", server_port=8501)
