from transformers import AdamW, get_scheduler, BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
import torch
from data_preparation import training_data, create_category_map

company_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
company_classification_model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

category_map = create_category_map(training_data)

class CompanyDataset(Dataset):
    def __init__(self, data, tokenizer, category_map):
        self.data = data
        self.tokenizer = tokenizer
        self.category_map = category_map

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        company_name = self.data[idx]["company_name"]
        label = self.data[idx]["category"]
        inputs = self.tokenizer(company_name, return_tensors="pt", padding=True, truncation=True)
        inputs["labels"] = torch.tensor(self.category_map[label], dtype=torch.long)
        return inputs

dataset = CompanyDataset(training_data, company_tokenizer, category_map)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)

optimizer = AdamW(company_classification_model.parameters(), lr=5e-5)
num_epochs = 3
num_training_steps = num_epochs * len(dataloader)
lr_scheduler = get_scheduler("linear", optimizer=optimizer, num_warmup_steps=0, num_training_steps=num_training_steps)

company_classification_model.train()

for epoch in range(num_epochs):
    for batch in dataloader:
        outputs = company_classification_model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()

torch.save(company_classification_model.state_dict(), "company_classification_model.pth")
