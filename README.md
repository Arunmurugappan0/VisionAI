# 📱 Employee Monitoring System

A real-time AI-powered employee monitoring system that detects mobile phone usage using YOLOv8 and provides live camera feeds with admin and server dashboards.

## ✨ Features

- **🔍 AI-Powered Detection**: Uses YOLOv8 to detect mobile phones in real-time
- **📹 Multi-Camera Support**: Supports USB cameras, RTSP streams, and HTTP video streams
- **👨‍💼 Role-Based Access**: Separate Admin and Server dashboards
- **📸 Automatic Capture**: Saves images when mobile phones are detected
- **⏱️ Smart Cooldown**: Configurable capture intervals to prevent spam
- **🎨 Modern UI**: Beautiful, responsive web interface
- **🔄 Auto-Reconnection**: Automatic camera reconnection on failures
- **📊 Real-time Monitoring**: Live camera feeds with detection overlays

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Activate virtual environment
F:\employee_monitoring\venv\Scripts\activate

# Install required packages
pip install -r backend/requirements.txt
```

### 2. Run the Application

```bash
# Simple start
python run.py

# Or run directly
python backend/app.py
```

### 3. Access the System

- **URL**: http://localhost:5000
- **Admin Login**: admin / admin123
- **Server Login**: Select "Server" role (no credentials needed)

## ⚙️ Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Camera Configuration
CAMERA_SOURCES="0:Entrance,1:Lobby,rtsp://user:pass@ip/stream:Warehouse"
DETECT_CAPTURE_COOLDOWN=300  # 5 minutes in seconds
MAX_CAMERAS=5

# YOLO Configuration
YOLO_WEIGHTS="path/to/yolov8n.pt"
YOLO_CONFIDENCE=0.25

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123

# Server Configuration
HOST=0.0.0.0
PORT=5000
DEBUG=False
```

### Camera Sources

The system supports multiple camera types:

#### USB Cameras
```bash
CAMERA_SOURCES="0:Front Desk,1:Reception"
```

#### RTSP Streams
```bash
CAMERA_SOURCES="rtsp://user:pass@192.168.1.100:554/stream:Office Camera"
```

#### HTTP Streams
```bash
CAMERA_SOURCES="http://192.168.1.101:8080/video:Mobile Camera"
```

#### Mixed Sources
```bash
CAMERA_SOURCES="0:USB Cam,rtsp://ip:554/stream:IP Cam,http://ip:8080/video:HTTP Cam"
```

## 📁 Project Structure

```
employee_monitoring/
├── backend/
│   ├── __init__.py
│   ├── app.py              # Flask application
│   ├── camera.py           # Camera management
│   ├── detector.py         # YOLO detection
│   ├── requirements.txt    # Python dependencies
│   └── yolov8n.pt         # YOLO model weights
├── frontend/
│   ├── templates/          # HTML templates
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── server_dashboard.html
│   └── static/
│       ├── css/
│       │   └── styles.css  # Modern UI styles
│       └── captures/       # Saved detection images
├── config.py              # Configuration settings
├── run.py                 # Main entry point
└── README.md             # This file
```

## 🎯 Usage

### Admin Dashboard
- **Live Feeds**: Real-time camera feeds with mobile detection overlays
- **Captured Images**: Gallery of saved mobile detection images
- **Manual Snapshots**: Capture images on demand
- **Detection Status**: Shows number of active detections

### Server Dashboard
- **Live Feeds**: Camera feeds without detection overlays
- **Manual Snapshots**: Capture images for reference
- **Camera Status**: Connection status indicators

### Mobile Detection
- **Automatic**: Saves images when mobile phones are detected
- **Cooldown**: Configurable interval between captures (default: 5 minutes)
- **Overlays**: Shows bounding boxes, confidence scores, and timestamps
- **Filtering**: Only captures "cell phone" class detections

## 🔧 Troubleshooting

### Camera Issues

**No cameras detected:**
```bash
# Check available cameras
python -c "import cv2; [print(f'Camera {i}: {cv2.VideoCapture(i).isOpened()}') for i in range(5)]"
```

**RTSP connection fails:**
- Verify network connectivity
- Check credentials and URL format
- Test with VLC or similar player

**USB camera not working:**
- Check device permissions
- Try different camera indices (0, 1, 2...)
- Verify camera is not used by other applications

### YOLO Issues

**Model not loading:**
```bash
# Download YOLO weights manually
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

**Detection not working:**
- Check if ultralytics is installed: `pip install ultralytics`
- Verify model file exists and is readable
- Check confidence threshold settings

### Performance Issues

**High CPU usage:**
- Reduce camera resolution
- Increase capture cooldown
- Use smaller YOLO model (yolov8n.pt)

**Memory issues:**
- Clear old captures regularly
- Reduce number of cameras
- Restart application periodically

## 📊 API Endpoints

### Camera Feeds
- `GET /admin_feed/<cam_id>` - Admin feed with detection
- `GET /server_feed/<cam_id>` - Server feed without detection

### API
- `POST /api/snapshot/<cam_id>` - Capture manual snapshot
- `GET /api/captures` - List captured images
- `GET /api/status` - System status

## 🔒 Security

- Change default admin credentials
- Use HTTPS in production
- Restrict network access
- Regular security updates

## 📝 Logs

Application logs are saved to `employee_monitoring.log` and include:
- Camera connection status
- Detection events
- Error messages
- System status

## 🤝 Support

For issues and questions:
1. Check the logs in `employee_monitoring.log`
2. Verify camera connections
3. Test YOLO model loading
4. Check environment variables

## 📄 License

This project is for educational and monitoring purposes. Ensure compliance with local privacy laws and regulations.

