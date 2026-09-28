
import os
from dotenv import load_dotenv
from groq import Groq


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. "
        "Please add GROQ_API_KEY=your_key in .env"
    )


# ============================================================
# GROQ CONFIGURATION
# ============================================================

MODEL = "openai/gpt-oss-20b"

client = Groq(
    api_key=GROQ_API_KEY
)


# ============================================================
# COMPACT EXECUTION HISTORY
# ============================================================

def make_compact_history(history, max_steps=12):
    """
    Convert tracer history into a small readable format.

    We intentionally limit the number of steps so that
    the Groq request does not become too large.
    """

    if history is None:
        return "No execution history available."

    try:

        # If history object has .steps
        if hasattr(history, "steps"):
            steps = history.steps

        else:
            steps = history

        if not isinstance(steps, list):
            return str(steps)[:6000]

        # Keep only limited number of steps
        steps = steps[:max_steps]

        compact = []

        for index, step in enumerate(
            steps,
            start=1
        ):

            # ------------------------------------------------
            # Dictionary step
            # ------------------------------------------------

            if isinstance(step, dict):

                line = step.get(
                    "line_number",
                    step.get("line", "?")
                )

                variables = step.get(
                    "variables",
                    {}
                )

                # Limit variables
                if isinstance(variables, dict):

                    small_variables = {}

                    for key, value in list(
                        variables.items()
                    )[:10]:

                        # Convert large values to short strings
                        value_text = str(value)

                        if len(value_text) > 200:
                            value_text = (
                                value_text[:200]
                                + "..."
                            )

                        small_variables[key] = value_text

                else:

                    small_variables = str(
                        variables
                    )[:500]

                compact.append(
                    f"Step {index}: "
                    f"Line {line}, "
                    f"Variables: {small_variables}"
                )

            # ------------------------------------------------
            # Object step
            # ------------------------------------------------

            else:

                line = getattr(
                    step,
                    "line_number",
                    getattr(step, "line", "?")
                )

                variables = getattr(
                    step,
                    "variables",
                    {}
                )

                if isinstance(
                    variables,
                    dict
                ):

                    small_variables = {}

                    for key, value in list(
                        variables.items()
                    )[:10]:

                        value_text = str(value)

                        if len(value_text) > 200:
                            value_text = (
                                value_text[:200]
                                + "..."
                            )

                        small_variables[key] = value_text

                else:

                    small_variables = str(
                        variables
                    )[:500]

                compact.append(
                    f"Step {index}: "
                    f"Line {line}, "
                    f"Variables: {small_variables}"
                )

        result = "\n".join(compact)

        # Final safety limit
        return result[:8000]

    except Exception as e:

        return (
            "Execution history could not be "
            f"processed: {str(e)[:300]}"
        )


# ============================================================
# AI CODE EXPLANATION
# ============================================================

def explain_code(code, history=None):
    """
    Explain Python code for beginners using Groq.
    """

    # --------------------------------------------------------
    # Limit source code size
    # --------------------------------------------------------

    if code is None:
        code = ""

    code = str(code)

    if len(code) > 12000:
        code = code[:12000] + "\n...code truncated..."


    # --------------------------------------------------------
    # Compact execution history
    # --------------------------------------------------------

    history_text = make_compact_history(
        history,
        max_steps=12
    )


    # ========================================================
    # PROMPT
    # ========================================================

    prompt = f"""
You are a Python teacher.

Explain the following Python program to a beginner.

PYTHON CODE:
--------------------
{code}
--------------------

EXECUTION HISTORY:
--------------------
{history_text}
--------------------

Use this structure:

## 1. What the code does
Explain the purpose of the program.

## 2. Line-by-line explanation
Explain the important lines simply.

## 3. Execution steps
Explain how the variables change.

## 4. Loop explanation
If there is a loop, explain each iteration.

## 5. Final output
Explain exactly what the program prints.

## 6. Real-life analogy
Give one simple analogy.

## 7. Common beginner mistakes
Mention relevant mistakes.

## 8. Short summary
Give a short 2-3 sentence summary.

Rules:
- Use simple English.
- Be technically correct.
- Do not invent execution results.
- Do not discuss unnecessary advanced concepts.
- Keep the answer concise.
"""


    # ========================================================
    # GROQ API CALL
    # ========================================================

    try:

        response = client.chat.completions.create(

            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a patient Python teacher "
                        "who explains programming clearly "
                        "to beginners."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            # Keep response reasonably small
            max_tokens=1800
        )

        return response.choices[0].message.content


    except Exception as e:

        error_text = str(e)

        # ----------------------------------------------------
        # Friendly 413 error
        # ----------------------------------------------------

        if "413" in error_text or "rate_limit_exceeded" in error_text:

            return """
## AI Explanation Failed

The request was too large for the current Groq limit.

The execution history has been reduced automatically.
Please try running the code again.

If this still happens, use a smaller Python program.
"""

        # ----------------------------------------------------
        # Authentication error
        # ----------------------------------------------------

        if "401" in error_text or "invalid_api_key" in error_text:

            return """
## AI Explanation Failed

Your Groq API key is invalid.

Check the GROQ_API_KEY value inside your .env file.
"""

        # ----------------------------------------------------
        # Other errors
        # ----------------------------------------------------

        return f"""
## AI Explanation Failed

Error:
{error_text}
"""


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("PYTHON AI VISUALIZER - AI TEST")
    print("=" * 60)

    test_code = """
x = 10

for i in range(3):
    x += 20

print(x)
"""

    result = explain_code(
        test_code
    )

    print("\nAI EXPLANATION:")
    print("-" * 60)

    print(result)

    print("-" * 60)

