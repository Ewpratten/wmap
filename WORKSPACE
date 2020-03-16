load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    sha256 = "506dfbfd74ade486ac077113f48d16835fdf6e343e1d4741552b450cfc2efb53",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.1/bazel_federation-0.0.1.tar.gz",
)

http_archive(
    name = "rules_python",
    sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz",
)

load("@bazel_federation//:repositories.bzl", "rules_python")

rules_python()

load("@bazel_federation//setup:rules_python.bzl", "rules_python_setup")

rules_python_setup(use_pip = True)

# Workspace deps
load("@rules_python//python:pip.bzl", "pip_import")

pip_import(
    name = "webservice",
    requirements = "//webservice:requirements.txt",
)