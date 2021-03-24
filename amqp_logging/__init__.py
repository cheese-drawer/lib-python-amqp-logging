"""Library for publishing LogRecords via AMQP.

Wraps python's built-in `logging` library in async/await syntax & publishes a
copy of every log over AMQP on a direct exchange with routing based on log
level. API is a near match to a subset of the `logging` API, using familiar
setup methods like `getLogger` & `basicConfig` in addition to the log methods
of `debug`, `info`, `warn`, & `error`.
"""
