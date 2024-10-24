import sys
import importlib.util


def test_tensorflow_text_install():
    # installed_packages_list = [i.key for i in list(pkg_resources.working_set)]
    # tf_text_installed = "tensorflow-text" in installed_packages_list
    tf_text_installed = importlib.util.find_spec("tensorflow-text") != None

    if sys.platform == "win32":
        assert not tf_text_installed
    else:
        assert tf_text_installed
