# Audio Optimization

- Automatic optimization of audio parameters
- Volume normalization
- Conversion to a standard format (mono, 44.1kHz, 16-bit)
- Error handling with detailed messages
- Colorful, styled terminal interface
- Support for multiple audio formats

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- ffmpeg (library for audio and video processing)

## Installation

1. Clone the repository or download the project files.

```bash
git clone git@github.com:hectorOliSan/optimize-audio.git
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
optimize-audio/
├── output/              # Directory where optimized audio files are stored
├── main.py              # Main file with generator logic
├── decorators.py        # Decorators for error handling and styling
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md
```

### Dependencies

- `pydub`: Library for manipulating and processing audio files
- `rich`: Library for terminal styling and colors

## Usage

```bash
python main.py <audio_file>
```

- `<audio_file>`: Path to the audio file to optimize.

### Example

```bash
python main.py audio.mp3
```

## Output

Optimized files are saved in the `output/` directory, which is created automatically if it doesn't exist.

