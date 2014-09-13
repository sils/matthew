"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from datetime import datetime

from mathlib.output.LOG_LEVEL import LOG_LEVEL
from mathlib.output.Printer import Printer


class LogMessage:
    def __init__(self, log_level, message):
        if not log_level in [LOG_LEVEL.DEBUG, LOG_LEVEL.WARNING, LOG_LEVEL.ERROR]:
            raise ValueError("log_level has to be a valid LOG_LEVEL.")
        if message == "":
            raise ValueError("Empty log messages are not allowed.")

        self.log_level = log_level
        self.message = str(message).strip()

    def __str__(self):
        return '[{}] {}'.format({LOG_LEVEL.DEBUG: "DEBUG",
                                 LOG_LEVEL.WARNING: "WARNING",
                                 LOG_LEVEL.ERROR: "ERROR"}.get(self.log_level, "ERROR"), self.message)


class LogPrinter(Printer):
    def __init__(self, timestamp_format="%X"):
        Printer.__init__(self)
        self.timestamp_format = timestamp_format

    def _get_log_prefix(self, log_level, timestamp):
        datetime_string = timestamp.strftime(self.timestamp_format)

        if datetime_string != "":
            datetime_string = "["+datetime_string+"]"

        return '[{}]{} '.format({LOG_LEVEL.DEBUG: "DEBUG",
                                 LOG_LEVEL.WARNING: "WARNING",
                                 LOG_LEVEL.ERROR: "ERROR"}.get(log_level, "ERROR"),
                                datetime_string)

    def debug(self, message, timestamp=None, **kwargs):
        return self.log_message(LogMessage(LOG_LEVEL.DEBUG, message), timestamp=timestamp, **kwargs)

    def warn(self, message, timestamp=None, **kwargs):
        return self.log_message(LogMessage(LOG_LEVEL.WARNING, message), timestamp=timestamp, **kwargs)

    def err(self, message, timestamp=None, **kwargs):
        return self.log_message(LogMessage(LOG_LEVEL.ERROR, message), timestamp=timestamp, **kwargs)

    def log(self, log_level, message, timestamp=None, **kwargs):
        return self.log_message(LogMessage(log_level, message), timestamp=timestamp, **kwargs)

    def log_exception(self, message, exception, log_level=LOG_LEVEL.ERROR, timestamp=None, **kwargs):
        if not isinstance(exception, BaseException):
            raise TypeError("log_exception can only log derivatives of BaseException.")

        return self.log_message(LogMessage(log_level, message + "\n\n" + _("Exception was:") + "\n" + str(exception)),
                                timestamp=timestamp,
                                **kwargs)

    def log_message(self, log_message, timestamp=None, **kwargs):
        if not isinstance(log_message, LogMessage):
            raise TypeError("log_message should be of type LogMessage.")
        if not isinstance(timestamp, datetime):
            timestamp = datetime.today()

        prefix = self._get_log_prefix(log_message.log_level, timestamp)
        return self.print(prefix, log_message.message, delimiter="", **kwargs)
