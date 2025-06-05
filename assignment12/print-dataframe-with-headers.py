import pandas as pd

# Define DFPlus as a subclass of pandas.DataFrame
class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        # Ensure operations on DFPlus return DFPlus, not regular DataFrame
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        
        df = pd.read_csv(filepath, **kwargs)
        
        return cls(df)

    def print_with_headers(self):
        
        total_rows = len(self)
        # Print 10 rows at a time
        for start in range(0, total_rows, 10):
            end = start + 10
            # Print a header
            print("\n" + "-" * 40)
            print(f"Rows {start + 1} to {min(end, total_rows)}:")
            print("-" * 40)
            # Print the current slice of rows
            print(super().iloc[start:end])


if __name__ == "__main__":
    # Load the CSV as DFPlus instance
    dfp = DFPlus.from_csv("../python_homework/csv/products.csv")

    
    dfp.print_with_headers()
