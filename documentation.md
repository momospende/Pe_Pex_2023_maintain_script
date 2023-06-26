# Documentation: Configuring Visual Studio Code for Python Development

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Setting Up Python Development in Visual Studio Code](#setting-up-python-development-in-visual-studio-code)
   4.1. [Installing the Python Extension](#installing-the-python-extension)
   4.2. [Setting Up a Python Interpreter](#setting-up-a-python-interpreter)
   4.3. [Enabling Autocompletion and IntelliSense](#enabling-autocompletion-and-intellisense)
   4.4. [Configuring the Debugger](#configuring-the-debugger)
5. [Incorporating Virtual Environments](#incorporating-virtual-environments)
   5.1. [Creating a Virtual Environment](#creating-a-virtual-environment)
   5.2. [Activating the Virtual Environment](#activating-the-virtual-environment)
6. [Selecting the Virtual Environment for a Workspace](#selecting-the-virtual-environment-for-a-workspace)
7. [Running Python Applications in a Virtual Environment](#running-python-applications-in-a-virtual-environment)
8. [Conclusion](#conclusion)

## 1. Introduction
This documentation provides step-by-step instructions for configuring Microsoft Visual Studio Code for Python scripting. It covers the setup of Python development, enabling autocompletion, IntelliSense, and debugging features. Additionally, it explains how to incorporate virtual environments for isolated package management and run Python applications within those environments.

## 2. Prerequisites
- Microsoft Visual Studio Code installed on your system.
- Python installed on your system.

## 3. Installation
- Download and install Visual Studio Code from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/).
- Install Python by downloading the installer from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

## 4. Setting Up Python Development in Visual Studio Code

### 4.1. Installing the Python Extension
- Launch Visual Studio Code.
- Click on the Extensions icon in the sidebar (or press `Ctrl+Shift+X`).
- Search for "Python" in the extensions marketplace.
- Click on the "Python" extension offered by Microsoft and click the Install button.
- Wait for the installation to complete and restart Visual Studio Code if prompted.

### 4.2. Setting Up a Python Interpreter
- Open a Python file or create a new one with the `.py` extension.
- If prompted, select a Python interpreter. If no prompt appears, follow the next step.
- Open the Command Palette by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
- Type "Python: Select Interpreter" and select the desired interpreter from the list.

### 4.3. Enabling Autocompletion and IntelliSense
- Visual Studio Code's Python extension provides automatic IntelliSense and autocompletion for Python code.
- As you start typing Python code, suggestions and completions will automatically appear.

### 4.4. Configuring the Debugger
- Open the Python file you want to debug.
- Place breakpoints in the code by clicking on the left gutter of the editor or pressing `F9`.
- Open the Debug view by clicking on the bug icon in the sidebar (or press `Ctrl+Shift+D`).
- Click on the gear icon and choose "Python" from the environment options.
- Click on the green play button to start debugging.
- The debugger will pause at breakpoints and allow you to inspect variables and step through the code.

## 5. Incorporating Virtual Environments

### 5.1. Creating a Virtual Environment
- Open a terminal within Visual Studio Code by going to View > Terminal or pressing ``Ctrl+` ``.
- In the terminal, navigate to the directory where you want to create the virtual environment for your project.
- Run the command to create a virtual environment using `venv`:

```bash
python -m venv venv

## 5.2. Activating the Virtual Environment

In the terminal, run the command to activate the virtual environment:
source venv/bin/activate

The terminal prompt should now indicate that you are working within the virtual environment.

## 6. Selecting the Virtual Environment for a Workspace

1. Open the workspace for the desired application in Visual Studio Code.
2. If the virtual environment is not already activated, follow the steps mentioned in the previous section to activate it.
3. Ensure that the Python interpreter used within the workspace is set to the virtual environment you created.

## 7. Running Python Applications in a Virtual Environment

1. Open the main Python file of the application in Visual Studio Code.
2. Configure the launch configuration for the application by following these steps:
   - Press `Ctrl+Shift+D` to open the Debug view.
   - Click on the gear icon (Configure gear icon) in the top-right corner of the Debug view and choose "Python" from the environment options.
   - A launch configuration file named `launch.json` will open with default settings.
3. Set any desired breakpoints in the code by clicking on the left gutter of the editor or pressing `F9`.
4. Press `F5` or click on the green play button in the Debug view to start running the application in debug mode.
5. The application will execute, and if there are any breakpoints, the execution will pause at those points, allowing you to inspect variables and step through the code.

## 8. Conclusion

Congratulations! You have successfully configured Microsoft Visual Studio Code for Python scripting. You can now take advantage of features such as autocompletion, IntelliSense, and the debugger. By incorporating virtual environments, you can maintain package isolation and run Python applications within specific environments.

