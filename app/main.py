from dotenv import load_dotenv
load_dotenv()

import logging
from agents.agent_config import DebuggingAgent
from examples.sample_code import code

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    print("🔍 Debugging Code:\n")
    agent = DebuggingAgent()

    # Always debug first
    result = agent.run(code, suggest_fix=False)

    print("\n🧠 Output:\n")
    print(result)

    # Ask after debugging
    fix = input("\nWould you like the agent to suggest a fix? (y/n): ").strip().lower()
    if fix == "y":
        fixed_code = agent.run(code, suggest_fix=True)
        print("\n🛠 Suggested Fix:\n")
        print(fixed_code)
    else:
        print("\n✅ No fix requested.")

if __name__ == "__main__":  # ✅ Fixed
    main()
