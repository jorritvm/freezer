import signal
import sys
import reflex as rx

from .style import freezer_theme

app = rx.App(
    theme=freezer_theme
)

# Handle Ctrl+C properly
def shutdown_handler(sig, frame):
    print("Shutting down Reflex...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)


