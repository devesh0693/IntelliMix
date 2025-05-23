# IntelliMix

![IntelliMix Logo](frontend/src/assets//logo.png)

## AI-Powered Audio Transformation Suite

IntelliMix is a powerful web application that transforms your creative vision into reality using AI-powered audio tools. It streamlines complex audio editing tasks, allowing you to focus on creativity rather than technical work.

## Features

### 🎵 AI Music Studio
Create unique transformations of songs using advanced AI. Perfect for remixes, covers, and creative experiments.
- Generate AI-powered music mashups and transformations
- Customize with detailed prompts
- Download high-quality audio files

### 🎧 Audio Mixer
Extract and edit specific portions from audio tracks. Supports batch processing for efficient workflows.
- Trim and extract snippets from YouTube videos
- Process multiple audio files simultaneously
- Precise timestamp control

### 📱 Media Downloader
Download high-quality audio and video content. Optimized for the best possible quality.
- Download videos from various platforms
- Choose quality options
- Fast and reliable processing

## Technology Stack

### Frontend
- React with TypeScript
- Three.js for 3D elements and animations
- React Router for navigation
- GSAP for smooth animations
- Tailwind CSS for styling

### Backend
- Python Flask server
- Google Gemini AI integration
- YouTube API integration
- Audio processing libraries

## Getting Started

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)
- pip

### Installation

#### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt