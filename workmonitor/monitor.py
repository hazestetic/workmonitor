from datetime import datetime
from workmonitor.session import WorkSession
from workmonitor.io import read_sessions_data
from functools import cache


@cache
def _total_seconds(sessions: tuple[WorkSession]) -> float:
    """Previous session total-times should be calculated only once per program execution."""
    return sum(sess.total_seconds() for sess in sessions)


class WorkMonitor:
    _sessions: list[WorkSession]
    current_session: WorkSession

    def __init__(self, sessions_data: list[str]) -> None:
        self._sessions = [WorkSession(line) for line in sessions_data]
        self.current_session = WorkSession()

    def total_hours(self, month: int = datetime.now().month):
        """Calucates total number of hours worked in arbitrary month."""
        return (
            _total_seconds(tuple(self._sessions)) + self.current_session.total_seconds()
        ) / 3600.0

    def switch(self):
        """Starts/stops working session iterval."""
        if self.current_session.is_idle():
            self.current_session.start()
        else:
            self.current_session.stop()
