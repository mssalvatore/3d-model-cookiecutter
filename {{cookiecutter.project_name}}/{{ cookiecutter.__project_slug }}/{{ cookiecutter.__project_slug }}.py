import argparse
from pathlib import Path

from build123d import *  # noqa: F403
from ocp_vscode import (  # noqa: F401
    get_defaults,
    reset_show,
    set_defaults,
    set_port,
    show,
    show_all,
    show_object,
)

set_port(3939)


def export_model_to_stl(model: Part):
    src_file_path = Path(__file__)
    renders_dir = src_file_path.parent.parent / "renders"

    if not renders_dir.exists():
        renders_dir.mkdir()
    elif not renders_dir.is_dir():
        raise RuntimeError(f"{renders_dir} is not a directory.")

    stl_file_name = src_file_path.stem + ".stl"

    export_stl(model, renders_dir / stl_file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_short_description }}"
    )
    parser.add_argument("--stl", action="store_true", help="Export STL")
    args = parser.parse_args()

    ...

    if args.stl:
        export_model_to_stl(Part() + model)
    else:
        show_all()
