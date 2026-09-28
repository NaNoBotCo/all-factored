import functools, http.server, pathlib, sys
docs = pathlib.Path(__file__).resolve().parent.parent / "docs"
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8871
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(docs))
http.server.ThreadingHTTPServer(("127.0.0.1", port), h).serve_forever()
