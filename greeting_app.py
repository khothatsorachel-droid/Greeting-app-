import flet as ft

def main(page: ft.Page):
    page.title = "Greeting App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_field = ft.TextField(label="Enter your name", width=300)
    greeting_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def greet_click(e):
        name = name_field.value.strip()
        greeting_text.value = f"Hello, {name}!" if name else "Hello! Please enter your name."
        page.update()

    page.add(
        ft.Column(
            controls=[
                name_field,
                ft.ElevatedButton(text="Greet Me", on_click=greet_click),
                greeting_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
