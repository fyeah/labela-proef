from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from decimal import Decimal as D

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)

class Base(object):
    def __json__(self, request):
        json_exclude = getattr(self, '__json_exclude__', set())
        res = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_') and key not in json_exclude:
                if isinstance(value, D):
                    # use float or str?
                    res[key] = float(value)
                else:
                    res[key] = value
        return res	

Base = declarative_base(metadata=metadata, cls=Base)
