from policyengine_us.model_api import *


class nc_tanf_income_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "North Carolina TANF income eligible"
    definition_period = YEAR
    defined_for = StateCode.NC

    def formula(spm_unit, period, parameters):
        monthly_allowed_difference = parameters(
            period
        ).gov.states.nc.ncdhhs.tanf.need_standard.monthly_allowed_difference
        income = add(
            spm_unit,
            period,
            [
                "nc_tanf_countable_earned_income",
                "nc_tanf_countable_gross_unearned_income",
            ],
        )
        need_standard = spm_unit("nc_tanf_need_standard", period)
        household_size = spm_unit("spm_unit_size", period)
        reduced_need_standard = max_(need_standard - income, 0)
        need_standard_fraction = reduced_need_standard / household_size
        difference_threshold = monthly_allowed_difference * MONTHS_IN_YEAR

        return need_standard_fraction >= difference_threshold