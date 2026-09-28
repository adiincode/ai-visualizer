import sys
import linecache
import copy
import io
from contextlib import redirect_stdout

from execution_state import ExecutionHistory


class PythonTracer:

    def __init__(self):
        self.history = ExecutionHistory()
        self.output_buffer = io.StringIO()

    def trace_function(self, frame, event, arg):

        if event == "line":

            filename = frame.f_code.co_filename
            line_number = frame.f_lineno

            code = linecache.getline(
                filename,
                line_number
            ).strip()

            variables = {}

            for name, value in frame.f_locals.items():
                try:
                    variables[name] = copy.deepcopy(value)
                except Exception:
                    variables[name] = str(value)

            self.history.add_step(
                line_number=line_number,
                code=code,
                event=event,
                variables=variables
            )

        return self.trace_function

    def run(self, code: str):

        self.history.clear()

        filename = "<user_code>"

        # Make source available to linecache
        lines = code.splitlines()
        linecache.cache[filename] = (
            len(code),
            None,
            lines,
            filename
        )

        try:

            compiled_code = compile(
                code,
                filename,
                "exec"
            )

            sys.settrace(self.trace_function)

            with redirect_stdout(self.output_buffer):

                exec(
                    compiled_code,
                    {
                        "__name__": "__main__"
                    }
                )

        except Exception as e:

            self.output_buffer.write(
                f"\nERROR: {type(e).__name__}: {e}"
            )

        finally:

            sys.settrace(None)

            linecache.cache.pop(
                filename,
                None
            )

        output = self.output_buffer.getvalue()

        # Add output to final step
        if self.history.steps:
            self.history.steps[-1].output = output

        return self.history.get_steps()