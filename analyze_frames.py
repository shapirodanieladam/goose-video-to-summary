#!/usr/bin/env python3
import os
from pathlib import Path
import json
from datetime import timedelta

def frame_to_timestamp(frame_num, fps=1):
    """Convert frame number to timestamp."""
    seconds = frame_num / fps
    return str(timedelta(seconds=seconds))

def analyze_frames():
    """Analyze frames sequentially and build a narrative."""
    frames_dir = Path("frames")
    frames = sorted(frames_dir.glob("frame_*.jpg"))
    
    narrative = []
    current_scene = {
        "start_frame": 1,
        "end_frame": 1,
        "context": "",
        "frames": []
    }
    
    # Process each frame
    for frame_path in frames:
        frame_num = int(frame_path.stem.split("_")[1])
        timestamp = frame_to_timestamp(frame_num)
        
        # Add frame to current scene
        current_scene["frames"].append({
            "frame": frame_num,
            "timestamp": timestamp,
            "path": str(frame_path)
        })
        current_scene["end_frame"] = frame_num
        
        # Every 5 frames, create a scene summary
        if len(current_scene["frames"]) >= 5:
            narrative.append(current_scene)
            current_scene = {
                "start_frame": frame_num + 1,
                "end_frame": frame_num + 1,
                "context": "",
                "frames": []
            }
    
    # Add any remaining frames
    if current_scene["frames"]:
        narrative.append(current_scene)
    
    return narrative

def write_summary(narrative):
    """Write the visual narrative summary."""
    with open("visual_summary.txt", "w") as f:
        f.write("VISUAL NARRATIVE SUMMARY\n")
        f.write("======================\n\n")
        
        for i, scene in enumerate(narrative, 1):
            start_time = scene["frames"][0]["timestamp"]
            end_time = scene["frames"][-1]["timestamp"]
            f.write(f"Scene {i}: [{start_time} - {end_time}]\n")
            f.write(f"Frames: {scene['start_frame']} - {scene['end_frame']}\n")
            f.write("Please analyze this scene's frames for context\n")
            f.write("-" * 50 + "\n\n")

def main():
    narrative = analyze_frames()
    write_summary(narrative)
    print("Visual summary created in visual_summary.txt")
    print(f"Total scenes: {len(narrative)}")
    print(f"Total frames: {sum(len(scene['frames']) for scene in narrative)}")

if __name__ == "__main__":
    main()