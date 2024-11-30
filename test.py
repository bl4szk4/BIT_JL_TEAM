# import pandas as pd
#
#
# column_mapping = {
#     "Physical Activity Level": "physical_activity_level",
#     "Creativity Level": "creativity_level",
#     "Complexity Level": "complexity_level",
#     "Entry/Start Level": "entry_start_level",
#     "Age Range": "age_range",
#     "Time Commitment": "time_commitment",
#     "Number of People": "number_of_people",
#     "Remote_On_Site": "remote_on_site",
#     "Competitiveness": "competitiveness",
#     "Budget": "budget",
#     "Seasonality": "seasonality",
#     "Risk of Injury": "risk_of_injury",
#     "Acceptable Disability Level": "acceptable_disability_level",
#     "Popularity (Community)": "popularity",
#     "Phobias": "phobias",
#     "Relaxation Level": "relaxation_level",
#     "Stress Level": "stress_level",
#     "Skill Development": "skill_development",
#     "Regularity": "regularity",
#     "Flexibility": "flexibility",
#     "Earning Potential": "earning_potential",
#     "Emotional Engagement": "emotional_engagement",
#     "Mental Health Impact": "mental_health_impact",
# }
#
#
# df = pd.read_csv("output.csv", sep=",")
#
# df.rename(columns=column_mapping, inplace=True)
#
# # Zapisz zaktualizowany plik CSV
# df.to_csv("output2.csv", index=False)
#
# #
# # print(df.columns)
# #
# # mapping = {
# #     'low': 0,
# #     'semi-low': 1,
# #     'medium': 2,
# #     'medium-hard': 3,
# #     'high': 4,
# #     'very-high': 4,
# #     'very-hard': 4,
# #     'on-site': 0,
# #     'remote': 4
# # }
# #
# # df_copy = df.drop(columns=['Hobby'])
# # print(df_copy.columns)
# #
# # df_copy = df_copy.replace(mapping)
# #
# # df_copy['Hobby'] = df['Hobby']
# #
# # df_copy.to_csv('output.csv', index=False)


import csv
from bit_app.apps.hobby.models.hobby import Hobby

csv_file_path = 'output2.csv'

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            hobby = Hobby(
                name=row.get('name'),
                physical_activity_level=int(row.get('physical_activity_level', 0)),
                creativity_level=int(row.get('creativity_level', 0)),
                complexity_level=int(row.get('complexity_level', 0)),
                entry_start_level=int(row.get('entry_start_level', 0)),
                age_range=int(row.get('age_range', 0)),
                time_commitment=int(row.get('time_commitment', 0)),
                number_of_people=int(row.get('number_of_people', 0)),
                remote_on_site=int(row.get('remote_on_site', 0)),
                competitiveness=int(row.get('competitiveness', 0)),
                budget=int(row.get('budget', 0)),
                seasonality=int(row.get('seasonality', 0)),
                risk_of_injury=int(row.get('risk_of_injury', 0)),
                acceptable_disability_level=int(row.get('acceptable_disability_level', 0)),
                popularity=int(row.get('popularity', 0)),
                phobias=int(row.get('phobias', 0)),
                relaxation_level=int(row.get('relaxation_level', 0)),
                stress_level=int(row.get('stress_level', 0)),
                skill_development=int(row.get('skill_development', 0)),
                regularity=int(row.get('regularity', 0)),
                flexibility=int(row.get('flexibility', 0)),
                earning_potential=int(row.get('earning_potential', 0)),
                emotional_engagement=int(row.get('emotional_engagement', 0)),
                mental_health_impact=int(row.get('mental_health_impact', 0)),
                is_for_disability_person=bool(int(row.get('acceptable_disability_level', 0)) > 0),
                summary=""
            )
            hobby.save()
            print(f"Added Hobby: {hobby.name}")
        except Exception as e:
            print(f"Error adding Hobby: {row.get('name')}, {e}")