import tkinter as tk
from tkinter import scrolledtext
import openai

openai.api_key = ""


def enviar_mensagem():
    mensagem = user_input.get()
    if mensagem == "fim":
        texto_conversa.insert(tk.END, "Fim da conversa.\n")
        return
    messages.append({"role": "user", "content": mensagem})
    texto_conversa.insert(tk.END, f"Usuário: {mensagem}\n")
    user_input.delete(0, tk.END)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=messages,
        max_tokens=200
    )

    resposta = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": resposta})
    texto_conversa.insert(tk.END, f"Assistente: {resposta}\n")
    texto_conversa.yview(tk.END)


root = tk.Tk()
root.title("Conversa com Assistente de Startup")
root.geometry("600x400")

texto_conversa = scrolledtext.ScrolledText(root, wrap=tk.WORD)
texto_conversa.pack(expand=True, fill=tk.BOTH)

user_input = tk.Entry(root, width=50)
user_input.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.X)

enviar_button = tk.Button(root, text="Enviar", command=enviar_mensagem)
enviar_button.pack(side=tk.RIGHT, padx=10, pady=10)

messages = [{"role": "system", "content": "You are a helpful assistant."}]

root.mainloop()
