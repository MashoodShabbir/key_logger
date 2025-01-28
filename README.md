# Keylogger
A simple keylogger script written in Python that records keystrokes and sends logs to a specified email address at regular intervals. For educational purposes only.

## Features
- Keystroke logging with timestamps.

- Automated email reports at configurable intervals.

- Command-line configuration for email, password, and reporting interval.

- Lightweight and cross-platform (requires Python 3.x).

## Disclaimer
⚠️ This tool is intended for educational and ethical use only.
Unauthorized monitoring of keystrokes on devices you do not own or have explicit permission to access is illegal.
The developers assume no liability for misuse of this software.

## Installation
Clone the repository:

```bash
git clone https://github.com/MashoodShabbir/key_logger.git
cd keylogger
```
## Install dependencies:
```bash
pip install pynput
```
## Configuration (Gmail Example)
1. Enable 2-Step Verification for your Gmail account:
    - Go to Google Account Security → Enable "2-Step Verification."

2. Create an App Password:
    - Visit App Passwords.

    - Generate a password for the "Other" app type (e.g., name it "Keylogger").

    - Use this 16-character password in the script.

## Usage
```bash
python keylogger.py -e your.email@gmail.com -p YOUR_APP_PASSWORD -i 60
```
    - -e / --email: Your Gmail address.

    - -p / --password: App-specific password (see Configuration).

    - -i / --interval: Time interval (in seconds) between email reports.

## How It Works
1. Keystroke Capture: Uses pynput to monitor keyboard input.

2. Logging: Stores keystrokes in memory, handling special keys (e.g., spaces).

3. Email Reporting: Sends encrypted logs via SMTP (Gmail) at specified intervals.

4. Threading: Runs the email scheduler in the background to avoid interrupting key capture.

## Notes
- Gmail Required: The script is configured for Gmail's SMTP server. Modify smtp.gmail.com and the port in the code for other providers.

- Security: Never hardcode credentials in the script. Use environment variables or input arguments.

- Ethics: Use responsibly and only on devices you own or have explicit authorization to test.
