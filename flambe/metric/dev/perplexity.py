import torch

from flambe.metric import Metric


class Perplexity(Metric):

    def __init__(self):
        """Initalizes the Metric."""
        self.entropy = torch.nn.CrossEntropyLoss()

    def compute(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Compute the preplexity given the input and target.

        Parameters
        ----------
        pred: torch.Tensor
            input logits of shape (B x N)
        target: torch.LontTensor
            target tensor of shape (B x N)

        Returns
        -------
        torch.float
            Output perplexity

        """
        entropy = self.entropy(pred, target).mean()
        return torch.exp(entropy)
