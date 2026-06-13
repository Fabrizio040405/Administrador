import flet as ft
import os
# Imágenes
base = os.path.dirname(__file__)
temp = os.path.join(base,'templates')
# /Imágenes

def main(page : ft.Page):
    page.title = "Login"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.full_screen = False
    page.window.resizable = False
    page.window.maximizable = False
    page.window.max_width = 400
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_700
    # ------------------------------ Funciones ------------------------------
    def cont_change(content):
        Contenedor_principal.content = content
        page.update()
    # ----------------------------- /Funciones ------------------------------

    # -------------------------------- Login --------------------------------
    titulo_login = ft.Text("Iniciar Sesión", size=25)
    texto_login = ft.Text("Bienvenido, indique su usuario y contraseña", text_align=ft.TextAlign.CENTER)
    username_login = ft.TextField(label='Username', icon=ft.Icons.PERSON_2_OUTLINED, border_color=ft.Colors.WHITE)
    password_login = ft.TextField(label='Password',password=True, can_reveal_password=True, icon=ft.Icons.PERSON_2_OUTLINED,  border_color=ft.Colors.WHITE)
    boton_login = ft.Button('Ingresar',
                              bgcolor='WHITE',
                              color='BLACK',
                              icon=ft.Icons.ACCOUNT_TREE,
                              width = 125,
                              height= 33,
                              )
    #username y password
    col1_Login = ft.Column(controls=[titulo_login,ft.Text('',size=8),username_login, password_login,boton_login,ft.Text('',size=8),texto_login], 
                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                           alignment=ft.MainAxisAlignment.CENTER,
                           scroll=ft.ScrollMode.AUTO,
                           auto_scroll=True,
                           
                           )
    
    contenedor_login = ft.Container(
                            content=col1_Login,
                            bgcolor=ft.Colors.BLACK_87,
                            expand=True,
                            padding=20,  # Un margen interior para que los TextField no toquen los bordes
                            opacity=0.80
                            )

    # ------------------------------ /Login ---------------------------------

    # ------------------------------ 

    #########################################################################
    # ----------------------- Contenedor Principal --------------------------
    Contenedor_principal = ft.Container(content=contenedor_login,
                           bgcolor=ft.Colors.BLACK,
                           expand=True,
                           image = ft.DecorationImage(src='login_imagen_2.png',opacity=0.8,fit=ft.BoxFit.COVER),
                           width=1290,
                           height=800
                           )
    # ----------------------- /Contenedor Principal -------------------------
    #########################################################################
    # ------------------------------ Page.add -------------------------------
    page.add(Contenedor_principal)
    # ----------------------------- /Page.add -------------------------------

if __name__ == "__main__":
    ft.run(main=main, port=10000, assets_dir=temp)