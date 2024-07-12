import random
from django.contrib.auth.models import User
from .models import Subscriber, Transaction

# Function to generate random transactions
def generate_random_transactions(subscriber):
    transaction_choices = ['E_Parking', 'E_Insurance', 'Book_mechanic', 'Chauffeur_4hire']
    for _ in range(3):  # Generate three transactions for each subscriber
        transaction = Transaction.objects.create(
            sub=subscriber.sub,
            Transaction_type=random.choice(transaction_choices),
            provider_id=str(random.randint(1000, 9999)),  # Replace with your logic
            amount=random.randint(10, 100),  # Replace with your logic
            transaction_status=random.choice([True, False]),
        )

# Function to create subscribers and associated transactions
def create_subscribers_with_transactions():
    for _ in range(3):  # Create three subscribers
        user = User.objects.create(username=f'user{_}', password='nindenkawe')  # Replace with your logic
        subscriber = Subscriber.objects.create(sub=user, phone_number='umurerwa@1')  # Replace with your logic
        generate_random_transactions(subscriber)

create_subscribers_with_transactions()

""" 
import torch
import torch.nn as nn
import random
from django.contrib.auth.models import User
from yourapp.models import Subscriber, Transaction

# Define a simple PyTorch model for data generation
class DataGenerator(nn.Module):
    def __init__(self, input_size, output_size):
        super(DataGenerator, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# Function to generate random transactions using PyTorch
def generate_random_transactions_with_pytorch(subscriber, model):
    transaction_choices = ['E_Parking', 'E_Insurance', 'Book_mechanic', 'Chauffeur_4hire']
    for _ in range(3):  # Generate three transactions for each subscriber
        input_data = torch.randn(1, model.input_size)  # Replace with your input size
        output_data = model(input_data)
        transaction = Transaction.objects.create(
            sub=subscriber.sub,
            Transaction_type=random.choice(transaction_choices),
            provider_id=str(int(output_data.item())),  # Replace with your logic
            amount=int(output_data.item() * 10),  # Replace with your logic
            transaction_status=random.choice([True, False]),
        )

# Function to create subscribers and associated transactions with PyTorch data generation
def create_subscribers_with_transactions_and_pytorch():
    model = DataGenerator(input_size=5, output_size=1)  # Replace with your input and output sizes
    for _ in range(3):  # Create three subscribers
        user = User.objects.create(username=f'user{_}', password='password123')  # Replace with your logic
        subscriber = Subscriber.objects.create(sub=user, phone_number='1234567890')  # Replace with your logic
        generate_random_transactions_with_pytorch(subscriber, model)

create_subscribers_with_transactions_and_pytorch() """
