import streamlit as st
from tracer import PythonTracer
from model import explain_code


st.set_page_config(
    page_title="Python AI Visualizer",
    page_icon="🐍",
    layout="wide"
)


st.title("🐍 Python AI Visualizer")
st.caption("Understand your Python code execution step-by-step with AI")


# ============================================================
# CODE INPUT
# ============================================================

st.subheader("💻 Enter Python Code")

default_code = """x = 10

for i in range(3):
    x += 20

print(x)
"""

code = st.text_area(
    "Write your Python code:",
    value=default_code,
    height=250
)


# ============================================================
# RUN CODE
# ============================================================

if st.button("▶ Run Code", use_container_width=True):

    if not code.strip():
        st.warning("Please enter some Python code.")
        st.stop()

    tracer = PythonTracer()

    try:
        result = tracer.run(code)

        # Your tracer returns a list
        if isinstance(result, list):
            steps = result

        elif hasattr(result, "steps"):
            steps = result.steps

        else:
            steps = []

        st.session_state["steps"] = steps
        st.session_state["code"] = code

        st.success(
            f"Execution completed! {len(steps)} steps captured."
        )

    except Exception as e:
        st.error(f"Execution Error: {e}")
        st.stop()


# ============================================================
# VISUALIZATION
# ============================================================

if "steps" in st.session_state:

    steps = st.session_state["steps"]
    code = st.session_state["code"]

    st.divider()
    st.header("📊 Execution Visualization")

    if len(steps) == 0:

        st.warning("No execution steps were captured.")

    else:

        step_number = st.slider(
            "Move through execution:",
            min_value=1,
            max_value=len(steps),
            value=1
        )

        step = steps[step_number - 1]

        st.subheader(
            f"🔹 Step {step_number} / {len(steps)}"
        )

        # ====================================================
        # LINE NUMBER
        # ====================================================

        if isinstance(step, dict):

            line_number = step.get(
                "line_number",
                step.get("line", -1)
            )

        else:

            line_number = getattr(
                step,
                "line_number",
                -1
            )


        # ====================================================
        # CURRENT LINE
        # ====================================================

        if line_number != -1:

            st.info(
                f"📍 Currently executing line: **{line_number}**"
            )


        # ====================================================
        # VARIABLES
        # ====================================================

        st.subheader("📦 Variables")

        if isinstance(step, dict):

            variables = step.get(
                "variables",
                {}
            )

        else:

            variables = getattr(
                step,
                "variables",
                {}
            )


        if variables:

            cols = st.columns(len(variables))

            for col, (name, value) in zip(
                cols,
                variables.items()
            ):

                with col:

                    st.metric(
                        label=name,
                        value=str(value)
                    )

        else:

            st.info("No variables at this step.")


        # ====================================================
        # SOURCE CODE
        # ====================================================

        st.subheader("📝 Code")

        lines = code.splitlines()

        for i, line in enumerate(lines, start=1):

            if i == line_number:

                st.markdown(
                    f"""
                    <div style="
                        background-color:#1f6f43;
                        padding:12px;
                        border-radius:8px;
                        margin-bottom:6px;
                        color:white;
                    ">
                        <b>▶ {i}</b>
                        &nbsp;&nbsp;
                        {line}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.code(
                    f"{i}: {line}",
                    language="python"
                )


# ============================================================
# AI EXPLANATION
# ============================================================

if "steps" in st.session_state:

    steps = st.session_state["steps"]
    code = st.session_state["code"]

    st.divider()

    st.header("🤖 AI Explanation")

    if st.button(
        "🧠 Explain This Code with AI",
        use_container_width=True
    ):

        with st.spinner("AI is analyzing your code..."):

            try:

                explanation = explain_code(
                    code,
                    steps
                )

                if explanation:
                    st.markdown(explanation)
                else:
                    st.warning(
                        "AI returned an empty explanation."
                    )

            except Exception as e:

                st.error(
                    f"AI explanation failed: {e}"
                )