# Video Analysis and Executive Summary Tool

This tool provides comprehensive video analysis through audio transcription, visual frame analysis, and executive summary generation. It's designed for creating VP-level summaries and detailed visual narratives from video content.

## Prerequisites

- macOS (tested on macOS 14+)
- `ffmpeg` installed (for audio/video processing)
- Hermit package manager (for Python environment)
- Python packages: openai-whisper, tqdm, pillow, numpy

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
pip install openai-whisper tqdm pillow numpy
```

## Usage

### Basic Audio Transcription

1. Place your MP4 video file in your Downloads directory.

2. Run the transcription script:
```bash
./audio_to_text.py
```

### Visual Frame Analysis

1. Extract frames from video:
```bash
mkdir -p frames
ffmpeg -i ~/Downloads/your_video.mp4 -vf "fps=1" frames/frame_%04d.jpg
```

2. Run the frame analysis script:
```bash
./analyze_frames.py
```

3. Run the texture analysis (optional):
```bash
./analyze_texture.py frames/frame_0001.jpg
```

## Goose Prompts for Different Outputs

### 1. Basic Audio Transcription
```
let's create an audio-to-text script using python. we can use `ffmpeg` on path to extract audio. the target file for audio extraction will be in the `.mp4` in `~/Downloads`
```

### 2. Visual Frame Analysis
```
let's try "watching" the video by using `ffmpeg` to isolate every frame of the video, write it to a separate file, and merge the files into one document of files. then, scan the document sequentially top to bottom, keeping a running context of what's happening by summarizing each document page
```

### 3. Detailed Visual Narrative
After running frame analysis:
```
let's follow the sequence further, all the way to the end, then create a visual narrative document
```
This will create `visual_narrative_detailed.txt` containing:
- Scene-by-scene breakdown
- Visual style analysis
- Narrative themes
- Production quality notes

### 4. Combined Executive Summary
After having both transcript and visual analysis:
```
can you please combine both the visual narrative analysis and creation we've done here, and the audio transcript work we did earlier, and use both to create an executive summary suitable for VP+ level?
```
This will create `executive_summary_combined.txt` containing:
- Business impact overview
- Key outcomes
- Strategic relevance
- Market implications
- ROI indicators

## Output Files

The tool generates several types of files:

1. **Transcript** (`[videoname].transcript.txt`):
   - Timestamped transcription
   - Word-by-word accuracy
   - Speaker context

2. **Visual Analysis** (`visual_narrative_detailed.txt`):
   - Scene-by-scene breakdown
   - Visual style notes
   - Narrative themes
   - Production quality assessment

3. **Executive Summary** (`executive_summary_combined.txt`):
   - Business impact overview
   - Strategic analysis
   - Market implications
   - Distribution recommendations

## Customization

You can modify the analysis by:
- Adjusting frame extraction rate
- Changing analysis depth
- Customizing summary format
- Targeting specific audience levels

## Best Practices

1. **Frame Extraction**:
   - Use 1 fps for standard analysis
   - Higher rates for fast-moving content
   - Lower rates for static content

2. **Analysis Sequence**:
   - Start with audio transcription
   - Follow with frame analysis
   - Combine for executive summary

3. **Summary Creation**:
   - Focus on business impact
   - Include concrete metrics
   - Highlight strategic relevance
   - Consider audience level

## Technical Notes

- Uses Whisper "medium" model for better accuracy
- First run downloads Whisper model (~1.42GB)
- Frame analysis works best with videos under 10 minutes
- High-resolution frame extraction preserves detail
- Processing time depends on video length and CPU power