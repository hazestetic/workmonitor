from datetime import datetime
from enum import Enum

DATE_FMT = "%d/%m/%y"
HOUR_FMT = "%H:%M:%S"


class WorkStatus(Enum):
    WORKING = 1
    IDLE = 2


class WorkSession:
    """Tracks the working-time intervals."""

    _start_times: list[datetime]
    _end_times: list[datetime]
    status: WorkStatus

    def __init__(self, line: str = None) -> None:
        """Creates empty working session, or loads one from line of text."""
        self._start_times = []
        self._end_times = []
        self.status = WorkStatus.IDLE

        if line is not None:
            date_str, *time_strs = line.split(" ")
            for time_str in time_strs:
                start_str, end_str = time_str.split("-")
                start_time = datetime.strptime(
                    f"{date_str} {start_str}", f"{DATE_FMT} {HOUR_FMT}"
                )
                end_time = datetime.strptime(
                    f"{date_str} {end_str}", f"{DATE_FMT} {HOUR_FMT}"
                )
                self._start_times.append(start_time)
                self._end_times.append(end_time)

    def __repr__(self) -> str:
        """Represents current session as a string."""
        if len(self._start_times) == 0:
            raise RuntimeError("Session hasn't started yet.")

        if self.status == WorkStatus.WORKING:
            end_times = self._end_times + [datetime.now()]
        else:
            end_times = self._end_times

        date = self._start_times[0].strftime(DATE_FMT)
        times = " ".join(
            f"{start.strftime(HOUR_FMT)}-{end.strftime(HOUR_FMT)}"
            for start, end in zip(self._start_times, end_times)
        )
        return f"{date} {times}"

    def start(self) -> None:
        """Starts the working session interval."""
        self.status = WorkStatus.WORKING
        self._start_times.append(datetime.now())

    def stop(self) -> None:
        """Ends the working session interval"""
        if self.status != WorkStatus.WORKING:
            raise RuntimeError("Already")
        self.status = WorkStatus.IDLE
        self._end_times.append(datetime.now())

    def total_seconds(self) -> float:
        """Calculates the total of seconds worked."""
        return sum(
            (end - start).total_seconds()
            for start, end in zip(self._start_times, self._end_times)
        )

    def is_idle(self):
        return self.status == WorkStatus.IDLE

    def has_started(self):
        return len(self._start_times) > 0

    @property
    def month(self) -> int:
        if len(self._start_times) > 0:
            return self._start_times[0].month
        else:
            return datetime.now().month
