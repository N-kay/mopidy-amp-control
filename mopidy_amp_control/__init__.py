import logging
import pathlib

import pkg_resources

from mopidy import config, ext

#__version__ = pkg_resources.get_distribution("Mopidy-Amp-Control").version
__version__ = '0.1'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = "Mopidy-Amp-Control"
    ext_name = "amp_control"
    #version = __version__
    version = 0.1

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["cmd_power"] = config.String()
        schema["cmd_unpower"] = config.String()
        schema["unpower_in_minutes"] = config.Integer()
        return schema

    def setup(self, registry):

        from .frontend import AmpControlFrontend
        registry.add('frontend', AmpControlFrontend)
