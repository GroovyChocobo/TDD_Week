import pytest
from health import *

def test_take_damage_reduces_health(player):
    result = take_damage(player,  30)
    assert result["health"] == 70

def test_heal_adds_health(player):
    result = health(player, 30)
    assert result["health"] == 100

def test_is_alive_true(player):
    result = take_damage(player, 100)
    assert result["health"] == False 
