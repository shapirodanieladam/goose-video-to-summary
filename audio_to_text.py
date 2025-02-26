#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
import json
import whisper
from datetime import timedelta

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS format."""
    return str(timedelta(seconds=round(seconds)))

def extract_audio(video_path, output_path):
    """Extract audio from video file using ffmpeg."""
    command = [
        'ffmpeg',
        '-i', str(video_path),
        '-vn',  # No video
        '-acodec', 'pcm_s16le',  # Convert to WAV
        '-ar', '16000',  # 16kHz sample rate
        '-ac', '1',  # Mono
        '-y',  # Overwrite output file if exists
        str(output_path)
    ]
    
    try:
        subprocess.run(command, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def get_video_duration(video_path):
    """Get video duration using ffprobe."""
    command = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_format',
        str(video_path)
    ]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        data = json.loads(result.stdout)
        return float(data['format']['duration'])
    except (subprocess.CalledProcessError, KeyError, json.JSONDecodeError) as e:
        print(f"Error getting video duration: {e}")
        return None

def transcribe_audio(audio_path):
    """Transcribe audio file using OpenAI Whisper."""
    try:
        print("Loading Whisper model...")
        # Use the medium model for better accuracy
        model = whisper.load_model("medium")
        
        print("Transcribing audio...")
        result = model.transcribe(
            str(audio_path),
            word_timestamps=True,
            language="en"
        )
        
        return result
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

def write_transcript(result, output_file):
    """Write timestamped transcript to file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("TIMESTAMPED TRANSCRIPT\n")
        f.write("===================\n\n")
        
        current_segment = {"text": "", "start": 0}
        
        for segment in result["segments"]:
            timestamp = format_timestamp(segment["start"])
            text = segment["text"].strip()
            f.write(f"[{timestamp}] {text}\n")

def create_executive_summary(transcript_path, video_duration, output_path):
    """Create an executive summary from the transcript."""
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    
    summary_prompt = f"""Video Duration: {format_timestamp(video_duration)}

Executive Summary
================
{transcript}

Key Points:
1. 
2. 
3. 

Target Audience: VP+ level executives
Purpose: Quick understanding of video content
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary_prompt)
    
    print(f"\nPlease review and complete the executive summary at: {output_path}")

def process_video(video_path):
    """Process a single video file."""
    # Create temporary WAV file
    temp_audio = video_path.with_suffix('.wav')
    
    # Get video duration
    duration = get_video_duration(video_path)
    if duration is None:
        return
    
    # Extract audio
    print(f"Extracting audio from {video_path}")
    if not extract_audio(video_path, temp_audio):
        return
    
    # Transcribe
    result = transcribe_audio(temp_audio)
    if result:
        # Save detailed transcript
        transcript_file = video_path.with_suffix('.transcript.txt')
        write_transcript(result, transcript_file)
        print(f"Detailed transcript saved to {transcript_file}")
        
        # Create executive summary template
        summary_file = video_path.with_suffix('.summary.txt')
        create_executive_summary(transcript_file, duration, summary_file)
    
    # Cleanup
    if temp_audio.exists():
        temp_audio.unlink()

def main():
    # Get downloads directory
    downloads_dir = Path.home() / "Downloads"
    
    # Find all MP4 files
    mp4_files = list(downloads_dir.glob("*.mp4"))
    
    if not mp4_files:
        print("No MP4 files found in Downloads directory")
        return
    
    print(f"Found {len(mp4_files)} MP4 files")
    
    # Process each video
    for video_path in mp4_files:
        print(f"\nProcessing {video_path}")
        process_video(video_path)

if __name__ == "__main__":
    main()