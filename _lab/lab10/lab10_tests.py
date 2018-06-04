import pytest

#############

from lab10 import spacedString

def test_spacedString_1():
    assert spacedString("UCSB",1)=="U C S B"

def test_spacedString_2():
    assert spacedString("Cal Poly",2)=="C  a  l     P  o  l  y"

def test_spacedString_3():
    assert spacedString("UCSD",0)=="UCSD"

def test_spacedString_4():
   with pytest.raises(ValueError):
      result = spacedString("UCSD",-1)

def test_spacedString_5():
   with pytest.raises(ValueError):
      result = spacedString(["not a string"],0)

def test_spacedString_5():
   with pytest.raises(ValueError):
      result = spacedString("A String","Not an int")
      
##########################



