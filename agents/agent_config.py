import os
import logging
from dotenv import load_dotenv
from agents.tools import DebugTool
from openai import OpenAI

load_dotenv()

class DebuggingAgent:
    def __init__(self):  # ✅ Fixed
        self.debug_tool = DebugTool()
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, code: str, suggest_fix: bool = False) -> str:
        try:
            logging.info("Running debug tool...")
            debug_output = self.debug_tool(code)
            logging.info("Debugging completed.")
        except Exception as e:
            logging.exception("Error while debugging code.")
            return f"❌ Debug tool failed:\n{str(e)}"

        if not suggest_fix:
            return debug_output

        try:
            logging.info("User requested suggested fix. Calling OpenAI model...")
            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful AI that corrects Python code errors."},
                    {"role": "user", "content": f"Fix this Python code:\n\n{code}\n\nAlso refer to this debug output:\n{debug_output}.Only give the correct code as a reply and do not use any additional statement"}
                ],
                temperature=0.2
            )
            fixed_code = response.choices[0].message.content.strip()
            logging.info("Fix suggestion completed.")
            return fixed_code

        except Exception as e:
            logging.exception("Error while generating suggested fix.")
            return debug_output + f"\n\n⚠ Failed to generate fix:\n{str(e)}"
