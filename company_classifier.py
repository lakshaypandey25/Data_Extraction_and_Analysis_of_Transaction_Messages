from transformers import BertTokenizer, BertForSequenceClassification
import torch
from data_preparation import training_data, create_category_map 

company_classification_model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
company_classification_model.load_state_dict(torch.load("company_classification_model.pth", weights_only=True))
company_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

category_map = create_category_map(training_data)

def classify_company(company_name):
    company_tokens = company_tokenizer(company_name, return_tensors="pt")
    company_outputs = company_classification_model(**company_tokens)
    company_prediction = torch.argmax(company_outputs.logits, dim=1).item()
    return [category for category, index in category_map.items() if index == company_prediction][0]


if __name__ == "__main__":
    company_name = "SuperMarketXYZ"
    category = classify_company(company_name)
    print(f"Company Category: {category}")
