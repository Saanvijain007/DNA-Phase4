#!/bin/bash
# Quick setup script for Pandora Chronicles Database System

echo "=== Pandora Chronicles - Environment Setup ==="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install -q pymysql cryptography

echo ""
echo "✓ Setup complete!"
echo ""
echo "To run the application:"
echo "  1. source venv/bin/activate"
echo "  2. cd src"
echo "  3. python main_app.py"
echo ""
