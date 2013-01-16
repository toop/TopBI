"""
"""


class Factory(object):

    def __init__(self, context, session_name='ro'):
        self.context = context
        self.session = sessions[session_name]()
        self.repository = RepositoryFactory(self.session)

    def __enter__(self):
        self.session.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.__exit__(exc_value, exc_value, traceback)


class RepositoryFactory(object):

    def __init__(self, session):
        self.session = session


# region: configuration details

from config import mode

if mode == 'mock':
    from wheezy.core.db import NullSession
    sessions = {'ro': NullSession, 'rw': NullSession}
else:
    raise NotImplementedError(mode)
del mode

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: