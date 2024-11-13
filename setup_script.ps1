# Define the root directory for your project
$rootDir = "guilliman-40000"

# Create directories
$dirs = @(
    "$rootDir/src/classes",
    "$rootDir/tests",
    "$rootDir/data",
    "$rootDir/docs"
)

# Create each directory
foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir
}

# Create files
$files = @(
    "$rootDir/README.md",
    "$rootDir/requirements.txt",
    "$rootDir/setup.py",
    "$rootDir/.gitignore",
    "$rootDir/src/__init__.py",
    "$rootDir/src/main.py",
    "$rootDir/src/utils.py",
    "$rootDir/src/classes/__init__.py",
    "$rootDir/src/classes/class1.py",
    "$rootDir/src/classes/class2.py",
    "$rootDir/tests/__init__.py",
    "$rootDir/tests/test_class1.py",
    "$rootDir/tests/test_class2.py",
    "$rootDir/tests/test_utils.py",
    "$rootDir/data/example_data.csv",
    "$rootDir/docs/index.md"
)

# Create each file
foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file
}

# Optional: Write initial content into some of the files
Add-Content -Path "$rootDir/README.md" -Value "# Project Name"
Add-Content -Path "$rootDir/setup.py" -Value "from setuptools import setup, find_packages\n\nsetup(\n    name='project_name',\n    version='0.1',\n    packages=find_packages(where='src'),\n    package_dir={'': 'src'},\n)"
