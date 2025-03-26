alias t := test
alias c := check
alias e := export-requirements
alias rf := run-frontend
alias rb := run-backend

# global
alias ga := git-add
alias l := lazygit

#default: check test
default:
  just --list

# test the backend
[positional-arguments]
test:
  python -m pytest $@

# lint
[positional-arguments]
check:
  pre-commit $@


run-frontend:
  npm run tailwind:dev

[positional-arguments]
run-backend:
  python manage.py runserver $@

export-requirements:
  uv pip compile -o requirements.txt pyproject.toml


## global commands ##

# stage all changes
git-add:
  git add -A

lazygit:
  lazygit

pwd:
  echo {{invocation_directory()}}
  echo {{justfile_directory()}}
  echo {{source_directory()}}
