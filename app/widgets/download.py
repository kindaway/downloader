from threading import Thread

from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Label, ProgressBar

from app.utils.download_chunked import download


class Download(Static):

    def __init__(self, file_name: str, file_size: float, file_id: str, url: str):
        super().__init__()
        self.file_name = file_name
        self.file_size = file_size
        self.file_id = file_id
        self.url = url

    def compose(self) -> ComposeResult:
        with Horizontal(classes="download", id=self.file_id):
            yield Label(self.file_name, classes="download_label")
            yield ProgressBar(
                total=int(self.file_size), id=f"progress_bar_{self.file_id}"
            )

    async def _on_mount(self, event: events.Mount) -> None:
        download_thread = Thread(
            target=download,
            kwargs={
                "url": self.url,
                "progress_bar": self.query_one(f"#progress_bar_{self.file_id}"),
                "chunk_size": 32768
            },
            daemon=True
        )
        download_thread.start()
