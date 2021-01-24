__version__ = '0.1.0'

try:
    import runner
except ModuleNotFoundError:
    from name_that_hash import runner

runner.main()