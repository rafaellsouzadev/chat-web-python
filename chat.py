import flet as ft
import emoji


def main(pagina):
    titulo = ft.Text("Chat Web")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        #adicionar a mensagem no chat
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
     
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        #cria a mensagem
        texto_campo_mensagem = f"{nome_usuario.value}: {emoji.emojize(campo_mensagem.value)}"        

        #Envia a mensagem pelo tunel
        pagina.pubsub.send_all(emoji.emojize(texto_campo_mensagem))

        #limpar o campo mensagem
        campo_mensagem.value = ""
        
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)   
   
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    
    def entrar_chat(evento):
        poput.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)

        #Informa qual usuario entrou no chat
            
        pagina.pubsub.send_all(nome_usuario.value + " entrou no chat")    

        linha_mensagem = ft.Row(
            [
                campo_mensagem,
                botao_enviar
            ]
        )
        pagina.add(linha_mensagem)
        pagina.update()

    poput =ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao chat Ao vivo"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    def iniciar_chat(evento):
        pagina.dialog = poput
        poput.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(titulo, botao_iniciar)



#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER, port=8081)