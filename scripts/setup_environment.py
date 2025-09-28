#!/usr/bin/env python3
"""
Environment Setup and Validation Script
=======================================

This script validates the ML environment and installs missing dependencies.

Usage:
    python scripts/setup_environment.py
    python scripts/setup_environment.py --install-missing
"""

import sys
import subprocess
import importlib
import argparse

# Required packages with minimum versions
REQUIRED_PACKAGES = {
    'numpy': '1.20.0',
    'pandas': '1.3.0',
    'matplotlib': '3.5.0',
    'seaborn': '0.11.0',
    'scikit-learn': '1.0.0',
    'scipy': '1.7.0',
    'jupyter': '1.0.0',
    'notebook': '6.4.0',
}

OPTIONAL_PACKAGES = {
    'joblib': '1.0.0',
    'requests': '2.25.0',
    'plotly': '5.0.0',
    'xgboost': '1.5.0',
}

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ required. Current version:", sys.version)
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_package(package_name, min_version=None):
    """Check if a package is installed and meets version requirements"""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')

        if min_version and version != 'unknown':
            from packaging import version as pkg_version
            if pkg_version.parse(version) < pkg_version.parse(min_version):
                return False, version, f"Version {version} < required {min_version}"

        return True, version, "OK"
    except ImportError:
        return False, None, "Not installed"

def install_package(package_name):
    """Install a package using pip"""
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", package_name
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Main environment validation function"""
    parser = argparse.ArgumentParser(description='ML Environment Setup and Validation')
    parser.add_argument('--install-missing', action='store_true',
                       help='Automatically install missing packages')
    args = parser.parse_args()

    print("🔧 ML ENVIRONMENT VALIDATION")
    print("=" * 50)

    # Check if virtual environment is activated
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
        print(f"   Environment path: {sys.prefix}")
    else:
        print("⚠️  No virtual environment detected")
        print("💡 Recommended: Activate virtual environment first:")
        print("   source ~/venv/ml-env/bin/activate")
        print("   Then run this script again")
        print()

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    print(f"\n📦 Checking Required Packages:")
    missing_packages = []

    for package, min_version in REQUIRED_PACKAGES.items():
        installed, version, status = check_package(package, min_version)

        if installed:
            print(f"  ✅ {package}: {version}")
        else:
            print(f"  ❌ {package}: {status}")
            missing_packages.append(package)

    print(f"\n📦 Checking Optional Packages:")
    optional_missing = []

    for package, min_version in OPTIONAL_PACKAGES.items():
        installed, version, status = check_package(package, min_version)

        if installed:
            print(f"  ✅ {package}: {version}")
        else:
            print(f"  ⚠️  {package}: {status}")
            optional_missing.append(package)

    # Summary
    print(f"\n📊 Summary:")
    print(f"  Required packages missing: {len(missing_packages)}")
    print(f"  Optional packages missing: {len(optional_missing)}")

    if missing_packages:
        print(f"\n❌ Missing required packages: {', '.join(missing_packages)}")

        if args.install_missing:
            print(f"\n🔧 Installing missing packages...")
            for package in missing_packages:
                print(f"  Installing {package}...")
                if install_package(package):
                    print(f"  ✅ {package} installed successfully")
                else:
                    print(f"  ❌ Failed to install {package}")
        else:
            print(f"\n💡 To install missing packages, run:")
            print(f"   pip install {' '.join(missing_packages)}")
            print(f"   Or use: python scripts/setup_environment.py --install-missing")
    else:
        print(f"\n✅ All required packages are installed!")

    if optional_missing:
        print(f"\n💡 Optional packages for enhanced features:")
        print(f"   pip install {' '.join(optional_missing)}")

    # Test environment
    print(f"\n🧪 Testing ML imports...")
    try:
        import numpy as np
        import pandas as pd
        import sklearn
        print("  ✅ Core ML libraries working")

        # Test basic functionality
        X = np.random.rand(10, 3)
        df = pd.DataFrame(X)
        assert df.shape == (10, 3)
        print("  ✅ Basic functionality test passed")

    except Exception as e:
        print(f"  ❌ Environment test failed: {e}")
        sys.exit(1)

    print(f"\n🎉 Environment validation complete!")

    if not missing_packages:
        print(f"🚀 Ready to start ML training!")

if __name__ == "__main__":
    main()