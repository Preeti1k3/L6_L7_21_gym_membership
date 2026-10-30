
import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# ---------------- MEMBERSHIP COST: BRANCH TESTS ----------------

def test_valid_plan():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_invalid_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_age_below_14():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_minimum_valid_age():
    assert membership_cost("monthly", 14, False, False) == 1500


def test_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_below_senior_age_student():
    assert membership_cost("monthly", 59, True, False) == 1350


def test_below_senior_age_non_student():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_senior_student_gets_senior_discount():
    # Senior discount takes precedence over student discount.
    assert membership_cost("monthly", 60, True, False) == 1125


def test_trainer_for_monthly_plan():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_trainer_for_yearly_plan():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_trainer_for_quarterly_plan():
    assert membership_cost("quarterly", 30, False, True) == 6000


def test_student_with_trainer():
    assert membership_cost("monthly", 20, True, True) == 3350


# ---------------- GYM ENTRY: BRANCH TESTS ----------------

def test_inactive_membership():
    assert can_enter(10, False, False, "M") is False


def test_active_membership():
    assert can_enter(10, True, False, "M") is True


def test_before_opening():
    assert can_enter(4, True, False, "M") is False


def test_opening_time_boundary():
    assert can_enter(5, True, False, "M") is True


def test_closing_time_boundary():
    assert can_enter(22, True, False, "M") is True


def test_after_closing():
    assert can_enter(23, True, False, "M") is False


def test_women_only_slot_female():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male():
    assert can_enter(10, True, True, "M") is False


def test_regular_slot_male():
    assert can_enter(10, True, False, "M") is True


# ---------------- BMI: BRANCH TESTS ----------------

def test_invalid_zero_height():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(60, 0)


def test_invalid_negative_height():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(60, -1)


def test_underweight():
    assert bmi_category(18, 1) == "underweight"


def test_normal_at_lower_boundary():
    assert bmi_category(18.5, 1) == "normal"


def test_normal_weight():
    assert bmi_category(22, 1) == "normal"


def test_overweight_at_lower_boundary():
    assert bmi_category(25, 1) == "overweight"


def test_overweight():
    assert bmi_category(27, 1) == "overweight"


def test_obese_at_lower_boundary():
    assert bmi_category(30, 1) == "obese"


def test_obese():
    assert bmi_category(35, 1) == "obese"
