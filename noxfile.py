import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["lint", "mypy", "test_admin"]


def run_external(session, *args):
    # used to suppress warning of type
    # "Warning: <package> is not installed into the virtualenv, it is located at [..]"
    session.run(*args, external=True)


@nox.session
def lint(session) -> None:
    """Run lint checks."""
    run_external(session, "black", "project")
    run_external(session, "ruff", "check", "project", "--fix")
    run_external(session, "autoflake", "project", "--check")
    run_external(session, "isort", "project")


@nox.session
def mypy(session) -> None:
    """Run Mypy."""
    run_external(session, "mypy", "project")


@nox.session
def test_admin(session) -> None:
    """Run coverage sequence."""
    session.cd("project")
    omit_glob = "manage.py,*/migrations/*,backend/*"
    run_external(
        session,
        "coverage",
        "run",
        f"--omit={omit_glob}",
        "--branch",
        "manage.py",
        "test",
        "--noinput",
    )
    run_external(session, "coverage", "report", f"--omit={omit_glob}", "-m")
