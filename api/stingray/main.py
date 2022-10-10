from argparse import ArgumentParser

import uvicorn

from stingray import StingrayApp

app = StingrayApp()


if __name__ == "__main__":
    parser = ArgumentParser("Stingray")
    parser.add_argument("--host", default="0.0.0.0", type=str, help="bind socket to this host")
    parser.add_argument("--port", default=8000, type=int, help="bind socket to this port")
    parser.add_argument("--reload", action="store_true", default=False, help="enable auto-reload")

    uvicorn.run(app=app, **vars(parser.parse_args()))
