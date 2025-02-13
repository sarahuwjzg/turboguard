# TurboGuard

TurboGuard is a simple Python program designed for Windows that allows users to generate desktop shortcuts for frequently accessed files or URLs. This tool simplifies the process of creating shortcuts, making it easier to access important documents or websites directly from your desktop.

## Features

- Create shortcuts for both files and URLs.
- Customizable shortcut names.
- Option to specify a working directory and icon for file shortcuts.

## Requirements

- Python 3.x
- `pywin32` package
- `winshell` package

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/TurboGuard.git
   cd TurboGuard
   ```

2. Install the required packages.
   ```bash
   pip install pywin32 winshell
   ```

## Usage

Run the script using Python:

```bash
python TurboGuard.py
```

Follow the on-screen prompts to create shortcuts:

1. Choose whether to create a file or URL shortcut.
2. Enter the necessary details such as the shortcut name, target file path or URL, and optional working directory or icon path.
3. The shortcut will be created on your desktop.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please open an issue on this repository.