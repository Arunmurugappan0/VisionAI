"""
Configuration settings for Employee Monitoring System
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"
CAPTURES_DIR = FRONTEND_DIR / "static" / "captures"

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'employee_monitoring_secret_key_2024')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Camera configuration
CAMERA_SOURCES = os.environ.get('CAMERA_SOURCES', '')
DETECT_CAPTURE_COOLDOWN = int(os.environ.get('DETECT_CAPTURE_COOLDOWN', '60'))  # 1 minute
MAX_CAMERAS = int(os.environ.get('MAX_CAMERAS', '5'))
AUTO_REFRESH_INTERVAL = int(os.environ.get('AUTO_REFRESH_INTERVAL', '15'))  # Auto refresh every 15 seconds
STREAM_FPS = int(os.environ.get('STREAM_FPS', '24'))  # Target FPS for streaming
STREAM_JPEG_QUALITY = int(os.environ.get('STREAM_JPEG_QUALITY', '80'))  # Default JPEG quality
FAST_STREAM_JPEG_QUALITY = int(os.environ.get('FAST_STREAM_JPEG_QUALITY', '45'))  # JPEG quality for fast mode
FAST_MODE = os.environ.get('FAST_MODE', 'false').lower() in ('1', 'true', 'yes')
STREAM_WIDTH = int(os.environ.get('STREAM_WIDTH', '640'))
STREAM_HEIGHT = int(os.environ.get('STREAM_HEIGHT', '480'))
FAST_STREAM_WIDTH = int(os.environ.get('FAST_STREAM_WIDTH', '320'))
# 0 height means auto-calculate to preserve aspect ratio
FAST_STREAM_HEIGHT = int(os.environ.get('FAST_STREAM_HEIGHT', '0'))
FAST_DETECTION_STRIDE = int(os.environ.get('FAST_DETECTION_STRIDE', '2'))  # run detection every N frames in fast mode
FAST_MAX_GRABS = int(os.environ.get('FAST_MAX_GRABS', '2'))  # drop up to N buffered frames per loop in fast mode

# YOLO configuration
# Prefer newer weights if provided via env, else fallback to common local filenames
_default_weights = None
for candidate in [
    BACKEND_DIR / "yolov11n.pt",
    BACKEND_DIR / "yolov12n.pt",
    BACKEND_DIR / "yolov8n.pt",
]:
    if candidate.exists():
        _default_weights = str(candidate)
        break
YOLO_WEIGHTS = os.environ.get('YOLO_WEIGHTS', _default_weights or str(BACKEND_DIR / "yolov8n.pt"))
YOLO_CONFIDENCE = float(os.environ.get('YOLO_CONFIDENCE', '0.55'))

# Admin credentials
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

# Server configuration
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '5000'))
PUBLIC_BASE_URL = os.environ.get('PUBLIC_BASE_URL', '')  # e.g., https://your-domain.com/

# Detection classes to monitor
DETECTION_CLASSES = ['cell phone', 'mobile phone', 'cellphone', 'phone']

# Ensure captures directory exists
CAPTURES_DIR.mkdir(parents=True, exist_ok=True)
