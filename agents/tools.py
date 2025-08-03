import traceback
import logging

class DebugTool:
    def __call__(self, code: str) -> str:  # ✅ Fixed
        logging.info("Executing submitted code...")
        try:
            local_vars = {}
            exec(code, {}, local_vars)
            logging.info("Code executed without error.")
            return "✅ Code executed successfully — no errors found."
        except Exception:
            error_trace = traceback.format_exc()
            logging.warning("Error during code execution.")
            return f"❌ Error during code execution:\n{error_trace}"
