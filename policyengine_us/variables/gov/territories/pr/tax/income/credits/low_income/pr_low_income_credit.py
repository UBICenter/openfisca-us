from policyengine_us.model_api import *


class pr_low_income_credit(Variable):
    value_type: float
    entity: TaxUnit
    label: "Puerto Rico low income credit"
    unit: USD 
    definition_period: YEAR
    reference: "https://casetext.com/statute/laws-of-puerto-rico/title-thirteen-taxation-and-finance/subtitle-17-internal-revenue-code-of-2011/part-ii-income-taxes/chapter-1007-credits-against-tax/subchapter-b-refundable-credits/30212-credit-for-low-income-individuals-older-than-sixty-five-65-years-of-age"

    