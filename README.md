# AutoDep Project

This project uses uv for dependency management, lean-interact for Lean 4 integration, and the OpenAI API for autoformalizing mathematical statements from the ProofNet dataset.

## Prerequisites

### Install Lean 4 and elan

This project requires Lean 4 and elan (Lean version manager). Choose one of the installation methods below:

#### Option 1: Cross-platform install-lean command (Recommended)
```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
```

#### Option 2: Platform-specific installation

**macOS:**
```bash
brew install elan-lean
```

**Linux:**
```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

**Windows:**
Download and run the installer from [Lean 4 releases](https://github.com/leanprover/lean4/releases)

#### Verify installation
```bash
elan --version  # Should be >= 4.0.0
lean --version  # Should show Lean 4.x.x
```

### Other Requirements
- Python >= 3.10 (this project uses 3.12+)
- git

## Setup

1. **Activate the virtual environment:**
   ```
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```
   uv sync --group dev
   ```

3. **Set up pre-commit hooks (optional but recommended):**
   ```
   source .venv/bin/activate
   pre-commit install
   ```

4. **Set your OpenAI API key:** (Replace `your_key_here` with your actual key)
   ```
   export OPENAI_API_KEY=your_key_here
   ```

5. **Run the main script:**
   ```
   python main.py
   ```

## What it does
- Loads the ProofNet Lean 4 dataset.
- Generates mathematical implications from informal statements using GPT-4o-mini.
- Formalizes both original statements and generated implications into Lean 4 theorems.
- Calculates BLEU scores to measure formalization quality.
- Outputs results to `data/proofnet/generated_implications.jsonl`.

## Dependencies
This project uses:
- **lean-interact**: For Lean 4 integration and theorem proving capabilities
- **OpenAI API**: For generating and formalizing mathematical statements
- **NLTK**: For BLEU score calculations
- **Datasets**: For loading the ProofNet dataset
