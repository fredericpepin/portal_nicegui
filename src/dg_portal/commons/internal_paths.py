from pathlib import Path

__all__ = [
    'resolve_asset', 
    'resolve_module_asset', 
    'images', 
    'css', 
    'icons', 
    'js', 
    'fonts',
    'PROJECT_ROOT',
    'SRC_DIR',
    'PKG_DIR',
    'STATIC_DIR',
    'IMAGES_DIR',
    'CSS_DIR',
    'ICONS_DIR',
    'JS_DIR',
    'FONTS_DIR',
    'COMMONS_DIR',
    'MODULES_DIR'
    ]



# Define base paths
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
SRC_DIR = PROJECT_ROOT / "src"
PKG_DIR = SRC_DIR / "dg_portal"
STATIC_DIR = PROJECT_ROOT / "static"
IMAGES_DIR = STATIC_DIR / "images"
CSS_DIR = STATIC_DIR / "css"
ICONS_DIR = STATIC_DIR / "icons"
JS_DIR = STATIC_DIR / "js"
FONTS_DIR = STATIC_DIR / "fonts"

# Module-specific paths
COMMONS_DIR = SRC_DIR / "dg_portal" / "commons"
MODULES_DIR = SRC_DIR / "dg_portal" / "modules"

# --- Asset resolvers ---
def resolve_asset(asset_path: str) -> str:
    """Resolve an asset path relative to the static directory."""
    return str(STATIC_DIR / asset_path)

def resolve_module_asset(module_name: str, asset_path: str) -> str:
    """Resolve an asset path relative to a specific module."""
    return str(MODULES_DIR / module_name / "assets" / asset_path)

# --- Friendly aliases for common dirs ---
def images(filename: str) -> Path:
    """Resolve a path inside /static/images."""
    return IMAGES_DIR / filename

def css(filename: str) -> Path:
    return Path(CSS_DIR / filename)

def icons(filename: str) -> Path:
    return ICONS_DIR / filename

def js(filename: str) -> Path:
    return JS_DIR / filename

def fonts(filename: str) -> Path:
    return FONTS_DIR / filename

