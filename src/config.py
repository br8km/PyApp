from pathlib import Path


class Config:
    """Config."""

    dir_app = Path(__file__).parent.parent

    dir_out = dir_app / "out"
    dir_cache = dir_out / "cache"
    dir_debug = dir_out / "debug"
    dir_log = dir_out / "log"
    dir_tmp = dir_out / "tmp"

    def __init__(self, private: bool = False) -> None:
        """Init."""
        self.private = private

    def dir_dat(self) -> Path:
        """Get dir_dat Path."""
        if self.private:
            return self.dir_app / "dat" / "private"
        return self.dir_app / "dat"

