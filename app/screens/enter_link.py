from textual import on
from textual.app import ComposeResult
from textual.containers import Center
from textual.screen import Screen
from textual.widgets import Header, Input, Footer


class EnterLinkScreen(Screen[str]):
    BINDINGS = [
        ("escape", "app.pop_screen", "Cancel"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Input(
                placeholder="Link", id="link_input"
            )
        yield Footer()

    @on(Input.Submitted)
    def enter_link(self):
        self.dismiss(result=self.query_one("#link_input").value)