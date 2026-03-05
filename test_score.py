import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points_basic(game):
    result = add_points(game, 10)
    assert result["score"] == 10

def test_add_points_uses_multiplier(game):
    game["multiplier"] = 3
    result = add_points(game, 5)
    assert result["score"] == 15

def test_add_points_inactive_game(game):
    game["active"] = False
    result = add_points(game, 10)
    assert result["score"] == 0

def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)

def test_add_points_rejects_zero(game):
    with pytest.raises(ValueError):
        add_points(game, 0)

def test_add_points_rejects_non_integer(game):
    with pytest.raises(ValueError):
        add_points(game, 2.5)

def test_apply_multiplier_basic(game):
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 3

def test_apply_multiplier_inactive_game(game):
    game["active"] = False
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 1

def test_apply_multiplier_rejects_below_one(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)

def test_reset_score_active_game(game):
    game["score"] = 100
    game["multiplier"] = 5
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1
    assert result["active"] == True

def test_reset_score_inactive_game(game):
    game["active"] = False
    game["score"] = 50
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1

def test_is_high_score_true(game):
    game["score"] = 100
    assert is_high_score(game, 50) == True

def test_is_high_score_false(game):
    game["score"] = 50
    assert is_high_score(game, 100) == False

def test_is_high_score_equal_returns_false(game):
    game["score"] = 100
    assert is_high_score(game, 100) == False

def test_is_high_score_rejects_negative_threshold(game):
    with pytest.raises(ValueError):
        is_high_score(game, -1)