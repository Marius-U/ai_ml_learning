#!/bin/bash
#
# ML Training Environment Activation Script
# ========================================
#
# This script activates the ML environment and starts Jupyter notebook
#
# Usage:
#   bash activate_and_start.sh
#   or make it executable: chmod +x activate_and_start.sh && ./activate_and_start.sh

echo "🚀 Starting ML Training Environment"
echo "=================================="

# Check if virtual environment exists
if [ ! -d "$HOME/venv/ml-env" ]; then
    echo "❌ Virtual environment not found at ~/venv/ml-env"
    echo "💡 Please create it first:"
    echo "   python -m venv ~/venv/ml-env"
    echo "   source ~/venv/ml-env/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

echo "🔧 Activating ML environment..."
source ~/venv/ml-env/bin/activate

echo "📦 Checking environment..."
python scripts/setup_environment.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎯 Starting Jupyter notebook..."
    echo "📖 Opening main training notebook..."
    echo ""
    echo "🌟 Navigate to: notebooks/ml_ai_101_training_complete.ipynb"
    echo "📋 Or check: notebooks/README.md for guidance"
    echo ""

    # Start Jupyter notebook
    jupyter notebook notebooks/ml_ai_101_training_complete.ipynb
else
    echo ""
    echo "❌ Environment validation failed"
    echo "💡 Please check the errors above and fix any missing dependencies"
    echo "   pip install -r requirements.txt"
fi