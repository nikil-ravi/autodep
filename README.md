# AutoDep Project

This project uses uv for dependency management and the OpenAI API for autoformalizing mathematical statements from the ProofNet dataset.

## Setup

1. **Activate the virtual environment:**
   ```
   source .venv/bin/activate
   ```

2. **Set your OpenAI API key:** (Replace `your_key_here` with your actual key)
   ```
   export OPENAI_API_KEY=your_key_here
   ```

3. **Run the main script:**
   ```
   python main.py
   ```

## What it does
- Loads the ProofNet Lean 4 dataset.
- Logs the first example.
- Uses OpenAI's GPT-4o-mini to generate a formalized Lean 4 theorem from the informal statement.
- Logs the formalized statement.



