from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label


class ErrorScreen(ModalScreen):
    BINDINGS = [
        ("enter", "app.pop_screen", "Ok")
    ]

    CSS = """
    ModalScreen {
        background: blue;
        border: white;
        color: red;
        width: 50%;
        margin: 2 2;
        content-align: center middle;
        layout: vertical;
        background: $background 30%;
    }
    """

    def __init__(self, error_text: str):
        super().__init__()
        self.error_text = error_text

    def compose(self) -> ComposeResult:
        yield Label(
            "AN error has occured:\n"
            f"{self.error_text}"
        )
