# Installing WSL on Your Windows Computer

This guide provides step-by-step instructions to install the Windows Subsystem for Linux (WSL) on a Windows computer, allowing you to run a Linux environment directly on Windows.

## Prerequisites
- A Windows 10 (version 2004 or later) or Windows 11 computer.
- Administrator access to your Windows machine.
- An internet connection.

## Steps

### 1. Enable WSL
1. Open PowerShell as Administrator:
   - Press `Win + S`, type `PowerShell`, right-click, and select "Run as administrator".
2. Run the following command to enable WSL:
   ```
   wsl --install
   ```
   This command enables WSL and installs the default Linux distribution (usually Ubuntu).

3. Restart your computer when prompted.

### 2. Install a Linux Distribution
1. After restarting, WSL will automatically start installing the default Linux distribution.
2. Alternatively, open the Microsoft Store, search for a Linux distribution (e.g., Ubuntu, Debian, or Kali), and install your preferred one.
3. Once installed, launch the distribution from the Start menu or by typing `wsl` in PowerShell.

### 3. Set Up Your Linux Distribution
1. The first time you launch the Linux distribution, it will prompt you to create a username and password.
2. Follow the on-screen instructions to complete the setup.

### 4. Update Your Linux Distribution
1. Open your Linux distribution's terminal.
2. Run the following commands to update the package lists and upgrade installed packages:
   ```
   sudo apt update
   sudo apt upgrade
   ```
   Note: Commands may vary depending on the Linux distribution (e.g., use `yum` or `dnf` for Red Hat-based distributions).

### 5. (Optional) Set WSL 2 as Default
WSL 2 offers improved performance over WSL 1. To ensure you're using WSL 2:
1. Open PowerShell as Administrator.
2. Set WSL 2 as the default version:
   ```
   wsl --set-default-version 2
   ```
3. Verify your distribution is running WSL 2:
   ```
   wsl --list --verbose
   ```
   Look for `WSL 2` next to your distribution name.

### 6. Test Your Installation
1. Open your Linux distribution's terminal.
2. Run a simple command to confirm it’s working, e.g.:
   ```
   lsb_release -a
   ```
   This displays the Linux distribution’s version information.

## Troubleshooting
- If `wsl --install` fails, ensure the "Windows Subsystem for Linux" feature is enabled:
  1. Go to `Control Panel > Programs > Turn Windows features on or off`.
  2. Check "Windows Subsystem for Linux" and click "OK".
  3. Restart your computer and retry.
- For additional help, run `wsl --help` or visit Microsoft’s WSL documentation.

## Additional Notes
- You can access your Windows files from Linux at `/mnt/c/`.
- To access Linux files from Windows, use File Explorer and navigate to `\\wsl$\`.
- Install additional tools (e.g., `git`, `python`) in your Linux distribution as needed.