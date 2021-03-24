"""Testing Logger."""

import asyncio
import unittest
from unittest import TestCase

from test.unit.helpers.asynchronous import async_test
from test.unit.helpers.output import captured_output

from amqp_logging.logger import Logger


class TestInit(TestCase):
    """Testing Logger initialization."""

    def test_has_name_and_root_route(self) -> None:
        """A Logger has props name and root route, give as strings on init."""
        logger = Logger('name', 'root')

        with self.subTest():
            self.assertEqual(logger.name, 'name')
        with self.subTest():
            self.assertEqual(logger.root_route, 'root')


class TestDebug(TestCase):
    """Testing Logger.debug."""

    logger: Logger
    stdout: str
    stderr: str

    @classmethod
    def setUpClass(cls) -> None:
        async def debug() -> None:
            await cls.logger.debug('A message')

        cls.logger = Logger('A Name', 'logging')

        with captured_output() as captured:
            asyncio.run(debug())

        stdout, stderr = captured
        cls.stdout = stdout.getvalue()
        cls.stderr = stderr.getvalue()

    def test_it_prints_msg_to_stdout(self) -> None:
        """Calling debug prints the given message to stdout."""
        self.assertIn('A message', self.stdout)

    def test_it_prints_nothing_to_stderr(self) -> None:
        """Calling debug prints nothing to stderr."""
        self.assertNotIn('A message', self.stderr)

    def test_it_publishes_message_to_root_debug(self) -> None:
        """Calling debug publishes message via AMQP to `{root_route}.debug`."""


if __name__ == '__main__':
    unittest.main()
