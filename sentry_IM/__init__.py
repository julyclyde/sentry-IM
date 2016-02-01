try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-IM').version
except Exception, e:
    VERSION = 'unknown'
