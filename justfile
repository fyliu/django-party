alias t := test
alias c := check
alias rf := run-frontend
alias rb := run-backend

#default: check test
default:
  just --list

# test the backend
[positional-arguments]
test:
  python -m pytest $@

# lint
check:
  pre-commit


run-frontend:
  npm run tailwind:dev

run-backend:
  python manage.py runserver

pwd:
  echo {{invocation_directory()}}
  echo {{justfile_directory()}}
  echo {{source_directory()}}
