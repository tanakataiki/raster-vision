from tempfile import TemporaryDirectory

import click

import rastervision as rv
from rastervision.plugin import PluginRegistry
from rastervision.utils.files import load_json_config
from rastervision.protos.command_pb2 import CommandConfig as CommandConfigMsg


class CommandRunner:
    @staticmethod
    def run(command_config_uri):
        with TemporaryDirectory as tmp_dir:
            msg = load_json_config(command_config_uri, CommandConfigMsg())
            PluginRegistry.get_instance().add_plugins(msg.plugins)
            command_config = rv.CommandConfig.from_proto(msg)
            command = command_config.create_command(tmp_dir)
            command.run(tmp_dir)
