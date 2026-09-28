from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionState:
    step: int
    line_number: int
    code: str
    event: str
    variables: dict[str, Any] = field(default_factory=dict)
    output: str = ""


class ExecutionHistory:
    def __init__(self):
        self.steps: list[ExecutionState] = []

    def add_step(
        self,
        line_number: int,
        code: str,
        event: str,
        variables: dict,
        output: str = ""
    ):
        state = ExecutionState(
            step=len(self.steps) + 1,
            line_number=line_number,
            code=code,
            event=event,
            variables=variables,
            output=output
        )

        self.steps.append(state)

    def get_steps(self):
        return self.steps

    def clear(self):
        self.steps.clear()