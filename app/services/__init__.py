"""
Services module for LocalFeed.
Contains business logic for path handling, caching, and optimizations.
"""

from app.services.path_utils import (
    expand_path,
    normalize_path,
    is_path_allowed,
    validate_and_normalize_path,
    format_image_url,
    extract_path_from_url,
)
from app.services.image_cache import (
    get_all_images,
    get_folder_mtime,
    invalidate_cache,
    get_images_by_folder,
    get_leaf_folders,
)
from app.services.optimizations import (
    ensure_thumbnail_dir,
    get_thumbnail_path,
    create_thumbnail,
    create_video_poster,
    get_cache_key,
)
from app.services.data import (
    load_config,
    save_config,
    get_optimization_settings,
    save_optimization_settings,
    load_favorites,
    save_favorites,
    cleanup_favorites,
    load_trash,
    save_trash,
    cleanup_trash,
)

__all__ = [
    # Path utilities
    'expand_path',
    'normalize_path',
    'is_path_allowed',
    'validate_and_normalize_path',
    'format_image_url',
    'extract_path_from_url',
    # Image cache
    'get_all_images',
    'get_folder_mtime',
    'invalidate_cache',
    'get_images_by_folder',
    'get_leaf_folders',
    # Optimizations
    'ensure_thumbnail_dir',
    'get_thumbnail_path',
    'create_thumbnail',
    'create_video_poster',
    'get_cache_key',
    # Data management
    'load_config',
    'save_config',
    'get_optimization_settings',
    'save_optimization_settings',
    'load_favorites',
    'save_favorites',
    'cleanup_favorites',
    'load_trash',
    'save_trash',
    'cleanup_trash',
]
