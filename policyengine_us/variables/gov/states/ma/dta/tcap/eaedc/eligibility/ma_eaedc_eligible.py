from policyengine_us.model_api import *


class ma_eaedc_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "Eligible for Massachusetts EAEDC"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MA

    def formula(spm_unit, period, parameters):
        assets_eligible = spm_unit("ma_eaedc_assets_eligible", period)
        financially_eligible = spm_unit(
            "ma_eaedc_financially_eligible", period
        )
        age_eligible = spm_unit("ma_eaedc_age_eligible", period)

        disabled_income_eligible = spm_unit(
            "ma_eaedc_disabled_income_eligible", period
        )

        return (
            assets_eligible
            & financially_eligible
            & age_eligible
            & disabled_income_eligible
        )