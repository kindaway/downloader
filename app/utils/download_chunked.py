import urllib.parse
import os

import requests

from textual.widgets import ProgressBar


def download(url: str, progress_bar: ProgressBar, chunk_size: int = 16384):
    try:
        rs = requests.get(url=url, stream=True, allow_redirects=True)
        if 200 <= rs.status_code <= 299:
            name = rs.headers.get('filename')
            if not name:
                name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(url=url).path))
            with open(name, 'wb') as file:
                for part in rs.iter_content(chunk_size):
                    file.write(part)
                    progress_bar.advance(chunk_size)
        else:
            return
    except Exception as ex:
        print(ex)
        return
