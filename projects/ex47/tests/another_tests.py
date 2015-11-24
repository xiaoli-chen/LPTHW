from nose.tools import *
from ex47.game import Room



def test_xiaoli():
    dorm=Room('IV','El Colegio Rd, #110')
    assert_equal(dorm.name, 'IV')
    assert_equal(dorm.paths,{})

def test_110():
    East_window=Room('Xiaoli','East')
    East_window.add_paths({'Window':2})
    assert_equal(East_window.go('Window'),2)
