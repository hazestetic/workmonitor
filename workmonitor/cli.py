from datetime import datetime
from typing import Protocol


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def _month(month_num: int) -> str:
    if not (1 <= month_num <= 12):
        raise RuntimeError("Wrong month number.")
    return MONTHS[month_num]


class UserInterface(Protocol):
    def show_total_hours(self, month: int) -> None:
        raise NotImplementedError()

    def show_current_session(self) -> None:
        raise NotImplementedError()

    def show_exit_message(self) -> None:
        raise NotImplementedError()

    def select_option(self, options: list[str]) -> str:
        raise NotImplementedError()

    def select_month_number(self) -> int:
        raise NotImplementedError()

    def show_session_append_success(self) -> None:
        raise NotImplementedError()


class CLI(UserInterface):
    def show_total_hours(self, hours: float, month: int) -> None:
        print(f"[{_month(month)}] Hours worked = {hours:.3f}h\n")

    def show_current_session(self, session_str: str) -> None:
        print(f"{session_str}\r")

    def show_exit_message(self) -> None:
        print("bye.")

    def select_option(self, options: list[str]) -> int:
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        while True:
            try:
                option_num = int(input("Select option: "))
                if 1 <= option_num <= len(options):
                    return options[option_num - 1]
                else:
                    raise ValueError
            except ValueError:
                print("Wrong option number.")

    def select_month_number(self) -> int:
        current_month = datetime.now().month
        while True:
            try:
                month_num = input(f"[ENTER={current_month}] Select month: ")
                if len(month_num) == 0:
                    return current_month
                if 1 <= int(month_num) <= 12:
                    return month_num
                else:
                    raise ValueError
            except ValueError:
                print("Wrong month number.")

    def show_session_append_success(self) -> None:
        print("Session appended successfully.")


class KeyboardInterface(UserInterface):
    def show_total_hours(self, hours: float, month: int) -> None:
        raise NotImplementedError()

    def show_current_session(self, session_str: str) -> None:
        raise NotImplementedError()

    def show_exit_message(self) -> None:
        raise NotImplementedError()

    def select_option(self, options: list[str]) -> int:
        raise NotImplementedError()

    def select_month_number(self) -> int:
        raise NotImplementedError()

    def show_session_append_success(self) -> None:
        raise NotImplementedError()
