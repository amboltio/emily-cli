
import time
import torch


def train_step(model: torch.nn.Module,
               epoch: int,
               dataloader: torch.utils.data.dataloader,
               loss_fn: torch.nn,
               optimizer: torch.optim,
               scheduler: torch.optim.lr_scheduler
               ):

    train_loss = 0.
    train_acc = 0.
    start_time = time.time()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    print('Epoch {}:'.format(epoch + 1), flush=True)

    # Set the model's mode to training
    model.train()
    for idx, batch in enumerate(dataloader):

        if (idx + 1) % 100 == 0:
            print(f'Processing batch {idx + 1}/{len(dataloader)}')

        # Read data and corresponding labels for the current batch
        data = batch['data'].to(device)
        labels = batch['label'].to(device)

        # Forward the data into model to get predictions
        predictions = model(data)
        predicted_class = predictions.argmax(dim=1)

        # Calculate loss and perform back propagation + weight optimize
        loss_value = loss_fn(predicted_class, labels)
        loss_value.backward()
        optimizer.step()

        # Methods for calculating loss and accuracy
        train_acc += calculate_accuracy(predicted_class, labels)
        train_loss += loss_value.item()

        # Reset the gradients
        optimizer.zero_grad()

    total_loss = train_loss / len(dataloader)
    total_acc = train_acc / len(dataloader)
    scheduler.step()

    end_time = time.time()
    print(f"Epoch took {str(round(end_time - start_time, 2))}")

    return total_acc, total_loss


def validation_step(model: torch.nn.Module, dataloader: torch.utils.data.dataloader, loss_fn: torch.nn):

    print("Evaluating model on validation set...")
    val_loss = 0.
    val_acc = 0.

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Set the model's mode to evaluation (mean gradients will not be calculated which speeds up the process)
    model.eval()
    for idx, batch in enumerate(dataloader):

        # Read data and corresponding labels for the current batch
        data = batch['data'].to(device)
        labels = batch['label'].to(device)

        # Forward the data into the model
        predictions = model(data)
        predicted_class = predictions.argmax(dim=1)

        # Calculate loss
        loss_value = loss_fn(predicted_class, labels)

        # Methods for calculating loss and accuracy
        val_acc += calculate_accuracy(predicted_class, labels)
        val_loss += loss_value.item()

    total_loss = val_loss / len(dataloader)
    total_acc = val_acc / len(dataloader)

    return total_acc, total_loss


def calculate_accuracy(predictions, labels):
    return (predictions == labels.data).float().mean()

