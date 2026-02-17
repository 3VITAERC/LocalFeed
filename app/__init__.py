"""
LocalFeed - Flask Application Factory.
"""

import os
import json
from flask import Flask
from flask_compress import Compress


def _ensure_config_files_exist():
    """Create default config files if they don't exist.
    
    This allows users to skip the manual setup step of copying example files.
    Files are created with sensible defaults on first launch.
    """
    from app.config import CONFIG_FILE, FAVORITES_FILE, TRASH_FILE, DEFAULT_OPTIMIZATIONS
    
    defaults = {
        CONFIG_FILE: {
            'folders': [],
            'shuffle': False,
            'optimizations': DEFAULT_OPTIMIZATIONS
        },
        FAVORITES_FILE: {'favorites': []},
        TRASH_FILE: {'trash': []}
    }
    
    for filepath, default_content in defaults.items():
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump(default_content, f, indent=2)


def create_app(config=None):
    """Create and configure the Flask application.
    
    Args:
        config: Optional configuration dictionary
        
    Returns:
        Configured Flask application instance
    """
    # Auto-create config files if they don't exist
    _ensure_config_files_exist()
    
    # Get the project root directory (where server.py is located)
    # __file__ is app/__init__.py, so parent is project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_folder = os.path.join(project_root, 'static')
    
    app = Flask(__name__, 
                static_folder=static_folder,
                static_url_path='/static')
    
    # Load configuration
    if config:
        app.config.update(config)
    
    # Enable Gzip compression for API responses
    # Compresses JSON responses > 500 bytes, achieving 70-80% size reduction
    app.config['COMPRESS_MIN_SIZE'] = 500  # Only compress responses > 500 bytes
    app.config['COMPRESS_LEVEL'] = 6       # Balance between speed and compression
    Compress(app)
    
    # Register blueprints
    from app.routes.images import images_bp
    from app.routes.folders import folders_bp
    from app.routes.favorites import favorites_bp
    from app.routes.trash import trash_bp
    from app.routes.cache import cache_bp
    from app.routes.pages import pages_bp
    
    app.register_blueprint(images_bp)
    app.register_blueprint(folders_bp)
    app.register_blueprint(favorites_bp)
    app.register_blueprint(trash_bp)
    app.register_blueprint(cache_bp)
    app.register_blueprint(pages_bp)
    
    return app
