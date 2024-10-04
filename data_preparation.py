import pandas as pd
df = pd.read_csv("C:/Users/lakshay pandey/Desktop/Intel-Hackathon/companies_sorted.csv")
training_data = [{'company_name': row['name'], 'category': row['industry']} for index, row in df.iterrows()]

def create_category_map(training_data):
    unique_categories = set(item['category'] for item in training_data)
    return {category: index for index, category in enumerate(unique_categories)}