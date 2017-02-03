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
"""Output log device.

The module contains the output devices to write the logs.

Classes:
  + OutputDevice: Abstract base class for output device implementations
  + ConsoleDevice: Console device. Writes output into the standard output.
  + FileDevice: File device. Writes the output into a file.
"""
from __future__ import print_function


class OutputDevice(object):
    """Abstract base class for output device implementations.

    You will need to implement the following methods:
        + write: Write the log into the device.
        + close: Close the device.
    """

    def write(self, text=""):
        """Write the log into the device."""
        raise NotImplementedError("write not implemented")

    def close(self):
        """Close the device."""
        raise NotImplementedError("close not implemented")


class OutputConsoleDevice(OutputDevice):
    """Console device. Writes output into the standard output.

    Functions:
      + __init__: Initialize the device with the specified file path.
      + write: Write the log into the standard output.
      + close: Do nothing, no need to close device.
    """

    def __init__(self, state, appInfo):
        """Initialize the device."""
        self.support_ansi = state['show_progress']
        self.state = state
        self._appInfo = appInfo

    def write(self, text=""):
        """Write the log into the standard output."""
        self._appInfo.current_output_index += 1
        # 33[k is an ANSI code to clear the line
        # We need it to clear the optional progress bar.
        if self.support_ansi:
            print("\033[K" + text)
        else:
            # Catch any potential exception when piping the output and
            # terminating the program.
            try:
                print(text)
            except IOError:
                # It makes no sense to print the error since we already had
                # an exception printing a message.
                pass

    def close(self):
        """Do nothing, no need to close device."""
        pass


class OutputFileDevice(OutputDevice):
    """File device. Writes the output into a file.

    Functions:
      + __init__: Initialize the device with the specified file path.
      + write: Write the log into a file stream.
      + close: Close the file stream.
    """

    def __init__(self, state, appInfo, file_path, overwrite):
        """Initialize the device with the specified file path."""
        open_mode = "w" if overwrite else "a"
        self.stream = open(file_path, open_mode)
        self.state = state
        self._appInfo = appInfo

    def write(self, text=""):
        """Write the log into a file stream."""
        self._appInfo.current_output_index += 1
        self.stream.write(text + "\n")

    def close(self):
        """Close the file stream."""
        self.stream.close()
