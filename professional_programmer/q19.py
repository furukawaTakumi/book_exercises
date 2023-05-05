import sys


class StringEchoFSM:
    def __init__(self, init_state, transitions) -> None:
        self.__state = init_state
        self.__transitions = transitions
        self.__parse_result = []

    def get_next_state(self, event):
        state_row = self.__transitions[self.__state]
        try:
            next_state, action = state_row[event]
        except KeyError:
            next_state, action = state_row["default"]
        return next_state, action

    def execute(self):
        ch = None
        while ch or ch == None:
            ch = sys.stdin.read(1)
            self.__state, action = self.get_next_state(ch)

            if action == "start_new_string":
                self.__parse_result = []
                pass
            elif action == "ignore":
                pass
            elif action == "finish_current_string":
                print("".join(self.__parse_result))
                pass
            elif action == "add_current_to_string":
                self.__parse_result.append(ch)


if __name__ == "__main__":
    fsm = StringEchoFSM(
        "look_for_string",
        {
            "look_for_string": {
                '"': ["in_string", "start_new_string"],
                "default": ["look_for_string", "ignore"],
            },
            "in_string": {
                '"': ["look_for_string", "finish_current_string"],
                "\\": ["copy_next_char", "add_current_to_string"],
                "default": ["in_string", "add_current_to_string"],
            },
            "copy_next_char": {"default": ["in_string", "add_current_to_string"]},
        },
    )
    fsm.execute()
