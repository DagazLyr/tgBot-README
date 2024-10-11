from .Models import *
from DB.MySql import AstroDatabase

ChakraProfile.set_name('chakra_profile_tbl')

AstroDatabase.create_tables([
    ChakraProfile
])