# TextGame Module: A Module for Text-Based/ASCII-Based Games
import curses
class KeyMapper:
    def __init__(self):
        self.actions = {}
        self.enabled = True
    def set_action(self, key, action_function):
        if self.enabled:
            self.actions[key] = action_function
    def get_action(self, key):
        return self.actions.get(key, None)
    def listen_for_keys(self, stdscr):
        while self.enabled:
            key = stdscr.getch()  # Capture a key press
            action = self.get_action(key)  # Retrieve the action for the pressed key
            if action:
                action()  # Call the action if it exists
    def start_listening(self):
        curses.wrapper(self._run)
    def _run(self, stdscr):
        # Set up curses settings
        stdscr.nodelay(1)  # Make getch() non-blocking
        curses.cbreak()    # React to keys immediately
        stdscr.keypad(True)  # Enable special keys handling
    # Main loop to listen for keys
        try:
            while self.enabled:
                stdscr.clear()
                stdscr.addstr(0, 0, "Press 'q' to quit.")
                stdscr.refresh()
                key = stdscr.getch()
                action = self.get_action(key)
                if action:
                    action()  # Call the action if it exists
                curses.napms(100)  # Add a small delay
                
        finally:
            self.stop_listening()  # Ensure we properly stop listening on exit
    def stop_listening(self):
        self.enabled = False  # This will stop the listening loop