# Password Filter Application

## Overview

The Password Filter Application is a Python Tkinter-based utility that allows you to filter a list of passwords according to specific criteria. It checks the passwords in a text file and filters out those that do not meet the criteria. This application is useful for managing password lists and ensuring they meet certain security standards.



## Features

- Upload a text file containing a list of passwords.
- Apply filtering criteria to the passwords in the file:
  - Length between 8 and 16 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one digit.
  - At least one special character from: `#`, `!`, `*`, `%`, `-`, `_`, or `=`.
  - No special characters such as `ü`, `Æ`, `ñ`, `ß`, `Ø`, or spaces.
- View the filtered passwords in a user-friendly interface.
- Download the filtered passwords as a text file.

## Technologies Used

- Python 3.6 or later
- Tkinter for the graphical user interface

## Installation

1. Make sure you have Python 3.6 or later installed.
2. Clone this repository to your local machine.
3. Run the application by executing `python main.py` in your terminal.

## Usage

1. Click the "Upload File" button to select a text file containing passwords.
2. The application will filter the passwords based on the criteria.
3. Filtered passwords will be displayed in the text area.
4. Click the "Download Filtered Passwords" button to save the filtered passwords to a text file.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
