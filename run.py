#!/usr/bin/env python3
"""
Employee Monitoring System - Main Entry Point
Run this file to start the application.
"""

import os
import sys
import logging
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('employee_monitoring.log')
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the Employee Monitoring System."""
    try:
        logger.info("Starting Employee Monitoring System...")
        
        # Set default environment variables if not set
        if not os.environ.get('CAMERA_SOURCES'):
            logger.info("No CAMERA_SOURCES set, will probe local cameras")
        
        if not os.environ.get('DETECT_CAPTURE_COOLDOWN'):
            os.environ['DETECT_CAPTURE_COOLDOWN'] = '60'  # 1 minute
            logger.info("Set default capture cooldown to 1 minute")
        
        # Import and run the Flask app
        from backend.app import app
        from config import HOST, PORT
        
        logger.info("Flask app initialized successfully")
        logger.info(f"Starting server on http://{HOST}:{PORT}")
        logger.info(f"Access the system at: http://{HOST}:{PORT}")
        logger.info("Admin login: admin / admin123")
        logger.info("Server login: Select 'Server' role (no credentials needed)")
        
        app.run(host=HOST, port=PORT, debug=False, threaded=True)
        
    except KeyboardInterrupt:
        logger.info("Shutting down Employee Monitoring System...")
    except Exception as e:
        logger.error(f"Failed to start Employee Monitoring System: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
