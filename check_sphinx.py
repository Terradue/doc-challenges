import py
import subprocess

def test_linkcheck(tmpdir):
    doctrees = tmpdir.join("_build/doctrees")
    htmldir = tmpdir.join("_build/html")
    subprocess.check_call(["sphinx-1.0-build", "-W", "-blinkcheck", "-d",
        str(doctrees), "source", str(htmldir)])


def test_build_docs(tmpdir):
    doctrees = tmpdir.join("_build/doctrees")
    htmldir = tmpdir.join("_build/html")
    subprocess.check_call([ "sphinx-1.0-build", "-n", "-W", "-bhtml", "-d",
        str(doctrees), "source", str(htmldir)])
