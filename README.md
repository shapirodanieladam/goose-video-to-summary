# Video Transcription and Summary Tool

This tool extracts audio from video files, transcribes the content using OpenAI's Whisper model, and generates both a detailed transcript and an executive summary. It's particularly useful for creating VP-level summaries of video content.

## Prerequisites

- macOS (tested on macOS 14+)
- `ffmpeg` installed (for audio extraction)
- Hermit package manager (for Python environment)

## Installation

1. Clone the repository and navigate to the project directory:
```bash
mkdir audio_transcriber
cd audio_transcriber
```

2. Initialize Hermit:
```bash
curl -fsSL https://github.com/cashapp/hermit/releases/download/stable/install.sh | HERMIT_STATE_DIR=. bash
```

3. Install Python using Hermit:
```bash
./bin/hermit install python3-3.11.9
source bin/activate-hermit
```

4. Install required Python packages:
```bash
pip install openai-whisper tqdm
```

## Usage

1. Place your MP4 video file in your Downloads directory.

2. Run the script:
```bash
./audio_to_text.py
```

The script will:
- Find all MP4 files in your Downloads directory
- Extract audio to WAV format
- Transcribe the audio using Whisper
- Generate two files:
  - `[videoname].transcript.txt`: Detailed timestamped transcript
  - `[videoname].summary.txt`: Executive summary for VP+ level review

## Example Goose Prompt

Here's how to prompt Goose to create a video summary:

```
let's create an audio-to-text script using python. we can use `ffmpeg` on path to extract audio. the target file for audio extraction will be in the `.mp4` in `~/Downloads` (or your preferred location)
```

After initial setup, you can enhance the script with:

```
can you please use `ffmpeg` to "watch" the video file, in sync with your transcription? once you're ready, please create an executive summary suitable for managers of managers (VP+ level) to review (or your preferred content style)
```

This will create a script that:
1. Extracts audio from video
2. Creates timestamped transcripts
3. Generates executive summaries
4. Uses Whisper's medium model for better accuracy

## Output Files

The script generates two files for each video:

1. **Transcript** (`[videoname].transcript.txt`):
   - Timestamped transcription
   - Format: `[HH:MM:SS] Spoken text`
   - Complete word-by-word transcription

2. **Summary** (`[videoname].summary.txt`):
   - Video duration
   - Overview
   - Key points
   - Strategic value proposition
   - Formatted for desired audience

## Customization

You can modify the script to:
- Use different Whisper models (tiny, base, small, medium, large)
- Change output formats
- Adjust transcription parameters
- Customize summary format

## Notes

- The script uses the Whisper "medium" model for better accuracy
- First run will download the Whisper model (~1.42GB)
- Processing time depends on video length and CPU power
- Transcription runs on CPU; GPU support requires additional setup