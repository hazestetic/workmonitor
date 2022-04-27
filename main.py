from workmonitor.cli import CLI
from workmonitor.monitor import WorkMonitor
from workmonitor.io import read_sessions_data, append_session


def main():
    cli = CLI()
    data = read_sessions_data()
    wm = WorkMonitor(sessions_data=data)
    is_running = True

    while is_running:
        try:
            option = cli.select_option(["Total hours", "Start/stop", "Exit"])
            if option == "Total hours":
                month = cli.select_month_number()
                cli.show_total_hours(hours=wm.total_hours(), month=month)
            elif option == "Start/stop":
                wm.switch()
            elif option == "Exit":
                is_running = False
        except KeyboardInterrupt:
            is_running = False
        finally:
            if not is_running:
                cli.show_exit_message()
                if wm.current_session.has_started():
                    append_session(repr(wm.current_session))
                    cli.show_session_append_success()


if __name__ == "__main__":
    main()
