"""
Utility routines: logging setup etc.
"""
import logging

def setup_logging(name="connecting-dots", level="INFO"):
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="[%(levelname)s %(name)s] %(message)s"
    )
