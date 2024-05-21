from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Footer


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("", classes="header"),
                Button("Saludar", id="butSaludar"),
                
            ),
            VerticalScroll(
                Static("", classes="footer"),
                Button("Salir", id="butSalir"),
                
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))
        if 
        


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())