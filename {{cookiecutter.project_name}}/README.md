# {{ cookiecutter.project_name | replace('-', ' ') | replace('_', ' ') }}

{{ cookiecutter.project_short_description }}

## Rendering an STL

Follow these steps to render an STL:

```shell
$ pip install poetry
$ poetry install
$ poetry run python -m {{ cookiecutter.__project_slug }}.{{ cookiecutter.__project_slug }}.py --stl
```

The rendered file will be saved to `renders/{{ cookiecutter.__project_slug }}.stl`.
