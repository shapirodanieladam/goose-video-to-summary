sources = [
    "https://github.com/cashapp/hermit-packages.git",
    "https://github.com/cashapp/hermit-build.git",
]

python "3.11" {
    env = {
        PATH = "${HERMIT_ENV}/bin:${PATH}"
        PYTHONPATH = "${HERMIT_ENV}/lib/python3.11/site-packages"
    }
}

env {
    PYTHONPATH = "${HERMIT_ENV}/lib/python3.11/site-packages"
}