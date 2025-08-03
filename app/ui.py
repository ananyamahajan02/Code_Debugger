import gradio as gr
from agents.agent_config import DebuggingAgent
from gradio.themes.ocean import Ocean

agent = DebuggingAgent()

def debug_and_fix(code: str, suggest_fix: bool):
    if not code.strip():
        return "⚠️ Please enter valid Python code.", ""

    try:
        debug_output = agent.run(code, suggest_fix=False)

        if suggest_fix:
            fix_output = agent.run(code, suggest_fix=True)
        else:
            fix_output = "✅ No fix requested."

        return debug_output, fix_output

    except Exception as e:
        return f"❌ Unexpected error:\n{str(e)}", ""

with gr.Blocks(theme=Ocean()) as demo:
    gr.Markdown(
        """
        <h1 style='text-align: center; color: #4EA8DE;'>🛠️ Python Code Debugger</h1>
        <p style='text-align: center; font-size: 16px;'>Paste your Python code below. Get error feedback and optionally a suggested fix!</p>
        """
    )

    with gr.Column():
        code_input = gr.Textbox(
            lines=12,
            label="👩‍💻 Python Code Input",
            placeholder="Paste your Python code here...",
            show_copy_button=True
        )

        suggest_checkbox = gr.Checkbox(
            label="💡 Suggest Fix",
            value=False
        )

        run_button = gr.Button("🚀 Run Debugger")

    # Grouped Output Area
    with gr.Group():

        with gr.Row():
            debug_output = gr.Textbox(
                lines=10,
                label="🐞 Debugging Result",
                interactive=False,
                show_copy_button=True,
                placeholder="This section shows error analysis..."
            )

            fix_output = gr.Textbox(
                lines=10,
                label="🛠 Suggested Fix",
                interactive=False,
                show_copy_button=True,
                placeholder="The suggested fixed code will appear here..."
            )

    run_button.click(
        fn=debug_and_fix,
        inputs=[code_input, suggest_checkbox],
        outputs=[debug_output, fix_output]
    )

if __name__ == "__main__":
    demo.launch()
