import os
import urllib.parse
import urllib.request
import uuid
from http.client import HTTPMessage

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Footer

from app.screens.enter_link import EnterLinkScreen
from app.screens.error import ErrorScreen
from app.widgets.download import Download


class DownloaderApp(App):
    """App to download files."""
    TITLE = "Downloader"
    CSS_PATH = "styles/download.css"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "add_task", "Add download")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(id="downloads_container")

    def action_add_task(self):
        def check_link(link: str):
            if link:
                self.start_download(link=link)

        self.push_screen(EnterLinkScreen(), callback=check_link)

    def start_download(self, link: str):
        try:
            d = urllib.request.urlopen(url=link)
            file_name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(url=link).path))
            info: HTTPMessage = d.info()
            self.query_one("#downloads_container").mount(
                Download(
                    file_name=file_name,
                    file_size=info.get("Content-Length"),
                    file_id=f"file{uuid.uuid4().hex}",
                    url=link
                )
            )
        except Exception as e:
            self.push_screen(ErrorScreen(error_text=e))


if __name__ == "__main__":
    app = DownloaderApp()
    app.run()
