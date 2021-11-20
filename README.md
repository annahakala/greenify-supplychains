# greenify-supplychains

Brief overview of how the data was extracted and calculated.

When We looked at the “spend data” file, we noticed that:
1.    There were very few unique categories in the CategoryL2 column
2.    Matching these categories with the categories in the emission tables provided would not be as simple as just matching words.

Therefore, we decided that it would not be time-effective to implement some natural language process to match these together. Instead, we decided to manually compile our own emission table based on the category names found in the CategoryL2 column.

This emission table consisted simply of three columns: category, UOM, and CO2keg equivalent. The UOM was based on in which form the spend data procurements were accounted for, as to make it possible to approximate the CO2 resulting form that transaction.

Then combining the “spend data” with its categories emission data and the matching quantity resulted in the transactions CO2kg value.
