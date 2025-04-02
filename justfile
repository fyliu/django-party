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

run-e2e:
  npx cypress run

## global commands ##

# stage all changes
git-add:
  git add -A

lazygit:
  lazygit

docker-build:
  docker build . -t party_organizer

docker-run:
  docker run -p 8000:8000 --name party_app -e PORT=8000 -d --rm party_organizer

docker-stop:
  docker stop party_app

dc-up:
  docker-compose up -d

dc-down:
  docker-compose down

pwd:
  echo {{invocation_directory()}}
  echo {{justfile_directory()}}
  echo {{source_directory()}}
