class UpdatingMean():
    """
        A class that updates mean value for loss aggregation

        Attributes
        ----------
        sum: int
            partial sum of all loss values

        n: int
            number of elements summed

        Methods
        -------
        mean()
            Return the mean of the values

        add(loss)
            Add new loss value to the actual sum of all the elements and increment counter n
        """
    def __init__(self):
        self.sum = 0
        self.n = 0

    def mean(self):
        return self.sum / self.n

    def add(self, loss):
        self.sum += loss
        self.n += 1