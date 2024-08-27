from policyengine_us.model_api import *


class az_hhs_tanf_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for the Arizona Cash Assistance"
    definition_period = MONTH
    reference = "https://des.az.gov/services/child-and-family/cash-assistance/cash-assistance-ca-income-eligibility-guidelines"
    defined_for = StateCode.AZ

    def formula(spm_unit, period, parameters):
        person = spm_unit.members
        monthly_fpg = spm_unit("spm_unit_fpg", period)
        monthly_countable_earned_income = spm_unit(
            "az_tanf_earned_income", period
        )
        payment_standard_threshold = spm_unit(
            "az_payment_standard_threshold", period
        )
        # Judge whether is a needy family (countable income is below 100% of Federal Poverty Guideline)
        fpg_rate = person("az_fpg_rate", period)
        fpg_eligibility = (
            monthly_countable_earned_income <= fpg_rate * monthly_fpg
        )
        # Judge whether the countable income exceed the Cash Assistance Payment Standard
        payment_standard_eligibility = (
            monthly_countable_earned_income <= payment_standard_threshold
        )
        # The family is eligible for cash assistance only when the two criteria are fitted at the same time
        return fpg_eligibility & payment_standard_eligibility