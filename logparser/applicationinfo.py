# Log Parser for RTI Connext.
#
#   Copyright 2016 Real-Time Innovations, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""Application information.

The module contains the class to store the information from the logged app..
"""


class ApplicationInformation(object):
    """Class to store the information from the logged app."""

    def __init__(self, config):
        """Constructor of the class."""
        self._configuration = config
        self._current_log_index = 0
        self._current_output_index = 0
        self._monotonic_clock = None
        self._system_clock = None

    # pylint: disable=E0211,W0612,W0212,C0111
    def configuration():
        """The current application configuration."""
        doc = "The current application configuration."

        def fget(self):
            return self._configuration
        return locals()
    configuration = property(**configuration())

    def current_log_index():
        """The current log line number."""
        doc = "The current log line number"

        def fget(self):
            return self._current_log_index

        def fset(self, value):
            self._current_log_index = value
        return locals()
    current_log_index = property(**current_log_index())

    def current_output_index():
        """The current output line number."""
        doc = "The current output line number."

        def fget(self):
            return self._current_output_index

        def fset(self, value):
            self._current_output_index = value
        return locals()
    current_output_index = property(**current_output_index())

    def monotonic_clock():
        """The monotonic clock."""
        doc = "The monotonic clock."

        def fget(self):
            return self._monotonic_clock

        def fset(self, value):
            self._monotonic_clock = value
        return locals()
    monotonic_clock = property(**monotonic_clock())

    def system_clock():
        """The system clock."""
        doc = "The system clock."

        def fget(self):
            return self._system_clock

        def fset(self, value):
            self._system_clock = value
        return locals()
    system_clock = property(**system_clock())
    # pylint: enable=E0211,W0612,W0212,C0111
