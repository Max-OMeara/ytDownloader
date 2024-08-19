# YouTube Video Downloader

## Project Overview

The YouTube Video Downloader is a Python-based application that allows users to download videos from YouTube by simply providing a video link. The application features a straightforward graphical user interface (GUI) created with Tkinter, making it easy for users to select the download path and initiate the download process.

## Features

- **Download YouTube Videos**: Users can input a YouTube video link and download the video in its highest available resolution.
- **Select Download Path**: Users can choose the directory where the downloaded video will be saved.
- **Simple GUI**: The application includes a user-friendly interface created with Tkinter, allowing easy interaction for users.

#Project Purpose
This project was developed to practice Python programming, specifically focusing on GUI development with Tkinter and working with external libraries like pytube and moviepy. It serves as a practical tool for downloading YouTube videos without paying for YouTube premium, and the source code can be further expanded with additional features.

## Technologies Used

- **Python**: The core programming language used for the application.
- **Tkinter**: Used to build the graphical user interface (GUI).
- **pytube**: A Python library used to download YouTube videos.
- **moviepy**: Used for processing video files.
- **shutil**: A Python module for high-level file operations, used to move the downloaded files.

## File Structure

- **main.py**: The main script that contains the code for the YouTube Video Downloader.
- **distutils.errors**: Used for handling template errors.
- **tkinter**: Used for the GUI components, such as labels, buttons, and entry fields.
- **pytube**: Handles downloading the YouTube videos.
- **moviepy.editor**: Processes and closes the video files after download.

## Installation

To run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yt-downloader.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd yt-downloader
   ```

3. **Install dependencies**:
   Make sure you have Python installed, then install the required libraries using pip:
   ```bash
   pip install pytube moviepy
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Contributing

Contributions to this project are welcome! If you have ideas for new features or improvements, feel free to fork the repository, make your changes, and submit a pull request.

## Future Plans

- **Error Handling**: Implement better error handling for invalid URLs and download issues.


## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

## Acknowledgments

This project was created as a learning exercise to improve my understanding of Python and GUI development. It has been a rewarding experience, and I hope others find it useful for downloading YouTube videos.

---

Feel free to adapt the README according to any additional details or changes in your project.
