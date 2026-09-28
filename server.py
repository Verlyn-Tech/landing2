"""
Verlyn Tech — Local Preview Server
Serves the 5 landing page directions at http://localhost:8000
"""

import sys
import os

try:
    import uvicorn
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    app = FastAPI(title="Verlyn Tech Landing Page Preview")
    app.mount("/", StaticFiles(directory=".", html=True), name="static")

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8000))
        print(f"\n[+] Verlyn Tech Preview Server running at: http://localhost:{port}")
        print("    Explore all 5 directions via the master switcher at root.\n")
        uvicorn.run(app, host="0.0.0.0", port=port)

except ImportError:
    # Standard library fallback if dependencies not yet installed
    import http.server
    import socketserver

    PORT = int(os.environ.get("PORT", 8000))
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.extensions_map.update({
        ".html": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
    })

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n[+] Verlyn Tech Preview Server (Standard HTTP) running at: http://localhost:{PORT}")
        print("    Explore all 5 directions via the master switcher at root.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            sys.exit(0)
