import pandas as pd


def group_complaints(df: pd.DataFrame) -> pd.DataFrame:
    """
    Consolidate complaint_type + descriptor into broader categories.
    """
    mapping = {
        # Construction
        "Noise: Construction Before/After Hours (NM1)": "Construction Noise",
        "Noise: Construction Equipment (NC1)": "Construction Noise",
        "Noise: Jack Hammering (NC2)": "Construction Noise",
        "Noise: Construction Equipment - For Dep Internal Use Only (YNC1)": "Construction Noise",
        "Noise: Construction Before/After Hours - For Dep Internal Use Only (YNM1)": "Construction Noise",

        # Vehicle / Transportation
        "Noise: Boat(Engine,Music,Etc) (NR10)": "Vehicle Noise",
        "Noise: Boat(Engine": "Vehicle Noise",
        "Noise, Ice Cream Truck (NR4)": "Vehicle Noise",
        "Noise: Private Carting Noise (NQ1)": "Vehicle Noise",
        "Noise: Vehicle (NR2)": "Vehicle Noise",
        "Collection Truck Noise": "Vehicle Noise",
        "21 Collection Truck Noise": "Vehicle Noise",

        # Alarms & Equipment
        "Noise: Alarms (NR3)": "Alarms & Equipment",
        "Noise: air condition/ventilation equipment (NV1)": "Alarms & Equipment",
        "NOISE: AIR CONDITION/VENTILATION EQUIPMENT - FOR DEP INTERNAL USE ONLY (YNV1)": "Alarms & Equipment",
        "Noise: Air Condition/Ventilation Equip, Commercial (NJ2)": "Alarms & Equipment",
        "Noise: Air Condition/Ventilation Equip, Residential (NJ1)": "Alarms & Equipment",

        # Music / Party
        "Noise: Loud Music/Daytime (Mark Date And Time) (NN1)": "Music/Party Noise",
        "Noise: Loud Music/Nighttime(Mark Date And Time) (NP1)": "Music/Party Noise",
        "Noise: Loud Music/Nighttime(Mark Date And Time) - For Dep Internal Use Only (YNP1)": "Music/Party Noise",
        "Noise: Loud Music From Siebel System - For Dep Internal Use Only (NP21)": "Music/Party Noise",
        "People Created Noise": "Music/Party Noise",

        # Animals
        "Noise, Barking Dog (NR5)": "Animal Noise",
        "Noise, Other Animals (NR6)": "Animal Noise",

        # Other Noise / Rare
        "Noise:  lawn care equipment (NCL)": "Other Noise",
        "Noise: Manufacturing Noise (NK1)": "Other Noise",
        "Noise: Other Noise Sources (Use Comments) (NZZ)": "Other Noise",
        "Noise: Other Noise Sources (Use Comments) - For Dep Internal Use Only (YNZZ)": "Other Noise",
        "Plants- Noise Related Problems (PN1)": "Other Noise",

        # Non-noise categories
        "Manhole Cover Broken/Making Noise (SB)": "Sewer",
        "Manhole Cover Broken/Making Noise *For Dep Internal Use Only* (WF1)": "Sewer",
    }

    # Apply mapping
    df["noise_category"] = df["descriptor"].map(mapping)
    df["noise_category"] = df["noise_category"].fillna("Other Noise")

    df.drop(columns='complaint_type', inplace=True)

    return df

if __name__ == "__main__":
    df = pd.read_csv(".data/processed/noise_data_cleaned.csv")
    df = group_complaints(df)
    df.drop(columns='complaint_type', inplace=True)
    print(df["noise_category"].value_counts())
    df.to_csv(".data/processed/final_noise_data.csv", index=False)
    